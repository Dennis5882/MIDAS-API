"""Offline regression coverage for article summaries, source attribution and lookup."""

import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import build_index
import check_coverage as coverage
import check_fields as fields
import lookup
from test_check_coverage import table


DSPSC = "DESIGN/PSC/AASHTO-LRFD24/DSPSC"
DREULT = "DESIGN/STEEL/KDS-41-30-2022/DREULT"
PSC_TABLE = "DESIGN/PSC/AASHTO-LRFD24/TABLE"


def article(aid, uri, methods="POST", params=None, updated_at="2026-01-01", schema=None):
    heading = '<h3>JSON Schema</h3>' + json.dumps(schema) if schema else ''
    body = (f'<h3>Input URI</h3><p>{{base url}} + {uri}</p><h3>Active Methods</h3>{methods}'
            f'{heading}<h3>Request Examples</h3><pre>{json.dumps(params or {})}</pre>')
    return {"body": body, "title": "Steel Design Result" if uri == DREULT else uri,
            "locale": "en-us", "html_url": f"https://support.midasuser.com/hc/en-us/articles/{aid}",
            "updated_at": updated_at}


def source(aid):
    return f"**원문** [공식 글](https://support.midasuser.com/hc/en-us/articles/{aid})"


class PerArticleIndexTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        fixture = tempfile.TemporaryDirectory()
        cls.addClassCleanup(fixture.cleanup)
        cls.index_dir = Path(fixture.name)
        path = cls.index_dir / "25_fixture.md"
        markdown = [
            f"## 1. {DSPSC}\n\n### Specifications\n\n{source('100')}\n\nDesign code.\n"
            f"\n### 이전 한국어 원문\n\n{source('101')}\n\nEarlier design code.\n",
            f"## 2. {DREULT}\n\nMain request defaults `0`, `0`, `false`.\n"
            "\n<!-- om-fields:201 -->\nOlder defaults `45`, `60`, `true`.\n<!-- /om-fields -->\n",
            f"## 3. {PSC_TABLE}\n\n### Specifications\n\n{source('300')}\n\nPrimary table.\n"
            f"\n### Request Example\n\nCurrent request text.\n"
            f"\n### 추가 원문 — PSC_PRINCIPAL_CS\n\n{source('301')}\n\nLegacy `\"STRUCTURE_GROUP_NAME\"`.\n",
        ]
        root_toc = table(DSPSC, "100") + table(DREULT, "200") + table(PSC_TABLE, "300") + table("POST/TABLE", "402", "403")
        official = {
            coverage.TOC_ARTICLE_ID: {"body": root_toc},
            "100": article("100", DSPSC, "GET, PUT, DELETE", {"DGNCODE": "AASHTO-LRFD24"}, "2026-02-01"),
            "101": article("101", DSPSC, "POST, GET, PUT, DELETE", schema={"properties": {
                "DGNCODE": {"enum": ["AASHTO-LRFD24"]}}}),
            "200": article("200", DREULT, params={"CURRENT_MODE": "STEEL"}, updated_at="2026-02-01"),
            "201": article("201", DREULT, params={"SHOW": True}),
            "300": article("300", PSC_TABLE, params={"TABLE_TYPE": "PSC_PRINCIPAL_CS"}, updated_at="2026-02-01"),
            "301": article("301", PSC_TABLE, params={"TABLE_TYPE": "PSC_PRINCIPAL_CS", "STRUCTURE_GROUP_NAME": "A"}),
            "501": article("501", "POST/TEXT", params={"TEXT_TYPE": "DISPLACEMENT"}),
        }
        for i in range(8):
            aid = str(400 + i)
            mode = "AMBIGUOUS" if i in (2, 3) else "BEAMFORCE" if i == 0 else f"TEST{i}"
            official[aid] = article(aid, "POST/TABLE", "" if i in (2, 3) else "POST", {"TABLE_TYPE": mode})
            markdown.append(f"## {i + 4}. POST/TABLE {mode}\n\n{source(aid)}\n\n"
                            f'{{"TABLE_TYPE": "{mode}"}}\n\n```python\nlocal_example()\n```\n')
        path.write_text("\n".join(markdown), encoding="utf-8")
        with patch.object(build_index, "OUT", str(cls.index_dir)), \
             patch.object(build_index, "fetch_bodies", return_value=official), \
             patch.object(build_index, "fetch_top_toc_ko", return_value=""), \
             patch.object(build_index, "load_manifest", return_value={}), \
             patch.object(fields, "_DOCS", str(cls.index_dir)), \
             patch.object(fields, "mapped_headings", return_value={"200": [(path.name, "2. Steel Design Result")]}), \
             patch("sys.argv", ["build_index.py"]), contextlib.redirect_stdout(io.StringIO()):
            build_index.main()
        cls.index = json.loads((cls.index_dir / "endpoints.json").read_text(encoding="utf-8"))
        cls.endpoints = {rec["endpoint"]: rec for rec in cls.index["endpoints"]}
        cls.chunks = {chunk["id"]: chunk for chunk in map(json.loads, (cls.index_dir / "chunks.jsonl").read_text(
            encoding="utf-8").splitlines())}

    def command(self, *args):
        with contextlib.redirect_stdout(io.StringIO()) as stream:
            code = lookup.main([*args, "--json"], index_dir=self.index_dir)
        return code, json.loads(stream.getvalue())

    def test_legacy_and_unlinked_summary(self):
        self.assertEqual(self.index["schema_version"], 2)
        endpoint = self.endpoints[DSPSC]
        self.assertEqual(endpoint["methods"], ["DELETE", "GET", "PUT"])
        self.assertEqual(endpoint["legacy_methods"], ["POST"])
        self.assertEqual(endpoint["summary_basis"], "non_legacy")
        self.assertNotIn("methods_status", endpoint)
        self.assertEqual([a["status"] for a in endpoint["articles"]], ["current", "legacy"])
        self.assertEqual(endpoint["articles"][1]["legacy_of"], ["100"])
        self.assertEqual(endpoint["articles"][1]["variant_evidence"]["DGNCODE"],
                         [{"value": "AASHTO-LRFD24", "sources": ["schema"]}])
        shared = self.endpoints["POST/TABLE"]
        self.assertEqual(shared["methods"], ["POST"])
        self.assertEqual(len(shared["doc"]), 8)
        self.assertTrue(shared["doc"][0].endswith("ambiguous"))

    def test_same_title_has_separate_body_and_generated_locations(self):
        current, unlinked = self.endpoints[DREULT]["articles"]
        self.assertEqual(current["title"], unlinked["title"])
        self.assertEqual(current["doc"], unlinked["doc"])
        self.assertEqual([a["locations"][0]["kind"] for a in (current, unlinked)], ["section", "om-fields"])
        for aid, defaults in (("200", "`0`, `0`, `false`"), ("201", "`45`, `60`, `true`")):
            code, response = self.command(DREULT, "--article-id", aid)
            self.assertEqual(code, 0)
            self.assertEqual(len(response["chunks"]), 1)
            self.assertEqual(response["chunks"][0]["articles"], [aid])
            self.assertIn(defaults, response["chunks"][0]["text"])

    def test_direct_source_overrides_parent_and_packing_preserves_it(self):
        legacy_chunks = [c for c in self.chunks.values() if '"STRUCTURE_GROUP_NAME"' in c["text"]]
        self.assertEqual([c["articles"] for c in legacy_chunks], [["301"]])
        self.assertNotIn("Current request text", legacy_chunks[0]["text"])
        _, response = self.command(PSC_TABLE, "--table-type", "PSC_PRINCIPAL_CS")
        self.assertEqual(response["selected_article_id"], "300")
        self.assertEqual([c["articles"] for c in response["chunks"]], [["300"]])

    def test_inline_citations_and_source_columns_have_local_scope(self):
        links = {aid: {} for aid in ("111", "222", "333")}
        text = ("- " + source("111") + "\n\n"
                "**Variant** — [원문](https://support.midasuser.com/hc/en-us/articles/222)\n\n"
                "Variant body\n\n**Other variants.**\n\n"
                "| Case | Source |\n| --- | --- |\n"
                "| One | [Article](https://support.midasuser.com/hc/en-us/articles/333) |\n"
                "| Two | [Article](https://support.midasuser.com/hc/en-us/articles/222) |\n")
        blocks = list(build_index.source_blocks(text, links))
        self.assertEqual([ids for _, ids, _ in blocks], [set(), {"222"}, set()])
        self.assertEqual(build_index.direct_sources(blocks[0][0], links), {"111"})
        self.assertNotIn("One", blocks[1][0])
        rows = list(build_index.table_sources(blocks[2][0], links))
        self.assertEqual([ids for _, ids in rows if ids], [{"333"}, {"222"}])

    def test_lookup_normalization_selectors_and_exit_codes(self):
        code, result = self.command("/pOsT/tAbLe", "--table-type", "BEAMFORCE")
        self.assertEqual((code, result["selected_article_id"]), (0, "400"))
        self.assertTrue(result["chunks"])
        self.assertFalse(any("local_example" in chunk["text"] for chunk in result["chunks"]))
        self.assertEqual(self.command("post/table", "--table-type", "beamforce")[0], 1)
        code, result = self.command("post/table", "--table-type", "AMBIGUOUS")
        self.assertEqual((code, result["selected_article_id"]), (3, None))
        self.assertEqual([a["id"] for a in result["matches"]], ["402", "403"])
        for uri, flag, value, aid in ((DREULT, "--current-mode", "STEEL", "200"),
                                      ("POST/TEXT", "--text-type", "DISPLACEMENT", "501"),
                                      (DSPSC, "--dgncode", "AASHTO-LRFD24", "100")):
            code, result = self.command(uri, flag, value)
            self.assertEqual((code, result["selected_article_id"]), (0, aid))
        code, result = self.command(DSPSC)
        self.assertEqual((code, result["selected_article_id"]), (0, None))
        self.assertEqual(result["matches"][1]["legacy_differences"][0]["methods"]["legacy_only"], ["POST"])
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as error:
            self.command(DSPSC, "--article-id", "bad")
        self.assertEqual(error.exception.code, 2)

    def test_schema_only_value_does_not_make_a_selector_ambiguous(self):
        def art(aid, sources):
            return dict(id=aid, status="unlinked", methods=["POST"], keys=[], variants={"TABLE_TYPE": ["PLATEFORCEG"]},
                        variant_evidence={"TABLE_TYPE": [{"value": "PLATEFORCEG", "sources": sources}]})
        index = {"endpoints": [dict(endpoint="POST/TABLE", articles=[
            art("1", ["request_example", "schema"]), art("2", ["schema"])])]}
        code, result = lookup.lookup(index, "POST/TABLE", {("TABLE_TYPE", "PLATEFORCEG")})
        self.assertEqual((code, result["selected_article_id"]), (0, "1"))
        index["endpoints"][0]["articles"][1]["variant_evidence"]["TABLE_TYPE"][0]["sources"] = ["request_example"]
        self.assertEqual(lookup.lookup(index, "POST/TABLE", {("TABLE_TYPE", "PLATEFORCEG")})[0], 3)

    def test_git_bash_path_conversion_is_undone(self):
        self.assertEqual(lookup.normalized_uri("C:/Program Files/Git/post/TABLE"), "POST/TABLE")
        self.assertEqual(lookup.normalized_uri("/db/node"), "DB/NODE")

    def test_korean_toc_and_historical_catalog_link_by_id(self):
        catalog = min(coverage.LEGACY_DESIGN_CATALOGS)
        official = {coverage.TOC_ARTICLE_ID: {"body": ""}, catalog: {"body": table("POST/OLD", "700")}}
        ko = f'<h2>Design Code</h2><a href="/hc/ko/articles/{catalog}">Catalog</a>' + table("POST/KO", "701")
        links, catalogs = build_index.ia.toc_links(official, ko)
        self.assertIn(catalog, catalogs)
        self.assertEqual(links["700"], [{"catalog_id": catalog, "uri": "POST/OLD"}])
        self.assertEqual(links["701"], [{"catalog_id": coverage.TOC_ARTICLE_ID, "uri": "POST/KO"}])


if __name__ == "__main__":
    unittest.main()
