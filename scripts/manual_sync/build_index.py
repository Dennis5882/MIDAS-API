"""Build the machine-readable index and retrieval chunks from docs/manual (no AI, no embeddings).

  docs/index/endpoints.json   one record per official endpoint: methods, article id/url, chapter and
                              section, Key list, JP-only flag
  docs/index/chunks.jsonl     docs/manual cut into retrieval chunks with the same metadata

Both are generated; do not edit by hand. Confirmed article sources are recorded per chunk.

  python build_index.py
"""
import argparse
import collections
import glob
import json
import os
import re
import sys

import build_llms
import check_fields as cf
import index_articles as ia
from check_coverage import fetch_bodies, fetch_top_toc_ko, shared_uri
from common import load_manifest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
OUT = os.path.join(ROOT, "docs", "index")
MAX_CHARS = 3500
FIELD_BLOCK = re.compile(r"<!-- om-fields:(\d+) -->.*?<!-- /om-fields -->", re.S)
SOURCE_LABEL = re.compile(r"^\s*(?:>\s*)?(?:[-*]\s+)?\*\*(?:원문|출처|Source)\b", re.I)
SOURCE_ID = re.compile(r"https://support\.midasuser\.com/hc/(?:en-us|ko)/articles/(\d+)")
INLINE_HEADING = re.compile(r"^\*\*[^*]+\*\*")
INLINE_SOURCE = re.compile(r"\[(?:원문|출처|Source)\]", re.I)
SOURCE_COLUMN = re.compile(r"\|\s*(?:원문|출처|Source)\s*\|\s*$", re.I)


def slug(heading):
    text = re.sub(r"^#+\s*", "", heading).lower().replace("`", "")
    return re.sub(r"\s", "-", re.sub(r"[^\w\- ]", "", text))


_ANCHORS = {}


def anchor(section):
    """GitHub anchor of a section heading, with the -1, -2 suffix of repeated headings."""
    path = section.get("path", "")
    if path not in _ANCHORS:
        out, seen, fenced = {}, {}, False
        try:
            with open(path, encoding="utf-8") as f:
                lines = f.read().splitlines()
        except OSError:
            lines = []
        for n, line in enumerate(lines):
            if line.startswith("```"):
                fenced = not fenced
            elif not fenced and re.match(r"#{1,6} ", line):
                base = slug(line)
                seen[base] = seen.get(base, -1) + 1
                out[n] = f"{base}-{seen[base]}" if seen[base] else base
        _ANCHORS[path] = out
    return _ANCHORS[path].get(section.get("start"), slug(section["heading"]))


TABLE_SEP = re.compile(r"^\|\s*:?-{3,}")


def split_text(lines, limit=MAX_CHARS):
    """Greedy split on blank lines outside code fences. A fenced block larger than twice the limit is
    cut by lines and every piece is re-wrapped in its own fence. A Markdown table larger than the
    limit is cut by rows and every piece repeats the table header."""
    parts, cur, size, fenced, fence_open, header = [], [], 0, False, "", []
    for line in lines:
        if line.startswith("```"):
            fenced = not fenced
            fence_open = line if fenced else ""
        elif fenced and size >= limit * 2:
            parts.append("\n".join(cur + ["```"]).strip("\n"))
            cur, size = [fence_open], 0
        elif not fenced and line.startswith("|"):
            if TABLE_SEP.match(line) and cur and cur[-1].startswith("|"):
                header = [cur[-1], line]
            elif header and size >= limit:
                parts.append("\n".join(cur).strip("\n"))
                cur, size = list(header), sum(len(h) + 1 for h in header)
        elif not fenced:
            header = []
        cur.append(line)
        size += len(line) + 1
        if not fenced and line.strip() == "" and size >= limit:
            parts.append("\n".join(cur).strip("\n"))
            cur, size = [], 0
    if "".join(cur).strip():
        parts.append("\n".join(cur).strip("\n"))
    return parts


# subsection headings that never name an endpoint ("### Request Example"); matched at the start only,
# so an endpoint title such as "/db/SPFC – Response Spectrum Functions" is not mistaken for one
GENERIC = re.compile(r"^(?:Python|예제|HTTP|Specifications|Request|Response|JSON Schema|Input URI|"
                     r"Active Methods|파라미터|Parameters|전체|개요|공통)", re.I)
# content written by this repository, not taken from the official manual
REPO_AUTHORED = re.compile(r"Python|워크플로|Workflow", re.I)


def bare(heading):
    return re.sub(r"^#+\s*(?:\d+(?:\.\d+)*\.?\s*)?", "", heading).strip("` ")


