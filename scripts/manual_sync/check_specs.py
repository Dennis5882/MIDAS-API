"""Read-only, per-article audit of Specifications cells and Response HEAD arrays.

Normalization (applied after tracking missing source cells)
  Field                 Presentation equivalences
  All scalar cells      Markdown code/bold, escaped Markdown delimiters, NBSP
  Default/Required      Standalone dash/blank markers, surrounding literal quotes
  Default               Boolean/Empty marker case, exact numeric and JSON value equivalence
  Required              Quotes and spacing in method-only markers (e.g. GET only)
  Value Type            Above, spacing around brackets/parentheses, type-name case
  Response HEAD         JSON formatting only. Order, case and repeated columns matter.

Exit 1 for an actual difference, 0 otherwise. Argument errors use exit 2.
"""

import argparse
from collections import Counter, defaultdict
from decimal import Decimal, InvalidOperation
import json
from pathlib import Path
import re
import sys

from build_index import anchor
from check_coverage import fetch_bodies
from index_articles import variant_pairs
from restore_descriptions import PIPE
from spec_qualifiers import CONDITIONAL, SUFFIX, ChapterSchemas
from spec_source import named_mode, parse_article

ROOT = Path(__file__).resolve().parents[2]
HOLDS = Path(__file__).with_name("spec_holds.json")
FIELDS = ("default", "type", "required", "response_head")
LABELS = dict(zip(FIELDS, ("기본값", "Value 타입", "필수", "Response HEAD")))
STATUSES = ("일치", "서식만 다름", "저장소 보강", "실제 차이", "모호", "원문 없음", "보류")
BRIDGE_CHAPTER = "28_Design_RC_AASHTO_LRFD.md"
BRIDGE_CODES = {"AASHTO-LRFD24", "AASHTO-LRFD20"}
METHOD_ONLY = re.compile(r'(?:"(GET|POST|PUT|DELETE|PATCH)"|(GET|POST|PUT|DELETE|PATCH))\s*only')
TYPE_WORD = re.compile(r'"[^"\n]*"|(?<![\w-])(?:array|object|bool|boolean|integer|int|number|float|double|'
                       r'string|null|enum|list|tuple)(?![\w-])', re.I)
BLANKS = {"", "-", "–", "—", '""', "''", "Blank"}
HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
MARKER = re.compile(r"^<!-- om-fields:(\d+) -->")
ARRAY = re.compile(r'\[\s*"')
KEY = re.compile(r"[A-Za-z0-9_$][\w$.-]*")
HEAD_LABEL = re.compile(r"^response head\b", re.I)
HEAD_CONTEXT = re.compile(r"시공단계|Construction Stage|\bCS\b", re.I)
HEAD_NON_STAGE = re.compile(r"General|Post CS|일반|후시공", re.I)
ROOT_LIST = re.compile(r'^\s*[-*]\s+`([^`]+)`\s*$', re.M)
TABLE_HEADERS = {
    "key": "key", "키": "key", "no.": "no", "sub-no.": "no",
    "description": "description", "설명": "description",
    "value type": "type", "value 타입": "type", "타입": "type",
    "default": "default", "default value": "default", "기본값": "default", "기본값/enum": "default",
    "required": "required", "필수": "required",
}


def surface(value):
    return re.sub(r'\\([\[\]_|])', r'\1', value.replace("`", "").replace("**", "")).replace("\xa0", " ").strip()


def canonical_json(value):
    if isinstance(value, Decimal):
        sign, digits, exponent = value.as_tuple()
        if not value:
            return "0"
        keep = len(digits)
        while digits[keep - 1] == 0:
            keep -= 1
        return str(Decimal((sign, digits[:keep], exponent + len(digits) - keep)))
    if isinstance(value, list):
        return "[" + ",".join(map(canonical_json, value)) + "]"
    if isinstance(value, dict):
        return "{" + ",".join(f"{json.dumps(key)}:{canonical_json(value[key])}" for key in sorted(value)) + "}"
    return json.dumps(value, allow_nan=False)


