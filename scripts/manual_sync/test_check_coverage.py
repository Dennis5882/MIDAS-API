"""Offline regression tests for bridge catalogs and shared endpoint matching."""
import contextlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

import build_index
import check_coverage as coverage
import check_fields as fields


def official(uri, key=None, value=None):
    variant = f'<p>"{key}": "{value}"</p>' if key else ""
    return f"<h3>Input URI</h3><p>{{base url}} + {uri}</p>{variant}"


def table(uri, *ids):
    links = "".join(f'<a href="/hc/en-us/articles/{aid}">Article</a>' for aid in ids)
    return f"<table><tr><td>1</td><td>{uri}</td><td>{links}</td></tr></table>"


def section(heading, uri, description, *ids):
    return dict(file="28_test.md", heading=heading, endpoints={uri}, ids=set(ids), text=description)


class CoverageTests(unittest.TestCase):
    def test_rating_uri_in_input_heading_and_catalog(self):
        uri = "RATING/PSC/AASHTO-LRFR19/TABLE"
        self.assertEqual(coverage.ARTICLE_URI_RE.findall(coverage.plain_text(official(uri))), [uri])
        self.assertEqual(coverage.ENDPOINT_RE.findall("## " + uri), [uri])
        self.assertEqual(coverage.parse_toc(table(uri, "800")), [(uri, ["800"])])

    def test_union_of_top_locale_links_skips_legacy_catalogs_and_later_sections(self):
        def links(*ids):
            return "".join(f'<p><a href="/hc/ko/articles/{aid}-title">text</a></p>' for aid in ids)

        en = "<h2>DB</h2><h3>Design</h3>" + links("700") + "<h2>Design</h2>" + links("801")
        ko = ("<h2><b>Design Code</b></h2>" + links("801", "802", "57711427405209") +
              '<a href="https://other.example/hc/ko/articles/804">External</a>' +
              "<h2>VIEW</h2>" + links("803"))
        articles = {
            coverage.TOC_ARTICLE_ID: {"body": en},
            "801": {"body": table("DESIGN/RC/DRC", "901")},
            "802": {"body": table("RATING/PSC/DSRPSC", "902")},
        }
        with patch.object(coverage, "fetch_top_toc_ko", return_value=ko) as fetch:
            catalogs = coverage.design_catalogs(articles)
        fetch.assert_called_once_with()
        self.assertEqual(catalogs, {"801": [("DESIGN/RC/DRC", ["901"])],
                                    "802": [("RATING/PSC/DSRPSC", ["902"])]})

    def test_archived_top_without_catalog_does_not_fetch_newer_locale(self):
        articles = {coverage.TOC_ARTICLE_ID: {"body": table("/db/X", "900")}}
        with patch.object(coverage, "fetch_top_toc_ko") as fetch:
            self.assertEqual(coverage.design_catalogs(articles, ko_body=""), {})
        fetch.assert_not_called()

    def test_catalog_linked_only_from_ko_top_is_found(self):
        articles = {coverage.TOC_ARTICLE_ID: {"body": "<h2>DB</h2>"},
                    "801": {"body": table("DESIGN/RC/DRC", "901")}}
        ko = '<h2>Design</h2><p><a href="/hc/ko/articles/801">KDS</a></p>'
        with patch.object(coverage, "fetch_top_toc_ko", return_value=ko) as fetch:
            self.assertEqual(coverage.design_catalogs(articles), {"801": [("DESIGN/RC/DRC", ["901"])]})
        fetch.assert_called_once_with()

    def test_catalog_duplicate_uris_preserve_ids_and_find_invalid_links(self):
        uri = "RATING/PSC/AASHTO-LRFR19/TABLE"
        articles = {coverage.TOC_ARTICLE_ID: {"body": ""},
                    "900": {"body": official(uri)},
                    "901": {"body": official("RATING/PSC/AASHTO-LRFR19/OTHER")}}
        catalogs = {"800": [(uri, ["900"]), (uri, ["901"]), (uri, ["902"])],
                    "801": None}
        catalogs["802"] = [("DESIGN/RC/DRC", ["903"])]
        articles["903"] = {"body": official("DESIGN/RC/DRC")}
        sections = {"RATING/PSC/AASHTO-LRFR19/EXTRA": {"30_test.md"},
                    "RATING/PSC/OLDER/EXTRA": {"30_test.md"},
                    "DESIGN/RC/KDS-41-20-2022": {"26_test.md"},
                    "DESIGN/RC/DRC": {"28_test.md"}}
        count, toc_only, docs_only, mismatch = coverage.check_toc(articles, sections, catalogs)
        self.assertEqual(count, 2)
        self.assertEqual(toc_only[0]["articles"], ["900", "901", "902"])
        self.assertEqual([entry["key"] for entry in docs_only], ["RATING/PSC/AASHTO-LRFR19/EXTRA"])
        self.assertEqual({entry["key"] for entry in mismatch}, {"catalog@801", uri+"@901", uri+"@902"})

    def test_nonshared_uri_cannot_be_credited_via_generic_table_type(self):
        uri = "DESIGN/RC/AASHTO-LRFD24/BC-TABLE"
        articles = {"900": {"body": official(uri, "TABLE_TYPE", "MEMB"), "title": "RC"}}
        docs = section("## Other", "POST/TABLE", '"TABLE_TYPE": "MEMB"')
        with patch.object(fields, "load_sections", return_value=([docs], {})):
            findings = coverage.check_articles(articles, {"POST/TABLE": {"18_test.md"}}, docs["text"])
        self.assertEqual([finding["key"] for finding in findings], ["900"])

    def test_shared_uri_fallback_uses_family_and_discriminator(self):
        uri = "DESIGN/PSC/KDS-24-14-21-2021/TABLE"
        here = section("## KDS", uri, '"TABLE_TYPE": "PSC_FLEXURE"')
        there = section("## LRFD", "DESIGN/PSC/AASHTO-LRFD24/TABLE", here["text"])
        other = section("## Other", uri, '"TABLE_TYPE": "PSC_SHEAR"')
        text = coverage.plain_text(official(uri, "TABLE_TYPE", "PSC_FLEXURE"))
        self.assertEqual(fields.covering("900", text, [there, other, here], {})[0], [here])

    def test_article_link_wins_over_an_identical_variant(self):
        uri = "RATING/PSC/AASHTO-LRFR19/TABLE"
        direct = section("## Linked", uri, '"TABLE_TYPE": "PSC_FLEXURE"', "900")
        other = section("## Other source", uri, direct["text"], "901")
        text = coverage.plain_text(official(uri, "TABLE_TYPE", "PSC_FLEXURE"))
        self.assertEqual(fields.covering("900", text, [other, direct], {})[0], [direct])

    def test_an_unlinked_twin_does_not_borrow_an_attributed_section(self):
        uri = "DESIGN/PSC/AASHTO-LRFD24/TABLE"
        source = section("## Cited", uri, '"TABLE_TYPE": "PSC_PRINCIPAL_CS"', "900")
        child = section("### Request", uri, source["text"])
        child["scope_ids"] = source["ids"]
        text = coverage.plain_text(official(uri, "TABLE_TYPE", "PSC_PRINCIPAL_CS"))
        self.assertEqual(fields.covering("901", text, [source, child], {})[0], [])
        with patch.object(fields, "load_sections", return_value=([source, child], {})):
            findings = coverage.check_articles({"901": {"body": text, "title": "Unlinked"}},
                                               {uri: {source["file"]}}, source["text"])
        self.assertEqual([finding["key"] for finding in findings], ["901"])

    def test_legacy_design_force_alias_is_specific_to_its_table_type(self):
        design = "DESIGN/RC/KDS-41-20-2022/TABLE"
        legacy = section("## Beam Forces", design, '"TABLE_TYPE": "BEAMDESIGNFORCES"')
        unrelated = section("## Material", design, '"TABLE_TYPE": "MATERIAL"')
        t = lambda value: coverage.plain_text(official("POST/TABLE", "TABLE_TYPE", value))
        self.assertEqual(fields.covering("900", t("BEAMDESIGNFORCES"), [legacy], {})[0], [legacy])
        self.assertEqual(fields.covering("900", t("MATERIAL"), [unrelated], {})[0], [])

    def test_shared_code_selector_needs_its_own_design_code(self):
        uri = "DESIGN/RC/DRC"
        kds = section("## Old RC", uri, '"DGNCODE": "KDS 41 20 : 2022"')
        lrfd = section("## Bridge RC", uri, '"DGNCODE": "AASHTO-LRFD24"')
        body = official(uri, "DGNCODE", "AASHTO-LRFD24")
        text = coverage.plain_text(body)
        self.assertEqual(fields.covering("900", text, [kds], {})[0], [])
        self.assertEqual(fields.covering("900", text, [kds, lrfd], {})[0], [lrfd])
        with patch.object(fields, "load_sections", return_value=([kds], {})):
            self.assertEqual(len(coverage.check_articles({"900": {"body": body, "title": "New DRC"}},
                                                         {uri: {kds["file"]}}, kds["text"])), 1)

    def test_schema_keyword_is_not_a_missing_request_key(self):
        body = '<div>{"propertyNames":{"const":"1"},"properties":{"DGNCODE":{"type":"string"}}}</div>'
        self.assertEqual(fields.article_keys(body), {"DGNCODE": "json"})

    def test_index_keeps_document_locations_per_selector_source(self):
        uri = "DESIGN/RC/DRC"
        kds = section("## 0. Existing RC", uri, 'Existing RC code: "KDS 41 20 : 2022"', "900")
        kds.update(path="26_test.md", file="26_test.md", level=2, start=0, end=2)
        kds["text"] += '\n**Source** [original](https://support.midasuser.com/hc/en-us/articles/900)'
        lrfd = section("## 0. Bridge RC", uri, 'Bridge RC code: "AASHTO-LRFD24"', "901")
        lrfd.update(path="28_test.md", level=2, start=0, end=2)
        lrfd["text"] += '\n**Source** [original](https://support.midasuser.com/hc/en-us/articles/901)'
        articles = {coverage.TOC_ARTICLE_ID: {"body": ""}}
        for aid, code in (("900", "KDS 41 20 : 2022"), ("901", "AASHTO-LRFD24"), ("902", "KDS 24 14 21 : 2021")):
            articles[aid] = dict(title=code, html_url=f"/hc/en-us/articles/{aid}",
                                 body=official(uri, "DGNCODE", code))
        with tempfile.TemporaryDirectory() as folder, \
             patch.object(build_index, "OUT", folder), \
             patch.object(build_index, "fetch_bodies", return_value=articles), \
             patch.object(build_index, "load_manifest", return_value={}), \
             patch.object(build_index, "fetch_top_toc_ko", return_value=""), \
             patch.object(fields, "load_sections", return_value=([kds, lrfd], {})), \
             patch.object(fields, "mapped_headings", return_value={}), \
             patch.object(sys, "argv", ["build_index.py"]), \
             contextlib.redirect_stdout(io.StringIO()):
            build_index.main()
            with (Path(folder) / "endpoints.json").open(encoding="utf-8") as stream:
                record = json.load(stream)["endpoints"][0]
            self.assertEqual({x["id"]: x["doc"] for x in record["articles"]},
                             {"900": ["26_test.md#0-existing-rc"],
                              "901": ["28_test.md#0-bridge-rc"], "902": []})


if __name__ == "__main__":
    unittest.main()