def generic(heading):
    text = bare(heading)
    return bool(GENERIC.match(text) or re.search(r"워크플로|Workflow", text, re.I))


def split_python(text):
    """(official text, repo-authored text). Every ```python block in docs/manual was written by this
    repository (README), so it is moved out together with a label line such as "**Python 예제**"."""
    keep, moved, fenced, py = [], [], False, False
    for line in text.split("\n"):
        if line.startswith("```"):
            if not fenced and line[3:].strip().lower() in ("python", "py"):
                py = True
                while keep and not keep[-1].strip():
                    keep.pop()
                if keep and "python" in keep[-1].lower() and not keep[-1].startswith("#"):
                    moved.append(keep.pop())
            fenced = not fenced
            (moved if py else keep).append(line)
            if not fenced:
                py = False
                keep.append("")
            continue
        (moved if py else keep).append(line)
    return "\n".join(keep).strip(), "\n".join(moved).strip()


def trivial(text):
    """Nothing left once headings, rules and generated markers are removed."""
    return not re.sub(r"<!--.*?-->|^-{3,}\s*$|^#+ .*$", "", text, flags=re.M).strip()


def pack(raw, locations, limit=MAX_CHARS):
    """Join consecutive pieces of the same group (endpoint section + source) up to the limit, so an
    endpoint's URI, methods, table and request example travel together instead of as 100-char scraps."""
    out = []
    for p in raw:
        last = out[-1] if out else None
        if (last and last["_group"] == p["_group"] and last["articles"] == p["articles"]
                and last["candidate_articles"] == p["candidate_articles"] and last["_refs"] == p["_refs"]
                and len(last["text"]) + len(p["text"]) + 2 <= limit):
            last["text"] += "\n\n" + p["text"]
            last["endpoints"] = sorted(set(last["endpoints"]) | set(p["endpoints"]))
            last["jp_only"] = last["jp_only"] or p["jp_only"]
            if last["heading"] != p["heading"]:
                last["heading"] = p["_host_trail"]
        else:
            out.append(dict(p))
    counter, final = collections.Counter(), []
    for c in out:
        n = counter[(c["file"], c["_slug"])]
        counter[(c["file"], c["_slug"])] += 1
        cid = f"{c['file'][:-3]}:{c['_slug']}:{n}"
        record = {"id": cid, **{k: c[k] for k in FIELDS}}
        if c["candidate_articles"]:
            record["candidate_articles"] = c["candidate_articles"]
        if c["source"] != "repo-example":
            for aid in c["articles"]:
                for ref, kind in sorted(c["_refs"]):
                    locations[aid][ref, kind].append(cid)
        final.append(record)
    return final


FIELDS = ("file", "heading", "anchor", "source", "endpoints", "articles", "jp_only", "text")


def ancestry(sections):
    """{(path, start): [ancestor sections, outermost first]} using heading levels."""
    out = {}
    for path in {s["path"] for s in sections}:
        stack = []
        for s in sorted((x for x in sections if x["path"] == path), key=lambda x: x["start"]):
            while stack and stack[-1]["level"] >= s["level"]:
                stack.pop()
            out[(path, s["start"])] = list(stack)
            stack.append(s)
    return out


def section_key(section):
    return section["path"], section["start"]


def direct_sources(text, metadata):
    return {aid for line in text.splitlines() if SOURCE_LABEL.match(line)
            for aid in SOURCE_ID.findall(line) if aid in metadata}


def source_blocks(text, metadata):
    """Yield text partitions with their local source citations and optional heading."""
    lines = text.splitlines()
    start, ids, heading, fenced = 0, set(), None, False
    for n, line in enumerate(lines):
        if line.startswith("```"):
            fenced = not fenced
        match = INLINE_HEADING.match(line)
        if fenced or match is None or SOURCE_LABEL.match(line):
            continue
        local = set(SOURCE_ID.findall(line)) & metadata.keys() if INLINE_SOURCE.search(line) else set()
        if local or ids:
            yield "\n".join(lines[start:n]), ids, heading
            start, ids, heading = n, local, match[0].strip("*") if local else None
    yield "\n".join(lines[start:]), ids, heading