def normalize_default(raw, text):
    if text.casefold() in {"true", "false", "empty"}:
        return text.casefold()
    # Strip Markdown around the cell before reading JSON. Preserve Markdown
    # characters that occur inside a JSON string value.
    literal = raw.strip()
    for marker in ("**", "`"):
        if literal.startswith(marker) and literal.endswith(marker):
            literal = literal[len(marker):-len(marker)].strip()
    if literal.startswith(("[", "{")):
        candidate = literal
    elif text and (text[0].isdigit() or text[0] == "-"):
        candidate = text
    else:
        return text
    try:
        value = json.loads(candidate, parse_int=Decimal, parse_float=Decimal)
        return canonical_json(value)
    except (ValueError, InvalidOperation):
        return candidate


def normalize(field, raw):
    if field == "response_head":
        return tuple(raw)
    text = surface(raw)
    if text in BLANKS:
        return ""
    if len(text) > 1 and text[0] == text[-1] and text[0] in "\"'" and text.count(text[0]) == 2:
        text = text[1:-1]
    if field == "default":
        return normalize_default(raw, text)
    if field == "required" and (match := METHOD_ONLY.fullmatch(text)):
        return f"{match[1] or match[2]} only"
    if field == "type":
        text = " ".join(text.split())
        text = re.sub(r'\s*([\[\](),])\s*', r'\1', text)
        text = TYPE_WORD.sub(lambda m: m[0] if m[0].startswith('"') else m[0].lower(), text)
    return text


def clean_keys(cell):
    quoted = re.findall(r'"([^"`]+)"', cell)
    if quoted:
        return sorted({value for item in quoted if KEY.fullmatch(value := item.strip())})
    paths = re.findall(r'`([^`]+)`', cell) or [cell]
    return sorted({value for item in paths if KEY.fullmatch(value := surface(item))})


def local_sections(path, text):
    stack, scope, generated, fenced = [], [], None, None
    lines = text.splitlines()
    for n, line in enumerate(lines):
        fence = re.match(r'^\s*(`{3,}|~{3,})', line)
        if fence:
            marker = fence[1][0]
            fenced = None if marker == fenced else fenced or marker
            scope.append(None)
            continue
        if not fenced:
            heading = HEADING.match(line)
            if heading:
                level = len(heading[1])
                while stack and stack[-1][0] >= level:
                    stack.pop()
                ref = f"{path.name}#{anchor({'path': str(path), 'start': n, 'heading': line})}"
                stack.append((level, ref, n))
            if match := MARKER.match(line):
                generated = match[1]
            elif line.startswith("<!-- /om-fields -->"):
                generated = None
        scope.append((tuple(stack), generated) if not fenced else None)
    return lines, scope


def local_rows(lines, scope=None):
    columns = {}
    for n, line in enumerate(lines):
        if (scope is not None and scope[n] is None) or not line.lstrip().startswith("|"):
            columns = {}
            continue
        cells = [cell.strip() for cell in PIPE.split(line.strip())[1:-1]]
        names = [TABLE_HEADERS.get(surface(cell).casefold()) for cell in cells]
        if "key" in names and any(name in FIELDS for name in names):
            columns = {name: i for i, name in enumerate(names) if name}
            continue
        if not columns or max(columns.values()) >= len(cells):
            continue
        keys = clean_keys(cells[columns["key"]])
        if keys:
            yield n, keys, cells[columns["no"]] if "no" in columns else "", {
                name: cells[i] for name, i in columns.items() if name in FIELDS}, columns


def required_row_key(line, column):
    parts = PIPE.split(line.strip())
    slot = column + 1
    return column, tuple(parts[:slot] + parts[slot + 1:])


