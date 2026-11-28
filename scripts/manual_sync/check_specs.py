"""Read-only, per-article audit of Specifications cells and Response HEAD arrays.

Normalization (applied after tracking missing source cells)
  Field                 Presentation equivalences
  All scalar cells      Markdown code/bold, escaped Markdown delimiters, NBSP
  Default/Required      Standalone dash/blank markers, surrounding literal quotes
  Value Type            Above, spacing around brackets/parentheses, type-name case
  Response HEAD         JSON formatting only. Order, case and repeated columns matter.

Exit 1 for an actual difference, 0 otherwise. Argument errors use exit 2.
"""

import argparse
from collections import Counter, defaultdict
import json
from pathlib import Path
import re
import sys

from build_index import anchor
from check_coverage import fetch_bodies
from index_articles import variant_pairs
from restore_descriptions import PIPE
from spec_source import named_mode, parse_article

ROOT = Path(__file__).resolve().parents[2]
HOLDS = Path(__file__).with_name("spec_holds.json")
FIELDS = ("default", "type", "required", "response_head")
LABELS = dict(zip(FIELDS, ("기본값", "Value 타입", "필수", "Response HEAD")))
STATUSES = ("일치", "서식만 다름", "실제 차이", "모호", "원문 없음", "보류")
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
    "value type": "type", "value 타입": "type", "타입": "type",
    "default": "default", "default value": "default", "기본값": "default", "기본값/enum": "default",
    "required": "required", "필수": "required",
}


def surface(value):
    return re.sub(r'\\([\[\]_|])', r'\1', value.replace("`", "").replace("**", "")).replace("\xa0", " ").strip()


def normalize(field, raw):
    if field == "response_head":
        return tuple(raw)
    text = surface(raw)
    if text in BLANKS:
        return ""
    if len(text) > 1 and text[0] == text[-1] and text[0] in "\"'" and text.count(text[0]) == 2:
        text = text[1:-1]
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


def local_rows(lines, scope):
    columns = {}
    for n, (line, context) in enumerate(zip(lines, scope)):
        if context is None or not line.lstrip().startswith("|"):
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
                name: cells[i] for name, i in columns.items() if name in FIELDS}


class Sources:
    def __init__(self, index, chunks):
        self.variants = defaultdict(set)
        chunk_locations = defaultdict(set)
        for record in index["endpoints"]:
            for article in record["articles"]:
                aid = article["id"]
                self.variants[aid].update(variant_pairs(article))
                for location in article["locations"]:
                    for cid in location["chunk_ids"]:
                        chunk_locations[cid].add((aid, location["ref"]))
        self.lines = defaultdict(set)
        self.refs = defaultdict(set)
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
            for line in set(chunk["text"].splitlines()):
                self.lines[file, line.strip()].update((aid, location, False) for aid, location in refs)
                self.lines[file, line.strip()].update((aid, ref, True) for aid in chunk.get("candidate_articles", []))

    def choose(self, file, raw, context, hint):
        headings, generated = context
        if generated:
            return [generated], []
        indexed = self.lines.get((file, raw.strip()))
        refs = {ref: level for level, ref, _ in headings}
        located = [(refs[ref], not tentative, aid) for aid, ref, tentative in indexed or () if ref in refs]
        if located:
            rank = max((level, confirmed) for level, confirmed, _ in located)
            candidates = {aid for level, confirmed, aid in located if (level, confirmed) == rank}
        elif indexed is None and HEADING.match(raw):
            # A heading need not be present in a continuation chunk.
            candidates = next((self.refs[ref] for _, ref, _ in reversed(headings) if self.refs[ref]), set())
        else:
            candidates = set()
        if len(candidates) > 1:
            declared = set().union(*(self.variants[aid] for aid in candidates))
            modes = named_mode(hint, declared)
            matched = {aid for aid in candidates if modes and modes <= self.variants[aid]}
            if matched:
                return sorted(matched), sorted(modes)
        return sorted(candidates), []


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
    return (record["file"], record["article_id"], tuple(sorted(record["keys"])), record["no"], record["field"])


