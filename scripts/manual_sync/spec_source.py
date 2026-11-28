"""Parse Specifications, JSON Schema and examples from the official manual."""

from collections import defaultdict
import html
import json
import re
from urllib.parse import unquote

from index_articles import HTML_HEADING, COPY_TEXT, SELECTORS
from om_parse import cell_text, spec_rows

COPY_BLOCK = re.compile(
    r'<(?P<tag>div|pre)\b(?P<attrs>[^>]*\bid\s*=\s*["\']copy[^"\']*["\'][^>]*|'
    r'(?<=pre)\b[^>]*)>(?P<text>.*?)</(?P=tag)>', re.I | re.S,
)
CAPTION = re.compile(r'<p\b[^>]*\bclass=["\'][^"\']*\bbtn_dropdown\b[^"\']*["\'][^>]*>(.*?)</p>', re.I | re.S)
WINDOWS_PATH = re.compile(r'("(?:EXPORT_PATH|[A-Z_]*FILE_PATH)"\s*:\s*")([A-Za-z]:\\(?:[^"\\]|\\.)*)(")')
BAD_ESCAPE = re.compile(r'\\\\|\\(?!["\\/bfnrt]|u[0-9a-fA-F]{4})')


def load_json(raw):
    raw = raw.replace("\xa0", " ").replace("\u200b", "").lstrip("\ufeff").strip()
    try:
        return json.loads(raw), ""
    except json.JSONDecodeError as first:
        # A copied Windows path can contain both illegal escapes and e.g. \t that
        # looks valid. Preserve all single separators in a path we can identify.
        fixed = WINDOWS_PATH.sub(lambda m: m[1] + re.sub(r'\\\\|\\', lambda sl: "\\\\", m[2]) + m[3], raw)
        fixed = BAD_ESCAPE.sub(lambda m: "\\\\", fixed)
        if fixed != raw:
            try:
                return json.loads(fixed), "불법 역슬래시 복구"
            except json.JSONDecodeError:
                pass
        return None, f"JSON 파싱 실패 ({first.msg}, 줄 {first.lineno})"


def objects(value, path=()):
    if isinstance(value, dict):
        yield path, value
        for key, child in value.items():
            yield from objects(child, (*path, key))
    elif isinstance(value, list):
        for child in value:
            yield from objects(child, path)


def variants(value):
    return {(key, obj[key]) for _, obj in objects(value) for key in SELECTORS
            if isinstance(obj.get(key), str)}


def example_blocks(block):
    start = 0
    for match in COPY_BLOCK.finditer(block):
        labels = CAPTION.findall(block[start:match.start()])
        label = " ".join(cell_text(labels[-1]).split()) if labels else ""
        source = COPY_TEXT.search(match["attrs"])
        visible = cell_text(match["text"])
        raw = unquote(html.unescape(source[2])) if source else visible
        value, note = load_json(raw)
        if value is None and source and visible.strip():
            retry, retry_note = load_json(visible)
            if retry is not None:
                value, note = retry, retry_note
        yield label, value, note
        start = match.end()


def named_mode(text, declared):
    return {(key, value) for key, value in declared
            if re.search(r'(?<![\w-])' + re.escape(value) + r'(?![\w-])', text)}


def caption_key(text):
    return re.sub(r'[^\w]+', '', text).casefold()


def request_mode(label, path, obj, requests, declared):
    explicit = variants(obj) | named_mode(" ".join((label, *path)), declared)
    if explicit:
        return explicit
    for matched in (
        [modes for name, _, modes in requests if label and caption_key(name) == caption_key(label)],
        [modes for _, names, modes in requests if path and path[0] in names],
    ):
        if matched and all(matched) and len({frozenset(modes) for modes in matched}) == 1:
            return matched[0]
    return declared if len(declared) == 1 else set()