class Sources:
    def __init__(self, index, chunks):
        self.variants = defaultdict(set)
        self.bridge_codes = defaultdict(set)
        chunk_locations = defaultdict(set)
        for record in index["endpoints"]:
            for article in record["articles"]:
                aid = article["id"]
                self.variants[aid].update(variant_pairs(article))
                prefix = record.get("endpoint", "").split("/")[:3]
                if len(prefix) == 3 and prefix[:2] == ["DESIGN", "RC"] and prefix[2] in BRIDGE_CODES:
                    self.bridge_codes[aid].add(prefix[2])
                if prefix == ["DESIGN", "RC", "DRC"]:
                    self.bridge_codes[aid].update(article["variants"].get("DGNCODE", ()))
                for location in article["locations"]:
                    for cid in location["chunk_ids"]:
                        chunk_locations[cid].add((aid, location["ref"]))
        self.lines = defaultdict(set)
        self.refs = defaultdict(set)
        self.required_rows = defaultdict(set)
        for chunk in chunks:
            if chunk["source"] == "repo-example":
                continue
            file = chunk["file"]
            ref = f"{file}#{chunk['anchor']}"
            refs = chunk_locations[chunk["id"]]
            located_ids = {aid for aid, _ in refs}
            # URI-less official appendices still have exact chunk attribution.
            refs |= {(aid, ref) for aid in chunk["articles"] if aid not in located_ids}
            for aid, location in refs:
                self.refs[location].add(aid)
            attributed = {(aid, location, False) for aid, location in refs}
            attributed.update((aid, ref, True) for aid in chunk.get("candidate_articles", []))
            lines = chunk["text"].splitlines()
            for line in set(lines):
                self.lines[file, line.strip()].update(attributed)
            for n, _, _, _, columns in local_rows(lines):
                if "required" in columns:
                    signature = required_row_key(lines[n], columns["required"])
                    self.required_rows[file, signature].update(attributed)

    def choose(self, file, raw, context, hint, required_column=None):
        headings, generated = context
        if generated:
            return [generated], []
        indexed = self.lines.get((file, raw.strip()))
        refs = {ref: level for level, ref, _ in headings}
        located = [(refs[ref], not tentative, aid) for aid, ref, tentative in indexed or () if ref in refs]
        # A required-cell normalization can precede publication of the next
        # index. Reuse provenance only when the section and every other cell match.
        if not located and required_column is not None:
            signature = required_row_key(raw, required_column)
            indexed_rows = self.required_rows.get((file, signature), ())
            located = [(refs[ref], not tentative, aid) for aid, ref, tentative in indexed_rows if ref in refs]
        if located:
            rank = max((level, confirmed) for level, confirmed, _ in located)
            candidates = {aid for level, confirmed, aid in located if (level, confirmed) == rank}
        elif indexed is None and HEADING.match(raw):
            # A heading need not be present in a continuation chunk.
            candidates = next((self.refs[ref] for _, ref, _ in reversed(headings) if self.refs[ref]), set())
        else:
            candidates = set()
        if len(candidates) > 1 and not self.shared_bridge(file, candidates):
            declared = set().union(*(self.variants[aid] for aid in candidates))
            modes = named_mode(hint, declared)
            matched = {aid for aid in candidates if modes and modes <= self.variants[aid]}
            if matched:
                return sorted(matched), sorted(modes)
        return sorted(candidates), []

    def shared_bridge(self, file, candidates):
        codes = [self.bridge_codes[aid] for aid in candidates]
        return (file == BRIDGE_CHAPTER and len(codes) == 2 and all(len(code) == 1 for code in codes)
                and set.union(*codes) == BRIDGE_CODES)


def source_rows(parsed, keys, no):
    indexed = parsed["rows"]
    # A local field path can spell out a parent which the official Key cell
    # omits. Exact Key spellings still take precedence over a leaf lookup.
    leaf_keys = {key if key in indexed else key.rsplit(".", 1)[-1] for key in keys}
    first = min(leaf_keys)
    selected = [row for row in indexed.get(first, ()) if leaf_keys <= set(row["keys"])]
    if len(selected) > 1 and no:
        def number(value):
            return re.sub(r"(?<=\d)-(?=\d)", ".", surface(value).rstrip("."))

        numbered = [row for row in selected if number(row["no"]) == number(no)]
        if numbered:
            return numbered
    return selected


def hold_key(record):
    key = (record["file"], record["article_id"], tuple(sorted(record["keys"])), record["no"], record["field"])
    if "section" in record:
        key += (record["section"],)
    if "description_ref" in record:
        key += (record["description_ref"],)
    return key


def registered_hold(record, holds):
    key = hold_key(record)
    return holds.get(key) or holds.get(key[:6]) or holds.get(key[:5])