def load_holds(path):
    holds = {}
    for item in json.loads(path.read_text(encoding="utf-8"))["holds"]:
        key = hold_key(item)
        if key in holds:
            raise ValueError(f"Duplicate spec hold: {key}")
        holds[key] = item
    return holds


def compare(record, official, holds):
    field, local = record["field"], record["local"]
    record["official"] = official
    hold = holds.get(hold_key(record))
    if hold and (hold["om_value"] != official or hold["doc_value"] != local):
        record.update(status="실제 차이", reason="등록된 보류의 문서 값 또는 원문 값이 달라짐")
    elif hold and local != official:
        record.update(status="보류", reason=hold["reason"])
    elif official is None or (field != "response_head" and official == ""):
        record.update(status="원문 없음", reason="공식 표에 값이 없거나 응답 예제에 HEAD가 없음")
    elif local == official:
        record["status"] = "일치"
    elif normalize(field, local) == normalize(field, official):
        record["status"] = "서식만 다름"
    else:
        record["status"] = "실제 차이"
    return record


def compare_cell(record, parsed, holds):
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
    out = compare(record, official, holds)
    if rows and out["status"] in {"실제 차이", "보류"}:
        out["official_rows"] = [{k: row[k] for k in ("no", "type", "default", "required", "group")} for row in rows]
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
        stage = "Stage" in record["local"]
        filtered = [row for row in picked if ("Stage" in row["value"]) == stage]
    if filtered:
        picked = filtered
    values = {tuple(r["value"]) for r in picked}
    explicit = {tuple(r["value"]) for r in picked if r["source"] == "heading"}
    if len(values) > 1 and (not modes or len(explicit) > 1 or len({tuple(x["variants"]) for x in picked}) > 1):
        return dict(record, status="모호", reason="공식 HEAD 배열이 여러 판별 값 또는 응답 조건으로 나뉨", official_candidates=picked)
    if tuple(record["local"]) in values:
        return compare(record, record["local"], holds)
    if len(values) != 1:
        return dict(record, status="모호", reason="같은 판별 값의 공식 HEAD 예제가 여러 형태임", official_candidates=picked)
    record["official_examples"] = picked
    return compare(record, list(next(iter(values))), holds)


def analyze(files, articles, sources, holds):
    parsed = {}
    records = []

    def add(record, context, line, prefix="", previous=""):
        candidates, modes = sources.choose(record["file"], line, context, prefix)
        record.update(article_id=candidates[0] if len(candidates) == 1 else None, candidates=candidates,
                      locale=None, official=None, variants=modes, reason="")
        aid = record["article_id"]
        if aid not in articles:
            reason = "색인에 글 출처 없음" if not candidates else "색인과 판별 값으로 글을 하나로 정할 수 없음"
            if aid:
                reason = "색인이 가리키는 공식 글 본문을 가져오지 못함"
            records.append(dict(record, status="모호", reason=reason))
            return
        official = articles[aid]
        record.update(locale=official.get("locale"), url=official.get("html_url"))
        if aid not in parsed:
            parsed[aid] = parse_article(official, sources.variants[aid])
        if record["field"] == "response_head":
            result = compare_head(record, parsed[aid], sources.variants[aid], prefix, previous, holds)
        else:
            result = compare_cell(record, parsed[aid], holds)
        records.append(result)

    for path in files:
        text = path.read_text(encoding="utf-8")
        lines, scope = local_sections(path, text)
        for n, keys, no, values in local_rows(lines, scope):
            headings, _ = scope[n]
            prefix = " ".join(lines[start] for _, _, start in headings)
            for field, value in values.items():
                add(dict(file=path.name, line=n + 1, no=no, keys=keys, field=field, local=value),
                    scope[n], lines[n], prefix)
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
                         local=value, head_kind=kind), scope[n], lines[line_no] or lines[n], prefix, previous)
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
    args = parser.parse_args(argv)
    docs = ROOT / "docs/manual"
    files = sorted(docs.glob("[0-9]*.md"))
    if args.file:
        files = [p for p in files if p.name == args.file]
        if not files:
            parser.error("--file must name an existing numbered chapter")
    index_dir = ROOT / "docs/index"
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