def table_sources(text, metadata):
    """Keep a source-named column on the rows it supports, along with the table header."""
    lines = text.splitlines()
    start = n = 0
    while n + 1 < len(lines):
        if not (lines[n].startswith("|") and SOURCE_COLUMN.search(lines[n]) and TABLE_SEP.match(lines[n + 1])):
            n += 1
            continue
        header = lines[n:n + 2]
        end = n + 2
        while end < len(lines) and lines[end].startswith("|"):
            end += 1
        rows = [(line, set(SOURCE_ID.findall(line.rstrip("| ").rsplit("|", 1)[-1])) & metadata.keys())
                for line in lines[n + 2:end]]
        if any(ids for _, ids in rows):
            yield "\n".join(lines[start:n]), set()
            for line, ids in rows:
                yield "\n".join([*header, line]), ids
            start = end
        n = end
    yield "\n".join(lines[start:]), set()


def infer_sources(text, endpoints, by_uri):
    variants = set(ia.VARIANT_RE.findall(text))
    return {a["id"] for uri in endpoints for a in by_uri.get(uri, ())
            if not shared_uri(uri) or variants & ia.variant_pairs(a)}


def mapped_sources(sections, mapping, children, metadata):
    matches_by_section = collections.defaultdict(list)
    for aid in mapping.keys() & metadata.keys():
        for filename, label in mapping[aid]:
            for section in cf.mapped_sections(aid, sections, {aid: [(filename, label)]}):
                matches_by_section[section_key(section)].append((aid, label))
    sources = collections.defaultdict(set)
    for key, matches in matches_by_section.items():
        for aid, label in matches:
            qualifier = re.search(r"\(([^()]+)\)\s*$", label)
            children_with_label = [child for child in children[key]
                                   if qualifier and qualifier[1].casefold() in child["heading"].casefold()]
            target = section_key(children_with_label[0]) if len(matches) > 1 and len(children_with_label) == 1 else key
            sources[target].add(aid)
    return sources


def document_chunks(sections, mapping, metadata, by_uri, jp_endpoints):
    tree = ancestry(sections)
    children = collections.defaultdict(list)
    for section in sections:
        parents = tree[section_key(section)]
        if parents:
            children[section_key(parents[-1])].append(section)
    own, extras, direct = {}, {}, {}
    for section in sections:
        key = section_key(section)
        lines = section["text"].splitlines()
        if children[key]:
            lines = lines[:children[key][0]["start"] - section["start"]]
        text = "\n".join(lines).strip()
        extras[key] = [(match[1], match[0]) for match in FIELD_BLOCK.finditer(text)]
        own[key] = FIELD_BLOCK.sub("", text).strip()
        direct[key] = direct_sources(own[key], metadata)
    mapped = mapped_sources(sections, mapping, children, metadata)
    raw, candidates = [], collections.defaultdict(set)
    for s in sections:
        if s["level"] > 3 or re.search(r"Table of Contents|목차", s["heading"]):
            continue
        key = section_key(s)
        parents = tree[key]
        text = own[key]
        chain = parents + [s]
        eps = sorted(set().union(*(x["endpoints"] for x in chain)))
        ids = direct[key] or next((direct[section_key(x)] for x in reversed(parents)
                                   if direct[section_key(x)]), set())
        if not ids:
            for ancestor in reversed(chain):
                akey = section_key(ancestor)
                specs = [direct[section_key(child)] for child in children[akey]
                         if bare(child["heading"]).casefold().startswith("specifications")]
                ids = set().union(*specs) or mapped[akey]
                if ids:
                    break
        possible = set()
        if not ids and eps and not any("공통" in x["heading"] for x in chain):
            private_text = "\n".join([text, *(own[section_key(x)] for x in parents),
                                      *(own[section_key(x)] for host in chain for x in children[section_key(host)]
                                        if generic(x["heading"]) and not direct[section_key(x)])])
            possible = infer_sources(private_text, eps, by_uri)
            if len(possible) == 1:
                ids, possible = possible, set()
        trail = " > ".join(re.sub(r"^#+\s*", "", x["heading"]) for x in chain)
        # the group a piece is packed into: the outermost section of the chain that names an endpoint,
        # else the level-2 section
        host = next((x for x in chain if x["level"] >= 2 and x["endpoints"]), None) \
            or ([x for x in chain if x["level"] == 2] or chain)[0]
        host_chain = chain[: chain.index(host) + 1]
        host_slug = "/".join(slug(x["heading"]) for x in host_chain)
        host_trail = " > ".join(re.sub(r"^#+\s*", "", x["heading"]) for x in host_chain)
        ref_section = s if (direct[key] or mapped[key]) and not generic(s["heading"]) else host
        ref = f"{s['file']}#{anchor(ref_section)}"
        kind = "supplement" if ref_section is not host else "section"
        links = {(ref, kind)}
        for aid in possible:
            candidates[aid].add(ref)
        source = "repo-example" if any(REPO_AUTHORED.search(bare(x["heading"])) for x in chain) else "om"
        if source == "repo-example":
            pieces = [(host_slug + "/example", trail, ids, possible, source, text, links)]
        else:
            pieces = []
            for block, local, label in source_blocks(text, metadata):
                official, python = split_python(block)
                for fragment, row_ids in table_sources(official, metadata):
                    own_ids = row_ids or local
                    block_ref = {(f"{s['file']}#{anchor(s)}", "supplement")} if own_ids else links
                    title = f"{trail} > {label}" if label else trail
                    pieces.append((host_slug, title, own_ids or ids, set() if own_ids else possible,
                                   "om", fragment, block_ref))
                pieces.append((host_slug + "/example", trail, local or ids, set() if local else possible,
                               "repo-example", python, links))
        for aid, blk in extras[key]:
            pieces.append((f"{host_slug}/om-fields-{aid}", f"{host_trail} > OM 원문 추가 필드",
                           {aid}, set(), "om-verbatim", blk, {(f"{s['file']}#{anchor(host)}", "om-fields")}))
        for pslug, ptrail, pids, pending, psource, ptext, refs in pieces:
            for part in split_text(ptext.split("\n")):
                if trivial(part):
                    continue
                raw.append({
                    "_slug": pslug, "_group": (s["file"], pslug), "_host_trail": host_trail,
                    "_refs": refs,
                    "file": s["file"], "heading": ptrail, "anchor": anchor(host), "source": psource,
                    "endpoints": eps, "articles": sorted(pids), "candidate_articles": sorted(pending),
                    "jp_only": any(e in jp_endpoints for e in eps), "text": part,
                })
    locations = collections.defaultdict(lambda: collections.defaultdict(list))
    return pack(raw, locations), locations, candidates