def load_holds(path):
    holds = {}
    for item in json.loads(path.read_text(encoding="utf-8"))["holds"]:
        key = hold_key(item)
        if key in holds:
            raise ValueError(f"Duplicate spec hold: {key}")
        holds[key] = item
    return holds


def added_qualifier(field, local, official):
    if field == "response_head" or not official or (field == "required" and CONDITIONAL.fullmatch(surface(local))):
        return None
    if match := SUFFIX.fullmatch(surface(local)):
        base, qualifier = match.groups()
        if field == "type" and qualifier.startswith("enum:") and SUFFIX.fullmatch(surface(official)):
            base += " (enum)"
        if normalize(field, base) == normalize(field, official):
            return qualifier.strip()
    return None


def compare(record, official, holds, schema_evidence=None):
    field, local = record["field"], record["local"]
    record["official"] = official
    hold = registered_hold(record, holds)
    if hold and "om_variant" in hold:
        hold = None  # compare_head checks variant-specific holds against official examples.
    if hold and (hold["om_value"] != official or hold["doc_value"] != local):
        record.update(status="실제 차이", reason="등록된 보류의 문서 값 또는 원문 값이 달라짐")
    elif official is None or (field != "response_head" and official == ""):
        if hold and local != official:
            record.update(status="보류", reason=hold["reason"])
        else:
            record.update(status="원문 없음", reason="공식 표에 값이 없거나 응답 예제에 HEAD가 없음")
    elif local == official:
        record["status"] = "일치"
    elif normalize(field, local) == normalize(field, official):
        record["status"] = "서식만 다름"
    else:
        qualifier = added_qualifier(field, local, official)
        if qualifier:
            record["qualifier"] = qualifier
            evidence = schema_evidence(qualifier) if field == "type" and schema_evidence else []
            if field != "type" or evidence:
                record.update(status="저장소 보강", reason="공식 값에 한정자만 추가됨")
                if evidence:
                    record["schema_evidence"] = evidence
                return record
            record["reason"] = "타입 한정자의 근거를 같은 섹션의 JSON Schema에서 확인하지 못함"
        if hold:
            record.update(status="보류", reason=hold["reason"])
        else:
            record["status"] = "실제 차이"
    return record


def required_schema_support(parsed, keys, local):
    """Use an explicit required array for the field's own schema object."""
    expected = surface(local)
    if expected not in {"Required", "Optional"}:
        return []
    proof = []
    for key in keys:
        *parents, leaf = key.split(".")
        nodes = parsed["schema"].get(key) or parsed["schema"].get(leaf, ())
        scoped = [node for node in nodes if all(parent in node["path"] for parent in parents)]
        fields = [node for node in scoped if "type" in node or "enum" in node or "const" in node]
        if not fields or any(node["required_keys"] is None or node["required"] != (expected == "Required")
                             for node in fields):
            return []
        if expected == "Optional" and any(node["required"] for node in scoped):
            return []
        proof.extend({"key": key, "schema_path": node["path"],
                      "required": node["required_keys"]} for node in fields)
    return proof


def default_schema_support(parsed, keys, local):
    proof = []
    for key in keys:
        *parents, leaf = key.split(".")
        nodes = parsed["schema"].get(key) or parsed["schema"].get(leaf, ())
        defaults = [node for node in nodes if "default" in node and all(parent in node["path"] for parent in parents)]
        if not defaults or any(normalize("default", json.dumps(node["default"])) != normalize("default", local)
                               for node in defaults):
            return []
        proof.extend({"key": key, "schema_path": node["path"], "default": node["default"]} for node in defaults)
    return proof


