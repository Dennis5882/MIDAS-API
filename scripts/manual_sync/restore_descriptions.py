"""Restore parameter descriptions/required cells from official Specifications tables.

Reuses the coverage mapping and OM parser; never edits generated om-fields blocks.
Apply to rows with Hangul descriptions. Run --dry-run to report drift in all supported rows.
Reports append each run to retain replaced descriptions across chapters and reruns.
Ambiguous/protected rows are left alone.
"""
import argparse
import collections
import datetime
import json
from pathlib import Path
import re
import sys

import check_fields as cf
from check_coverage import fetch_bodies, plain_text
from fill_fields import read, write
from om_parse import md_escape, spec_rows

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_REPORT = ROOT / "work_orders/2026-11-26_restore_source_descriptions_report.md"
HANGUL = re.compile(r"[가-힣]")
# Keep composite/path spellings in the inventory too; an exact OM match is still required.
KEY = re.compile(r'`"([^`]+)"`')
PIPE = re.compile(r"(?<!\\)\|")
RETAINED_GROUPS = {
    ("22_POST_TH_HY_Pushover.md", "39236753314073"): (
        {"STORY_NAME"},
        "원문 설명의 THIS_ELEMENT 참조가 기존 TYPE_ELEMENT 표기와 충돌하며, 복원 시 om-fields 블록이 사라짐",
    ),
    ("26_Design_RC_KDS41202022.md", "57426948142105"): (
        {"UNIT", "STYLES"},
        "공식 설명으로 바꾸면 HEAT/TEMP/FORMAT/PLACE의 문서 내 유일한 언급이 사라짐",
    ),
    ("26_Design_RC_KDS41202022.md", "57458836502553"): (
        {"REINFORCEMENT", "REINFORCEMENT_TYPE", "DISPLAY_MEMBERS", "OUTPUT_COMPONENT",
         "COLUMN_SECTION_SIZE", "VALUE_OPTION"},
        "원문 조건의 COMP/CHECK 참조가 기존 om-fields 행을 재생성 시 삭제하게 함",
    ),
}


def table_rows(text):
    """Yield physical lines/cell spans; escaped pipes, fences and generated blocks are safe."""
    fenced, generated = False, False
    for number, line in enumerate(text.split("\n")):
        if line.lstrip().startswith(("```", "~~~")):
            fenced = not fenced
        if "<!-- om-fields:" in line:
            generated = True
        if not fenced and not generated and line.startswith("|"):
            pipes = [m.start() for m in PIPE.finditer(line)]
            spans = list(zip([p + 1 for p in pipes[:-1]], pipes[1:]))
            cells = [line[a:b].strip(" \t") for a, b in spans]
            if len(cells) >= 6 and cells[2].startswith('`"'):
                keys = KEY.findall(cells[2])
                if keys:
                    yield number, line, cells, spans, keys
        if "<!-- /om-fields -->" in line:
            generated = False


def decorations(desc):
    prefix = re.match(r"^[ \u3000]*└\s*", desc)
    suffix = re.search(r"\s*(?:[ᴶᴴˢ]+⁾\s*)+$", desc)
    return prefix.group() if prefix else "", suffix.group() if suffix else ""


def render(row, old):
    prefix, suffix = decorations(old)
    desc = row["desc"]
    group = row["group"]
    # The official oneOf heading names the alternatives, not the columns after them.
    if group.startswith("oneOf ") and not any(f'"{key}"' in group for key in row["keys"]):
        group = ""
    if group and group not in desc:
        desc = f"[{group}] {desc}".strip()
    if suffix and desc.endswith(suffix.strip()):
        suffix = ""
    required = row["required"]
    if required.lower() == "required":
        required = f"**{required}**"
    return prefix + md_escape(desc) + suffix, md_escape(required)


