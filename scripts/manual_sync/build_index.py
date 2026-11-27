"""Build the machine-readable index and retrieval chunks from docs/manual (no AI, no embeddings).

  docs/index/endpoints.json   one record per official endpoint: methods, article id/url, chapter and
                              section, Key list, JP-only flag
  docs/index/chunks.jsonl     docs/manual cut into retrieval chunks with the same metadata

Both are generated; do not edit by hand. Every record points back to its official article.

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
from check_coverage import CODE_SELECTORS, TOC_ARTICLE_ID, design_catalogs, fetch_bodies, parse_toc, plain_text
from common import load_manifest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
OUT = os.path.join(ROOT, "docs", "index")
MAX_CHARS = 3500
FIELD_BLOCK = re.compile(r"<!-- om-fields:(\d+) -->.*?<!-- /om-fields -->", re.S)
METHODS_RE = re.compile(r"Active Methods\s*((?:(?:GET|POST|PUT|DELETE)\s*,?\s*)+)")


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


def pack(raw, limit=MAX_CHARS):
    """Join consecutive pieces of the same group (endpoint section + source) up to the limit, so an
    endpoint's URI, methods, table and request example travel together instead of as 100-char scraps."""
    out = []
    for p in raw:
        last = out[-1] if out else None
        if last and last["_group"] == p["_group"] and len(last["text"]) + len(p["text"]) + 2 <= limit:
            last["text"] += "\n\n" + p["text"]
            last["articles"] = sorted(set(last["articles"]) | set(p["articles"]))
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
        final.append({"id": f"{c['file'][:-3]}:{c['_slug']}:{n}", **{k: c[k] for k in FIELDS}})
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