def compare_cell(record, parsed, holds, schema_evidence=None):
    rows = source_rows(parsed, record["keys"], record["no"])
    if not rows and parsed["has_specs"] and not parsed["rows"]:
        if parsed["unnamed_spec_rows"] and not parsed["unparsed_spec_rows"]:
            return dict(compare(record, None, holds), reason="공식 Specifications 표의 Key 칸이 비어 있음")
        return dict(record, status="모호", reason="공식 Specifications에서 Key 열을 파싱하지 못함")
    field = record["field"]
    choices = list(dict.fromkeys(row[field] for row in rows))
    if choices and len({normalize(field, value) for value in choices}) > 1:
        return dict(record, status="모호", reason="공식 표에 같은 Key의 값이 여러 개 있음", official_candidates=choices)
    official = next((value for value in choices if value == record["local"]), choices[0] if choices else None)
    out = compare(record, official, holds, schema_evidence)
    if official in {"-", "–", "—"} and out["status"] == "실제 차이" and not registered_hold(record, holds):
        for target, supported, keyword in (("required", required_schema_support, "required"),
                                           ("default", default_schema_support, "default")):
            if field == target and (proof := supported(parsed, record["keys"], record["local"])):
                out.update(status="저장소 보강", reason=f"표기를 공식 글 JSON Schema의 {keyword}에서 확인함",
                           schema_evidence=proof)
    if rows and out["status"] in {"실제 차이", "저장소 보강", "보류"}:
        out["official_rows"] = [{k: row[k] for k in ("no", "type", "default", "required", "group", "desc")} for row in rows]
    return out


def local_heads(lines, scope):
    for n, line in enumerate(lines):
        heading = HEADING.match(line)
        if not (heading and scope[n] and HEAD_LABEL.match(heading[2])):
            continue
        end = next((i for i in range(n + 1, len(lines)) if scope[i] and scope[i][0] and
                    scope[i][0][-1][2] == i and scope[i][0][-1][0] <= len(heading[1])), len(lines))
        # A warning can quote a separate HEAD. Its blockquote is explanatory,
        # so it does not become a normative array in this section.
        text = "\n".join("" if part.lstrip().startswith(">") else part for part in lines[n + 1:end])
        found = []
        for match in ARRAY.finditer(text):
            try:
                value, _ = json.JSONDecoder().raw_decode(text[match.start():])
            except ValueError:
                continue
            if isinstance(value, list) and all(isinstance(x, str) for x in value):
                line_no = n + 1 + text.count("\n", 0, match.start())
                before = text[:match.start()].rsplit("\n", 2)
                prefix = before[-1]
                previous = before[-2] if len(before) > 1 else ""
                found.append((line_no, value, prefix, previous, "columns"))
        if not found and "최상위 Key" in text:
            roots = ROOT_LIST.findall(text)
            if roots:
                found.append((n, roots, "", "", "top_level_keys"))
        yield n, found


def compare_head(record, parsed, declared, prefix, previous, holds):
    modes = named_mode(prefix, declared)
    if not modes and len(declared) == 1:
        modes = declared
    record["variants"] = sorted(modes)
    roots = record["head_kind"] == "top_level_keys"
    if roots:
        available = parsed["roots"]
    else:
        subtables = {r["path"][-1] for r in parsed["heads"] if r["subtable"] and r["path"]}
        subtable = {name for name in subtables if f"`{name}`" in prefix}
        if not subtable and re.search(r'`HEAD`|하위', prefix):
            subtable = {name for name in subtables if f"`{name}`" in previous}
        named = "SUB_TABLES" in prefix or "하위" in prefix
        available = [r for r in parsed["heads"] if (r["path"] and r["path"][-1] in subtable)
                     or (not subtable and r["subtable"] == named)]
    notes = [note for note in parsed["parse_notes"] if note["section"].startswith(("response", "examples"))
             and note["note"].startswith("JSON 파싱 실패")]
    hold = registered_hold(record, holds)
    if hold and "om_variant" in hold and modes == {tuple(pair) for pair in hold["doc_variant"]}:
        source_mode = {tuple(pair) for pair in hold["om_variant"]}
        expected_mode = {tuple(pair) for pair in hold["doc_variant"]}
        observed = [row for row in available if source_mode <= {tuple(pair) for pair in row["variants"]}]
        corrected = any(expected_mode <= {tuple(pair) for pair in row["variants"]} for row in available)
        record["official_examples"] = observed
        if (not corrected and modes == expected_mode and record["local"] == hold["doc_value"]
                and {tuple(row["value"]) for row in observed} == {tuple(hold["om_value"])}):
            return dict(record, status="보류", reason=hold["reason"], official=hold["om_value"])
        return dict(record, status="실제 차이", reason="등록된 원문 판별 값 또는 HEAD가 달라짐",
                    official_candidates=observed)
    if not available:
        if notes:
            return dict(record, status="모호", reason="공식 응답 JSON 파싱 실패", parse_notes=notes)
        return compare(record, None, holds)
    if modes:
        picked = [row for row in available if modes & {tuple(pair) for pair in row["variants"]}]
        if not picked:
            return dict(record, status="모호", reason="공식 HEAD 예제에 해당 판별 값 연결 근거 없음", official_candidates=available)
    else:
        picked = available
    if roots:
        filtered = picked
    elif HEAD_NON_STAGE.search(prefix):
        filtered = [row for row in picked if "Stage" not in row["value"]]
    elif HEAD_CONTEXT.search(prefix):
        filtered = [row for row in picked if "Stage" in row["value"] or
                    (HEAD_CONTEXT.search(row["caption"]) and not HEAD_NON_STAGE.search(row["caption"]))]
    else:
        filtered = picked
    if filtered:
        picked = filtered
    values = {tuple(r["value"]) for r in picked}
    record["official_examples"] = picked
    if tuple(record["local"]) in values:
        return compare(record, record["local"], holds)
    if len(values) != 1:
        return dict(record, status="실제 차이", reason="비교 대상 공식 응답 배열과 모두 다름", official_candidates=picked)
    return compare(record, list(next(iter(values))), holds)


