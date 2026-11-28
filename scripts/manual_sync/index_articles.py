"""Official article metadata and URI summaries for the manual index."""

from collections import defaultdict
import html
import json
from pathlib import Path
import re
from urllib.parse import unquote

from check_coverage import ARTICLE_URI_RE, TOC_ARTICLE_ID, VARIANT_RE, design_catalogs, parse_toc, plain_text
from check_fields import article_keys

SELECTORS = ("TABLE_TYPE", "CURRENT_MODE", "TEXT_TYPE", "DGNCODE")
STATUS_ORDER = {"current": 0, "unlinked": 1, "legacy": 2}
LEGACY_PAIRS = Path(__file__).with_name("legacy_pairs.json")
METHODS_RE = re.compile(r"Active Methods\s*((?:(?:GET|POST|PUT|DELETE)\b\s*,?\s*)+)")
HTML_HEADING = re.compile(r"<h[1-6]\b[^>]*>(.*?)</h[1-6]>", re.I | re.S)
COPY_TEXT = re.compile(r'''data-copy-text=(["'])(.*?)\1''', re.S)


def toc_links(articles, ko_body):
    root = parse_toc(articles[TOC_ARTICLE_ID]["body"]) + parse_toc(ko_body)
    catalogs = design_catalogs(articles, ko_body, include_legacy=True)
    out = defaultdict(list)
    for catalog, rows in [(TOC_ARTICLE_ID, root), *catalogs.items()]:
        for uri, ids in rows or ():
            link = {"catalog_id": catalog, "uri": uri}
            for aid in ids:
                if link not in out[aid]:
                    out[aid].append(link)
    return out, {TOC_ARTICLE_ID, *catalogs}


def selector_schema_values(node):
    if not isinstance(node, dict):
        return
    yield node.get("const")
    yield from node.get("enum", [])
    for group in ("oneOf", "anyOf", "allOf"):
        for child in node.get(group, []):
            yield from selector_schema_values(child)


def schema_selectors(node):
    if isinstance(node, dict):
        properties = node.get("properties", {})
        for key in SELECTORS:
            if key in properties:
                for value in selector_schema_values(properties[key]):
                    if isinstance(value, str):
                        yield key, value
        for child in node.values():
            yield from schema_selectors(child)
    elif isinstance(node, list):
        for child in node:
            yield from schema_selectors(child)


def variant_metadata(body, text):
    evidence = defaultdict(set)
    for key, value in VARIANT_RE.findall(text):
        evidence[key, value].add("source_text")
    headings = list(HTML_HEADING.finditer(body))
    for i, heading in enumerate(headings):
        label = plain_text(heading[1]).strip().casefold()
        if not (label.startswith("request example") or label == "json schema"):
            continue
        end = headings[i + 1].start() if i + 1 < len(headings) else len(body)
        block = body[heading.end():end]
        if label.startswith("request example"):
            for key, value in VARIANT_RE.findall(plain_text(block)):
                evidence[key, value].add("request_example")
            continue
        encoded = [unquote(html.unescape(value)) for _, value in COPY_TEXT.findall(block)]
        visible = plain_text(block)
        for raw in encoded + [visible[visible.find("{"):]]:
            try:
                schema, _ = json.JSONDecoder().raw_decode(raw.lstrip())
            except ValueError:
                continue
            for key, value in schema_selectors(schema):
                evidence[key, value].add("schema")
    variants = defaultdict(list)
    for (key, value), sources in sorted(evidence.items()):
        if value.casefold() != "string":
            variants[key].append({"value": value, "sources": sorted(sources)})
    return {key: [item["value"] for item in values] for key, values in variants.items()}, dict(variants)


def collect(articles, manifest, links, catalogs):
    metadata, by_uri = {}, defaultdict(list)
    for aid, article in sorted(articles.items()):
        if aid in catalogs:
            continue
        body = article.get("body") or ""
        text = plain_text(body)
        uris = {uri.upper() for uri in ARTICLE_URI_RE.findall(text)}
        variants, evidence = variant_metadata(body, text)
        methods = METHODS_RE.search(text)
        url = article["html_url"]
        locale = re.search(r"/hc/([^/]+)/", url)
        metadata[aid] = {
            "id": aid, "locale": article.get("locale") or (locale[1] if locale else ""),
            "title": article["title"], "url": url,
            "updated_at": article.get("updated_at") or manifest.get(aid, {}).get("updated_at", ""),
            "variants": variants, "variant_evidence": evidence,
            "methods": sorted(set(methods[1].replace(",", " ").split())) if methods else [],
            "keys": sorted(article_keys(body)), "toc_linked": bool(links.get(aid)),
            "toc_links": links.get(aid, []),
            "status": "current" if links.get(aid) else "unlinked",
        }
        for uri in sorted(uris):
            by_uri[uri].append(metadata[aid])
    return metadata, by_uri


def variant_pairs(article):
    return {(key, value) for key, values in article["variants"].items() for value in values}


def classify(by_uri):
    reviewed = {pair["legacy"]: pair for pair in json.loads(LEGACY_PAIRS.read_text(encoding="utf-8"))}
    for uri, articles in by_uri.items():
        current = {a["id"]: a for a in articles if a["toc_linked"]}
        classified = []
        for original in articles:
            article = dict(original)
            values = variant_pairs(article)
            pair = reviewed.get(article["id"])
            if article["status"] == "unlinked" and pair and pair["current"] in current:
                successors = [pair["current"]]
                reason = pair["reason"]
            elif article["status"] == "unlinked" and values and article["updated_at"]:
                successors = sorted(aid for aid, other in current.items()
                                    if article["updated_at"] < other["updated_at"]
                                    and values <= variant_pairs(other))
                reason = "An updated, TOC-linked article at this URI contains the same selectors."
            else:
                successors = []
            if successors:
                article.update(status="legacy", legacy_of=successors, legacy_reason=reason)
            classified.append(article)
        by_uri[uri] = sorted(classified, key=lambda a: (STATUS_ORDER[a["status"]], a["id"]))


def summarize(uri, articles, jp_only, tagged):
    non_legacy = [article for article in articles if article["status"] != "legacy"]
    legacy = [article for article in articles if article["status"] == "legacy"]
    methods = {method for article in non_legacy for method in article["methods"]}
    keys = {key for article in non_legacy for key in article["keys"]}
    doc = list(dict.fromkeys(ref for article in articles for ref in article["doc"]))
    name = next((link["uri"] for article in articles for link in article["toc_links"]), None)
    result = {
        "endpoint": uri, "methods": sorted(methods), "jp_only": jp_only, "toc_name": name,
        "articles": articles, "keys": sorted(keys), "doc": doc, "key_count": len(keys),
        "documented": bool(doc) or tagged, "summary_basis": "non_legacy",
        "legacy_methods": sorted({method for article in legacy for method in article["methods"]} - methods),
        "legacy_keys": sorted({key for article in legacy for key in article["keys"]} - keys),
    }
    if not methods:
        result["methods_status"] = "not_listed"
    return result