def protected(cells, keys, host, aids, exclusions, section_text=None):
    if any("⚠" in c for c in cells):
        return "같은 행의 ⚠️ 표시"
    # A warning paragraph can wrap over physical lines. Use exact key token boundaries.
    if section_text is None:
        section_text = host["text"] if host else ""
    prose = re.sub(r"(?ms)^(?:```|~~~)[^\n]*\n.*?^(?:```|~~~)[^\n]*", "", section_text)
    prose = re.sub(r"(?m)^\|.*$", "", prose)
    for paragraph in re.split(r"\n\s*\n", prose):
        if "⚠" in paragraph and any(
            re.search(r"(?<![A-Za-z0-9_])" + re.escape(k) + r"(?![A-Za-z0-9_])", paragraph)
            for k in keys
        ):
            return "같은 섹션의 ⚠️ 주석에서 Key 언급"
    for item in exclusions:
        uri = item.get("uri", "").lstrip("/").upper()
        same = str(item.get("article_id", "")) in aids or (
            host and uri and uri in host["endpoints"]
        )
        if same and (item.get("type") != "field" or any(
            k == field or k == field.split(".")[-1]
            for k in keys for field in item.get("keys", [])
        )):
            return "jp_only.json exclude / needs_check"
    return ""


def pair(keys, no, aids, parsed):
    chosen = []
    for aid in sorted(aids):
        candidates = [r for r in parsed[aid] if set(keys) <= set(r["keys"])]
        if not candidates:
            continue
        if len(candidates) > 1:
            candidates = [r for r in candidates if r["no"] == no]
        if len(candidates) != 1:
            return "모호", [], f"OM {aid}: Key/No.로 후보를 하나로 좁히지 못함"
        chosen.append((aid, candidates[0]))
    if not chosen:
        return "짝 없음", [], "대응 섹션의 Specifications에 같은 Key 없음"
    signatures = {(r["desc"], r["group"], r["required"]) for _, r in chosen}
    if len(signatures) > 1:
        return "모호", chosen, "같은 섹션을 다루는 공식 글들의 설명/조건/필수가 다름"
    if not chosen[0][1]["desc"]:
        return "짝 없음", chosen, "공식 Description이 비어 있음"
    return "", chosen, ""


def loss_signals(old, new):
    """Conservative review hints, not a semantic equivalence claim."""
    signals = []
    missing_numbers = sorted(set(re.findall(r"\d+(?:\.\d+)?", old)) -
                             set(re.findall(r"\d+(?:\.\d+)?", new)))
    if missing_numbers:
        signals.append("원문에 없는 숫자: " + ", ".join(missing_numbers))
    for old_pattern, new_pattern, label in [
        (r"(?:\bmm\b|\bcm\b|kN|MPa|kPa|N/m|m/s|°|%|㎜|단위)",
         r"(?:\bmm\b|\bcm\b|kN|MPa|kPa|N/m|m/s|°|%|unit)", "단위 표현"),
        (r"(?:이상|이하|초과|미만|범위|\d\s*[-~–]\s*\d)",
         r"(?:range|greater|less|[<>≤≥]|\d\s*[-~–]\s*\d)", "범위 표현"),
        (r"(?:경우|이면|일 때|일때|전용|제외|조건)",
         r"(?:\bwhen\b|\bif\b|\bonly\b|except|exclud|condition)", "조건 표현"),
    ]:
        if re.search(old_pattern, old) and not re.search(new_pattern, new, re.I):
            signals.append(label)
    codes = set(re.findall(r'[`"]([A-Z][A-Z0-9_]+)[`"]', old))
    missing_codes = sorted(k for k in codes if not re.search(r"\b" + re.escape(k) + r"\b", new))
    if missing_codes:
        signals.append("원문에 없는 값: " + ", ".join(missing_codes))
    if re.search(r"[A-Z][A-Z0-9_]+\s*=\s*[가-힣]", old):
        signals.append("값별 한글 보충 설명")
    return signals


def comparable(value):
    value = value.replace("`", "").replace("**", "").replace("\\|", "|").strip()
    return "" if value in {"—", "-", "Blank", '""', ""} else re.sub(r"\s+", " ", value).lower()


