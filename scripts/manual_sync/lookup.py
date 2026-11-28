"""Look up a MIDAS endpoint and its article-specific documentation offline."""

import argparse
import json
from pathlib import Path
import re
import sys

from index_articles import SELECTORS, variant_pairs

INDEX = Path(__file__).resolve().parents[2] / "docs" / "index"
DISCOVERY_ORDER = {"current": 0, "unlinked": 1, "legacy": 2}
# Git Bash on Windows rewrites a leading-slash argument such as /db/NODE into C:/Program Files/Git/db/NODE
MSYS_PREFIX = re.compile(r"^[A-Za-z]:[/\\].*?[/\\]Git[/\\]", re.I)


def normalized_uri(value):
    uri = MSYS_PREFIX.sub("", value.strip()).lstrip("/").upper()
    if not re.fullmatch(r"[A-Z0-9_-]+(?:/[A-Z0-9_-]+)+", uri):
        raise argparse.ArgumentTypeError("expected an endpoint URI such as /db/NODE")
    return uri


def article_id(value):
    if not re.fullmatch(r"[0-9]+", value):
        raise argparse.ArgumentTypeError("expected a numeric article ID")
    return value


def legacy_differences(article, by_id):
    result = []
    for aid in article.get("legacy_of", []):
        current = by_id[aid]
        diff = {"current_article_id": aid}
        for field in ("methods", "keys"):
            older, newer = set(article[field]), set(current[field])
            diff[field] = {"legacy_only": sorted(older - newer), "current_only": sorted(newer - older)}
        result.append(diff)
    return result


def stated(article, key, value):
    """True when the article uses the selector value outside its Schema enum."""
    return any(item["value"] == value and set(item["sources"]) - {"schema"}
               for item in article.get("variant_evidence", {}).get(key, []))


def lookup(index, uri, selectors, aid=None):
    endpoint = next((record for record in index["endpoints"] if record["endpoint"] == uri), None)
    result = {"endpoint": uri, "endpoint_summary": None, "matches": [],
              "selected_article_id": None, "chunks": []}
    if endpoint is None:
        result["message"] = "Endpoint not found."
        return 1, result
    result["endpoint_summary"] = {key: value for key, value in endpoint.items() if key != "articles"}
    by_id = {article["id"]: article for article in endpoint["articles"]}
    matches = [dict(article) for article in by_id.values()
               if (aid is None or article["id"] == aid) and selectors <= variant_pairs(article)]
    matches.sort(key=lambda a: (DISCOVERY_ORDER[a["status"]], a["id"]))
    for article in matches:
        if article["status"] == "legacy":
            article["legacy_differences"] = legacy_differences(article, by_id)
    result["matches"] = matches
    if not selectors and aid is None:
        return 0, result
    if not matches:
        result["message"] = "No article matched the filters."
        return 1, result
    if len(matches) != 1:
        current = [article for article in matches if article["status"] == "current"]
        if len(current) != 1:
            # a value listed only in another article's Schema enum is weaker evidence than one
            # the article actually uses in its request example or text (PLATEFORCEG, THISBEAMFORCE)
            current = [article for article in matches if article["status"] != "legacy"
                       and all(stated(article, key, value) for key, value in selectors)]
        if len(current) != 1 or not selectors:
            result["message"] = "Several articles match. Add --article-id to select one."
            return 3, result
        matches = current
    result["selected_article_id"] = matches[0]["id"]
    return 0, result


def selected_chunks(path, article):
    ids = {cid for location in article["locations"] for cid in location["chunk_ids"]}
    if not ids:
        return []
    chunks = []
    with path.open(encoding="utf-8") as stream:
        for line in stream:
            if not line.strip():
                continue
            chunk = json.loads(line)
            if chunk["id"] in ids and article["id"] in chunk["articles"] and chunk["source"] != "repo-example":
                chunks.append(chunk)
    return chunks


def rendered_list(values):
    return ", ".join(values) or "(none listed)"


def print_result(result):
    print(f"/{result['endpoint']}")
    summary = result["endpoint_summary"]
    if summary:
        print(f"Methods (non-legacy)  {rendered_list(summary['methods'])}")
        for field, label in (("legacy_methods", "Legacy-only methods"), ("legacy_keys", "Legacy-only keys")):
            if summary[field]:
                print(f"{label}  {rendered_list(summary[field])}")
    if "message" in result:
        print(result["message"])
    for article in result["matches"]:
        selected = " [selected]" if article["id"] == result["selected_article_id"] else ""
        print(f"\n{article['status']}  {article['id']}  {article['title']}{selected}")
        print(f"  {article['url']}  ({article['locale']}, {article['updated_at']})")
        for key, values in article["variants"].items():
            print(f"  {key}  {rendered_list(values)}")
        print(f"  Methods  {rendered_list(article['methods'])}")
        print(f"  Keys  {rendered_list(article['keys'])}")
        for location in article["locations"]:
            print(f"  {location['kind']}  {location['ref']}  ({rendered_list(location['chunk_ids'])})")
        if not article["locations"]:
            print("  No confirmed document location.")
        for diff in article.get("legacy_differences", []):
            print(f"  Compared with current article {diff['current_article_id']}")
            for field in ("methods", "keys"):
                print(f"    {field} only in legacy  {rendered_list(diff[field]['legacy_only'])}")
                print(f"    {field} only in current  {rendered_list(diff[field]['current_only'])}")
    for chunk in result["chunks"]:
        print(f"\n[{chunk['id']}] {chunk['heading']}\n\n{chunk['text']}")


def main(argv=None, *, index_dir=INDEX):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("uri", type=normalized_uri)
    for key in SELECTORS:
        parser.add_argument("--" + key.lower().replace("_", "-"), help=f"exact {key} value")
    parser.add_argument("--article-id", type=article_id, help="numeric Zendesk article ID")
    parser.add_argument("--json", action="store_true", help="emit machine-readable results")
    args = parser.parse_args(argv)
    selectors = {(key, value) for key in SELECTORS if (value := getattr(args, key.lower())) is not None}
    if any(not value.strip() for _, value in selectors):
        parser.error("selector values must be non-empty")
    index = json.loads((index_dir / "endpoints.json").read_text(encoding="utf-8"))
    code, result = lookup(index, args.uri, selectors, args.article_id)
    if result["selected_article_id"]:
        selected = next(a for a in result["matches"] if a["id"] == result["selected_article_id"])
        result["chunks"] = selected_chunks(index_dir / "chunks.jsonl", selected)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print_result(result)
    return code


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