def consensus(record, compared):
    field = record["field"]
    record["article_ids"] = [result["article_id"] for result in compared]
    record["source_results"] = compared
    record["locale"] = ", ".join(sorted({result["locale"] for result in compared}))
    if any(result["status"] == "모호" for result in compared):
        return dict(record, status="모호", reason="LRFD24·LRFD20 중 공식 값이 확정되지 않은 글이 있음")

    def values(result):
        if field == "response_head" and result.get("official_examples"):
            return {tuple(item["value"]) for item in result["official_examples"]}
        value = result["official"]
        return {normalize(field, value)} if value not in (None, "") else {None}

    if values(compared[0]) != values(compared[1]):
        return dict(record, status="모호", reason="LRFD24·LRFD20의 공식 값이 다름",
                    official_candidates=[result.get("official_candidates", result["official"]) for result in compared])
    # If the source literals differ only in presentation, keep the source
    # that exactly matches the local spelling as the display value.
    representative = next((row for row in compared if row["status"] == "일치"), compared[0])
    return dict(representative, article_id=None, url=None, locale=record["locale"],
                article_ids=record["article_ids"], source_results=compared)


def analyze(files, articles, sources, holds):
    parsed = {}
    records = []

    def add(record, context, line, prefix="", previous="", schema_evidence=None, required_column=None):
        candidates, modes = sources.choose(record["file"], line, context, prefix, required_column)
        record.update(article_id=candidates[0] if len(candidates) == 1 else None, candidates=candidates,
                      locale=None, official=None, variants=modes, reason="")
        aid = record["article_id"]
        shared = sources.shared_bridge(record["file"], candidates)
        article_ids = candidates if shared else [aid]
        if any(article_id not in articles for article_id in article_ids):
            reason = "색인에 글 출처 없음" if not candidates else "색인과 판별 값으로 글을 하나로 정할 수 없음"
            if aid or shared:
                reason = "색인이 가리키는 공식 글 본문을 가져오지 못함"
            records.append(dict(record, status="모호", reason=reason))
            return
        compared = []
        for article_id in article_ids:
            official = articles[article_id]
            item = dict(record, article_id=article_id, locale=official.get("locale"), url=official.get("html_url"))
            if article_id not in parsed:
                parsed[article_id] = parse_article(official, sources.variants[article_id])
            if record["field"] == "response_head":
                result = compare_head(item, parsed[article_id], sources.variants[article_id], prefix, previous, holds)
            else:
                result = compare_cell(item, parsed[article_id], holds, schema_evidence)
            compared.append(result)
        records.append(consensus(record, compared) if shared else compared[0])

    for path in files:
        text = path.read_text(encoding="utf-8")
        lines, scope = local_sections(path, text)
        schemas = ChapterSchemas(lines, scope)
        for n, keys, no, values, columns in local_rows(lines, scope):
            headings, _ = scope[n]
            prefix = " ".join(lines[start] for _, _, start in headings)
            for field, value in values.items():
                record = dict(file=path.name, line=n + 1, no=no, keys=keys, field=field, local=value,
                              section=headings[-1][1].partition("#")[2] if headings else "")
                if "description" in columns:
                    record["description_ref"] = PIPE.split(lines[n].strip())[columns["description"] + 1].strip()
                if field == "required":
                    record["column"] = columns[field]
                    record["generated"] = bool(scope[n][1])
                    if "description_ref" in record:
                        record["description"] = record["description_ref"]
                add(record, scope[n], lines[n], prefix, schema_evidence=lambda q: schemas.support(scope[n], keys, q),
                    required_column=columns.get("required"))
        for n, arrays in local_heads(lines, scope):
            if not arrays:
                candidates, modes = sources.choose(path.name, lines[n], scope[n], lines[n])
                aid = candidates[0] if len(candidates) == 1 else None
                records.append(dict(file=path.name, line=n + 1, no="", keys=["HEAD"], field="response_head",
                                    local=None, official=None, variants=modes, article_id=aid, candidates=candidates,
                                    locale=articles.get(aid, {}).get("locale"), status="모호",
                                    reason="로컬 Response HEAD에 비교 가능한 문자열 배열이 없음"))
            for line_no, value, prefix, previous, kind in arrays:
                keys = ["HEAD"] if kind == "columns" else ["response_root"]
                add(dict(file=path.name, line=line_no + 1, no="", keys=keys, field="response_head",
                         local=value, head_kind=kind, section=scope[n][0][-1][1].partition("#")[2]),
                    scope[n], lines[line_no] or lines[n], prefix, previous)
    records.sort(key=lambda r: (r["file"], r["line"], FIELDS.index(r["field"])))
    return records, parsed