def main():
    argparse.ArgumentParser().parse_args()
    os.makedirs(OUT, exist_ok=True)
    articles = fetch_bodies()
    manifest = load_manifest()
    with open(os.path.join(ROOT, "docs", "manual", "jp_only.json"), encoding="utf-8") as stream:
        jp = json.load(stream)
    jp_endpoints = {x["uri"].lstrip("/").upper() for x in jp["exclude"] if x["type"] == "endpoint"}
    sections, _ = cf.load_sections()
    links, catalogs = ia.toc_links(articles, fetch_top_toc_ko())
    metadata, by_uri = ia.collect(articles, manifest, links, catalogs)
    ia.classify(by_uri)
    chunks, locations, candidates = document_chunks(sections, cf.mapped_headings(), metadata, by_uri, jp_endpoints)
    with open(os.path.join(OUT, "chunks.jsonl"), "w", encoding="utf-8", newline="\n") as f:
        for c in chunks:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")

    # an endpoint is documented when docs/manual has a section for it (PSC is listed but on hold)
    tagged = {e for c in chunks if c["source"] != "repo-example" for e in c["endpoints"]}
    records = []
    for uri, entries in sorted(by_uri.items()):
        for article in entries:
            aid = article["id"]
            article["locations"] = [{"ref": ref, "kind": kind, "chunk_ids": ids}
                                    for (ref, kind), ids in sorted(locations[aid].items())]
            article["doc"] = sorted({loc["ref"] for loc in article["locations"]})
            pending = candidates[aid] - set(article["doc"])
            if pending:
                article["doc_candidates"] = sorted(pending)
        records.append(ia.summarize(uri, entries, uri in jp_endpoints, uri in tagged))
    with open(os.path.join(OUT, "endpoints.json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump({"_note": "Generated by scripts/manual_sync/build_index.py from the official online manual and docs/manual. Do not edit.",
                   "schema_version": 2, "endpoints": records}, f, ensure_ascii=False, indent=1)
        f.write("\n")
    sizes = sorted(len(c["text"]) for c in chunks)
    by_source = collections.Counter(c["source"] for c in chunks)
    print(f"endpoints: {len(records)} (documented {sum(r['documented'] for r in records)})  "
          f"chunks: {len(chunks)} {dict(by_source)}  chunk chars median {(sizes or [0])[len(sizes)//2]} "
          f"max {max(sizes, default=0)}")
    # llms.txt reads the files just written, so its figures match the index. A run into another
    # folder (tests) keeps its llms.txt there instead of touching the repository root.
    default = os.path.abspath(OUT) == os.path.abspath(build_llms.INDEX_DIR)
    build_llms.main(index_dir=OUT, out=build_llms.OUT if default else os.path.join(OUT, "llms.txt"))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