def main():
    argparse.ArgumentParser().parse_args()
    os.makedirs(OUT, exist_ok=True)
    articles = fetch_bodies()
    manifest = load_manifest()
    with open(os.path.join(ROOT, "docs", "manual", "jp_only.json"), encoding="utf-8") as stream:
        jp = json.load(stream)
    jp_endpoints = {x["uri"].lstrip("/").upper() for x in jp["exclude"] if x["type"] == "endpoint"}
    sections, _ = cf.load_sections()
    mapping = cf.mapped_headings()
    toc_rows = parse_toc(articles[TOC_ARTICLE_ID]["body"])
    toc_rows += [row for rows in design_catalogs(articles).values() for row in rows or []]
    toc_ids = {i: ep for ep, ids in toc_rows for i in ids}

    records = collections.OrderedDict()
    linked = collections.defaultdict(set)  # section -> articles that cover it (links, article_map, URI match)
    selector_docs = {}
    for aid, art in sorted(articles.items()):
        if aid == TOC_ARTICLE_ID:
            continue
        text = plain_text(art.get("body"))
        found, uris = cf.covering(aid, text, sections, mapping)
        for sec in found:
            linked[(sec['path'], sec['start'])].add(aid)
        if not uris:
            continue
        keys = sorted(cf.article_keys(art.get("body")))
        methods = METHODS_RE.search(text)
        # several articles can share an endpoint (one per country code etc.): merge what each adds
        doc = {f"{s['file']}#{anchor(s)}" for s in found if not generic(s["heading"])}
        meths = set(re.findall(r"GET|POST|PUT|DELETE", methods.group(1))) if methods else set()
        for uri in uris:
            rec = records.setdefault(uri, {
                "endpoint": uri, "methods": set(), "jp_only": uri in jp_endpoints, "toc_name": None,
                "articles": [], "keys": set(), "doc": set(),
            })
            rec["methods"] |= meths
            rec["doc"] |= doc
            rec["toc_name"] = rec["toc_name"] or toc_ids.get(aid)
            if uri in CODE_SELECTORS:
                selector_docs[uri, aid] = sorted(doc)
            rec["articles"].append({
                "id": aid, "title": art["title"], "url": art["html_url"],
                "updated_at": manifest.get(aid, {}).get("updated_at", ""),
            })
            rec["keys"] |= set(keys)
    raw, tree = [], ancestry(sections)
    for s in sections:
        if s["level"] > 3 or re.search(r"Table of Contents|목차", s["heading"]):
            continue
        body = s["text"].split("\n")
        # a level-2 section that has level-3 children: keep only its own lead text here
        children = [t for t in sections if t["file"] == s["file"] and t["level"] > s["level"] and s["start"] < t["start"] < s["end"]]
        if children:
            body = body[: children[0]["start"] - s["start"]]
        text = "\n".join(body).strip()
        # generated "OM 원문 추가 필드" blocks become chunks of their own, with their own article id
        extra = [(m.group(1), m.group(0)) for m in FIELD_BLOCK.finditer(text)]
        text = FIELD_BLOCK.sub("", text).strip()
        chain = tree[(s["path"], s["start"])] + [s]
        ids = sorted(set().union(*(x["ids"] | linked[(x["path"], x["start"])] for x in chain)))
        eps = sorted(set().union(*(x["endpoints"] for x in chain)))
        if any("공통" in x["heading"] for x in chain):  # chapter-wide parameter tables apply to every article of the file
            ids = sorted(set(ids) | {a for (pa, _), v in linked.items() if pa == s["path"] for a in v})
        trail = " > ".join(re.sub(r"^#+\s*", "", x["heading"]) for x in chain)
        # the group a piece is packed into: the outermost section of the chain that names an endpoint,
        # else the level-2 section
        host = next((x for x in chain if x["level"] >= 2 and x["endpoints"]), None) \
            or ([x for x in chain if x["level"] == 2] or chain)[0]
        host_chain = chain[: chain.index(host) + 1]
        host_slug = "/".join(slug(x["heading"]) for x in host_chain)
        host_trail = " > ".join(re.sub(r"^#+\s*", "", x["heading"]) for x in host_chain)
        source = "repo-example" if any(REPO_AUTHORED.search(bare(x["heading"])) for x in chain) else "om"
        if source == "repo-example":
            pieces = [(host_slug + "/example", trail, host_trail, ids, source, text)]
        else:
            official, python = split_python(text)
            pieces = [(host_slug, trail, host_trail, ids, "om", official),
                      (host_slug + "/example", trail, host_trail, ids, "repo-example", python)]
        for aid, blk in extra:
            pieces.append((f"{host_slug}/om-fields-{aid}", f"{host_trail} > OM 원문 추가 필드", host_trail,
                           sorted(set(ids) | {aid}), "om-verbatim", blk))
        for pslug, ptrail, htrail, pids, psource, ptext in pieces:
            for part in split_text(ptext.split("\n")):
                if trivial(part):
                    continue
                raw.append({
                    "_slug": pslug, "_group": (s["file"], pslug), "_host_trail": htrail,
                    "file": s["file"], "heading": ptrail, "anchor": anchor(host), "source": psource,
                    "endpoints": eps, "articles": pids, "jp_only": any(e in jp_endpoints for e in eps), "text": part,
                })
    chunks = pack(raw)
    with open(os.path.join(OUT, "chunks.jsonl"), "w", encoding="utf-8", newline="\n") as f:
        for c in chunks:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")

    # an endpoint is documented when docs/manual has a section for it (PSC is listed but on hold)
    tagged = {e for c in chunks if c["source"] != "repo-example" for e in c["endpoints"]}
    for rec in records.values():
        rec["methods"] = sorted(rec["methods"])
        rec["doc"] = sorted(rec["doc"])[:6]
        if rec["endpoint"] in CODE_SELECTORS and len(rec["articles"]) > 1:
            # A selector can have several design-code articles, each with its own
            # documentation (or none yet). Keep those locations separate.
            for article in rec["articles"]:
                article["doc"] = selector_docs[rec["endpoint"], article["id"]]
        rec["keys"] = sorted(rec["keys"])
        rec["key_count"] = len(rec["keys"])
        rec["documented"] = bool(rec["doc"]) or rec["endpoint"] in tagged
    with open(os.path.join(OUT, "endpoints.json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump({"_note": "Generated by scripts/manual_sync/build_index.py from the official online manual and docs/manual. Do not edit.",
                   "endpoints": list(records.values())}, f, ensure_ascii=False, indent=1)
        f.write("\n")
    sizes = sorted(len(c["text"]) for c in chunks)
    by_source = collections.Counter(c["source"] for c in chunks)
    print(f"endpoints: {len(records)} (documented {sum(r['documented'] for r in records.values())})  "
          f"chunks: {len(chunks)} {dict(by_source)}  chunk chars median {sizes[len(sizes)//2]} max {sizes[-1]}")
    # llms.txt reads the files just written, so its figures match the index. A run into another
    # folder (tests) keeps its llms.txt there instead of touching the repository root.
    default = os.path.abspath(OUT) == os.path.abspath(build_llms.INDEX_DIR)
    build_llms.main(index_dir=OUT, out=build_llms.OUT if default else os.path.join(OUT, "llms.txt"))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