def parse_article(article, declared=()):
    body = article.get("body") or ""
    body = re.sub(r'<(?:script|style)\b[^>]*>.*?</(?:script|style)>', '', body, flags=re.I | re.S)
    parsed = {"rows": defaultdict(list), "schema": defaultdict(list), "examples": defaultdict(list),
              "heads": [], "roots": [], "parse_notes": [], "has_specs": False,
              "unnamed_spec_rows": 0, "unparsed_spec_rows": 0}
    for row in spec_rows(body, scoped_groups=True):
        if not row["key_text"]:
            parsed["unnamed_spec_rows"] += 1
        elif not row["keys"]:
            parsed["unparsed_spec_rows"] += 1
        for key in row["keys"]:
            parsed["rows"][key].append(row)
    headings = list(HTML_HEADING.finditer(body))
    responses, requests = [], []
    declared = set(declared)
    for i, heading in enumerate(headings):
        title = " ".join(cell_text(heading[1]).split()).casefold()
        if title.startswith("specifications"):
            parsed["has_specs"] = True
        if not (title == "json schema" or title == "examples" or title.startswith(
                ("request example", "response example", "response head"))):
            continue
        end = next((m.start() for m in headings[i + 1:] if int(m[0][2]) <= int(heading[0][2])), len(body))
        block = body[heading.end():end]
        if title.startswith("response head"):
            text = cell_text(block)
            for match in re.finditer(r'\[\s*"', text):
                try:
                    head, _ = json.JSONDecoder().raw_decode(text[match.start():])
                except ValueError:
                    continue
                if isinstance(head, list) and all(isinstance(col, str) for col in head):
                    modes = named_mode(text[:match.start()].split("\n")[-1], declared)
                    parsed["heads"].append(head_entry(head, (), "Response HEAD", modes, "heading"))
        for label, value, note in example_blocks(block):
            if note:
                parsed["parse_notes"].append({"section": title, "caption": label, "note": note})
            if value is None:
                continue
            if title == "json schema":
                for path, obj in objects(value):
                    for key, schema in obj.get("properties", {}).items():
                        if isinstance(schema, dict):
                            evidence = {k: schema[k] for k in ("type", "default", "enum", "const", "readOnly") if k in schema}
                            for kind in ("oneOf", "anyOf", "allOf"):
                                if kind in schema:
                                    evidence[kind] = [{k: alt[k] for k in ("type", "const", "enum") if k in alt}
                                                      for alt in schema[kind] if isinstance(alt, dict)]
                            if isinstance(schema.get("items"), dict) and "type" in schema["items"]:
                                evidence["item_type"] = schema["items"]["type"]
                            parsed["schema"][key].append({"path": list(path), "required": key in obj.get("required", ()),
                                                          **evidence})
                continue
            has_head = any(isinstance(obj.get("HEAD"), list) for _, obj in objects(value))
            if title.startswith("response") or (title == "examples" and has_head):
                responses.append((label, value))
            else:
                request_variants = variants(value)
                declared |= request_variants
                names = {obj["TABLE_NAME"] for _, obj in objects(value) if isinstance(obj.get("TABLE_NAME"), str)}
                requests.append((label, names, request_variants))
                for path, obj in objects(value):
                    for key, prop in obj.items():
                        if not key.isdecimal():
                            sample = {"path": list(path), "caption": label, "value": prop}
                            if sample not in parsed["examples"][key]:
                                parsed["examples"][key].append(sample)
    for label, value in responses:
        if isinstance(value, dict):
            modes = request_mode(label, tuple(value), value, requests, declared)
            parsed["roots"].append(head_entry(list(value), (), label, modes, "response_root"))
        for path, obj in objects(value):
            head = obj.get("HEAD")
            if isinstance(head, list) and all(isinstance(col, str) for col in head):
                modes = request_mode(label, path, obj, requests, declared)
                parsed["heads"].append(head_entry(head, path, label, modes, "response_example"))
    return parsed


def head_entry(head, path, caption, modes, source):
    return {"value": head, "path": list(path), "caption": caption,
            "subtable": "SUB_TABLES" in path, "variants": sorted(modes), "source": source}