def analyze(articles, files, *, korean_only=False):
    sections, _ = cf.load_sections()
    mapping = cf.mapped_headings()
    reverse = collections.defaultdict(set)
    parsed = {}
    for aid, article in articles.items():
        parsed[aid] = spec_rows(article.get("body"), scoped_groups=True)
        found, _ = cf.covering(aid, plain_text(article.get("body")), sections, mapping)
        for section in found:
            reverse[(section["file"], section["start"])].add(aid)
    jp = json.loads((ROOT / "docs/manual/jp_only.json").read_text(encoding="utf-8"))
    exclusions = jp.get("exclude", []) + jp.get("needs_check", [])
    records, outputs = [], {}
    for path in files:
        text, crlf = read(path)
        lines = text.split("\n")
        own = [s for s in sections if s["file"] == path.name]
        for number, line, cells, spans, keys in table_rows(text):
            korean = bool(HANGUL.search(cells[1]))
            if korean_only and not korean:
                continue
            containing = [s for s in own if s["start"] <= number < s["end"]]
            hosts = [s for s in containing if reverse[(s["file"], s["start"])]]
            host = min(hosts, key=lambda s: s["end"] - s["start"]) if hosts else None
            aids = reverse[(host["file"], host["start"])] if host else set()
            # Parameters subsections inherit warnings from their containing endpoint.
            parent = max((s for s in containing if s["level"] == 2),
                         key=lambda s: s["start"], default=host)
            item = dict(file=path.name, line=number + 1, keys=keys, old=cells[1],
                        old_required=cells[5], korean=korean,
                        aids=sorted(aids), status="", reason="", loss=[], differences=[])
            reason = protected(cells, keys, host, aids, exclusions, parent["text"] if parent else None)
            if reason:
                item.update(status="의도적 차이", reason=reason)
            else:
                status, chosen, reason = pair(keys, cells[0], aids, parsed)
                for aid, _ in chosen:
                    retained = RETAINED_GROUPS.get((path.name, aid))
                    if retained and retained[0].intersection(keys):
                        status, reason = "의도적 차이", retained[1]
                        break
                item.update(status=status, reason=reason, aids=[a for a, _ in chosen] or sorted(aids))
                if not status:
                    desc, required = render(chosen[0][1], cells[1])
                    item.update(new=desc, required=required)
                    item["loss"] = loss_signals(cells[1], desc + " " + required)
                    for aid, row in chosen:
                        for column, local, official in [("Value 타입", cells[3], row["type"]),
                                                         ("기본값", cells[4], row["default"])]:
                            if comparable(local) != comparable(official):
                                item["differences"].append((column, local, official, aid))
                    if (desc, required) == (cells[1], cells[5]):
                        item["status"] = "일치"
                    else:
                        item["status"] = "변경"
                        # Replace just the cell contents, preserving their surrounding padding.
                        for index, value in [(5, required), (1, desc)]:
                            a, b = spans[index]
                            raw = line[a:b]
                            left = len(raw) - len(raw.lstrip(" \t"))
                            right = len(raw) - len(raw.rstrip(" \t"))
                            if left == len(raw):
                                left, right = (1, 1) if len(raw) >= 2 else (left, 0)
                            line = line[:a + left] + value + line[b - right:]
                        lines[number] = line
            records.append(item)
        outputs[path] = (text, "\n".join(lines), crlf)
    return records, outputs


def cell(value):
    return PIPE.sub(lambda _: r"\|", str(value)).replace("\n", "<br>")