def summarize(records):
    fields = defaultdict(Counter)
    chapters = defaultdict(Counter)
    for row in records:
        fields[row["field"]][row["status"]] += 1
        chapters[row["file"]][row["status"]] += 1
    return {"by_field": dict(fields), "by_chapter": dict(chapters), "records": records}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--json", action="store_true", help="emit all records and counts as JSON")
    parser.add_argument("--file", help="one chapter filename under docs/manual")
    parser.add_argument("--source", type=Path, help="use a saved official article bundle instead of fetching")
    parser.add_argument("--index-dir", type=Path, default=ROOT / "docs/index", help="use a different generated index directory")
    args = parser.parse_args(argv)
    docs = ROOT / "docs/manual"
    files = sorted(docs.glob("[0-9]*.md"))
    if args.file:
        files = [p for p in files if p.name == args.file]
        if not files:
            parser.error("--file must name an existing numbered chapter")
    index_dir = args.index_dir
    index = json.loads((index_dir / "endpoints.json").read_text(encoding="utf-8"))
    if index.get("schema_version") != 2:
        parser.error("endpoint index must use schema version 2")
    with (index_dir / "chunks.jsonl").open(encoding="utf-8") as stream:
        sources = Sources(index, (json.loads(line) for line in stream if line.strip()))
    if args.source:
        bundle = json.loads(args.source.read_text(encoding="utf-8"))
        articles = bundle.get("articles", bundle)
    else:
        articles = fetch_bodies()
    records, _ = analyze(files, articles, sources, load_holds(HOLDS))
    summary = summarize(records)
    if args.json:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    else:
        for name, counts in summary["by_chapter"].items():
            print(name, " · ".join(f"{status} {counts[status]}" for status in STATUSES))
        for field in FIELDS:
            counts = summary["by_field"].get(field, Counter())
            print(LABELS[field], " · ".join(f"{status} {counts[status]}" for status in STATUSES))
        for row in records:
            if row["status"] in {"실제 차이", "모호"}:
                official = row.get("official_candidates", row["official"])
                print(f"{row['status']} {row['file']}:{row['line']} {','.join(row['keys'])} "
                      f"{LABELS[row['field']]} {row['local']!r} → {official!r} "
                      f"({row['article_id'] or ','.join(row['candidates']) or '-'}, {row['locale'] or '-'}) {row['reason']}")
    return int(any(row["status"] == "실제 차이" for row in records))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