def make_report(records, dry_run):
    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
    out = ["# 공식 원문 설명 복원 보고서", "", f"- 기준: {now.isoformat(timespec='seconds')} (Asia/Seoul)",
           f"- 실행: {'dry-run (문서 미변경)' if dry_run else '적용'}",
           "- 영어 행도 비교한다. 정보 손실 의심은 보수적인 자동 검토 신호이며 의미 동등성을 보증하지 않는다.",
           "- 타입/기본값 비교는 서식·빈 값 표기만 정규화한다. 발견한 차이는 수정하지 않는다.", "",
           "| 챕터 | 한글 행 | 변경 | 모호 | 짝 없음 | 의도적 차이 | 이미 일치 | 정보 손실 의심 | 전체 변경 |",
           "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for name in sorted({r["file"] for r in records}):
        all_rows = [r for r in records if r["file"] == name]
        rows = [r for r in all_rows if r["korean"]]
        counts = collections.Counter(r["status"] for r in rows)
        nums = [len(rows)] + [counts[s] for s in ["변경", "모호", "짝 없음", "의도적 차이", "일치"]]
        nums += [sum(bool(r["loss"]) and r["status"] == "변경" for r in rows),
                 sum(r["status"] == "변경" for r in all_rows)]
        out.append("| " + " | ".join([name] + list(map(str, nums))) + " |")
    for status in ["변경", "모호", "짝 없음", "의도적 차이"]:
        out += ["", f"## {status}", "", "| 파일:줄 | Key | 기존 설명 (그대로 보존) | 새 원문 설명 | 필수: 이전 → 원문 | OM 글 id | 사유 / 검토 신호 |",
                "| --- | --- | --- | --- | --- | --- | --- |"]
        for r in records:
            if r["status"] != status:
                continue
            fields = [f"{r['file']}:{r['line']}", ", ".join(r["keys"]), r["old"], r.get("new", ""),
                      f"{r['old_required']} → {r.get('required', '')}", ", ".join(r["aids"]),
                      "; ".join([r["reason"]] + r["loss"]).strip("; ")]
            out.append("| " + " | ".join(cell(x) for x in fields) + " |")
    out += ["", "## 정보 손실 의심 (검토 필요)", "",
            "| 파일:줄 | Key | 신호 |", "| --- | --- | --- |"]
    for r in records:
        if r["status"] == "변경" and r["loss"]:
            out.append("| " + " | ".join(cell(x) for x in
                       [f"{r['file']}:{r['line']}", ", ".join(r["keys"]), "; ".join(r["loss"])]) + " |")
    out += ["", "## 타입·기본값 차이 (수정하지 않음)", "",
            "| 파일:줄 | Key | 칸 | 로컬 | OM | OM 글 id |", "| --- | --- | --- | --- | --- | --- |"]
    for r in records:
        for column, local, official, aid in r["differences"]:
            out.append("| " + " | ".join(cell(x) for x in
                       [f"{r['file']}:{r['line']}", ", ".join(r["keys"]), column, local, official, aid]) + " |")
    return "\n".join(out) + "\n"


def main(argv=None, articles=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--file", help="one chapter filename under docs/manual")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--korean-only", action="store_true", help="process only rows with Hangul descriptions")
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT, help="append-only Markdown report path")
    args = parser.parse_args(argv)
    docs = ROOT / "docs/manual"
    files = sorted(docs.glob("[0-9]*.md"))
    if args.file:
        files = [p for p in files if p.name == args.file]
        if not files:
            parser.error("--file must name an existing numbered docs/manual chapter")
    report = args.report.resolve()
    if report == Path(__file__).resolve() or report.is_relative_to(ROOT / "docs") or report in files:
        parser.error("--report must not overwrite source documents")
    if articles is None:
        articles = fetch_bodies()  # once per run; finish fetching before any writes
    records, outputs = analyze(articles, files, korean_only=args.korean_only or not args.dry_run)
    report.parent.mkdir(parents=True, exist_ok=True)
    separator = "\n---\n\n" if report.exists() and report.stat().st_size else ""
    with report.open("a", encoding="utf-8", newline="\n") as stream:
        stream.write(separator + make_report(records, args.dry_run))
    if not args.dry_run:
        for path, (before, after, crlf) in outputs.items():
            if before != after:
                write(path, after, crlf)
    print(f"articles: {len(articles)}  rows: {len(records)}  Korean: {sum(r['korean'] for r in records)}")
    print(dict(collections.Counter(r["status"] for r in records)))
    print(f"report: {report}")
    return records


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
