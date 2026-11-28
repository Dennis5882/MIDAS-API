"""Offline fixtures for the per-article Specifications and Response HEAD audit."""

import json
from pathlib import Path
import tempfile
import unittest

from build_index import slug
from check_specs import Sources, analyze, compare, hold_key, load_holds
from spec_source import load_json


def specs(*rows):
    header = ("No.", "Description", "Key", "Value Type", "Default", "Required")
    return "<h3>Specifications</h3><table>" + "".join(
        "<tr>" + "".join(f"<td>{cell}</td>" for cell in row) + "</tr>" for row in (header, *rows)
    ) + "</table>"


def article(body):
    return {"body": body, "locale": "en-us", "title": "Steel Design Result"}


def examples(heading, cases):
    return f"<h3>{heading}</h3>" + "".join(
        f'<p class="btn_dropdown">{label}</p><pre>{json.dumps(payload)}</pre>' for label, payload in cases)


def chunk(aid, file, section, text, *, verbatim=False):
    key = slug(section)
    return {"file": file, "id": f"{aid}-chunk", "anchor": key, "articles": [aid], "text": text,
            "source": "om-verbatim" if verbatim else "om"}


def catalog(*entries):
    return Sources({"endpoints": [{"articles": [
        {"id": entry["articles"][0], "variants": variants,
         "locations": [{"ref": f"{entry['file']}#{entry['anchor']}", "chunk_ids": [entry["id"]]}]}
        for entry, variants in entries]}]}, [entry for entry, _ in entries])


class CheckSpecsTests(unittest.TestCase):
    def run_fixture(self, name, md, articles, sources):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / name
            path.write_text(md, encoding="utf-8")
            return analyze([path], articles, sources, {})[0]

    def test_scalar_formatting_and_type_case_only(self):
        for field, local, official in (("default", '"3D"', '3D'), ("default", '–', '-'),
                                       ("type", 'Array[Integer]', 'Array [Integer]'),
                                       ("type", 'STRING', 'string'), ("required", '**Required**', 'Required')):
            with self.subTest(field=field, local=local):
                row = dict(field=field, local=local, file="03.md", article_id="1", keys=["KEY"], no="1")
                self.assertEqual(compare(row, official, {})["status"], "서식만 다름")
        row.update(field="default", local='"abc"')
        self.assertEqual(compare(row, 'ABC', {})["status"], "실제 차이")

    def test_imethod_diff_is_a_value_difference(self):
        md = ('## Node Local Axis\n\n#### iMETHOD = 1\n\n'
              '| No. | 설명 | 키 | 타입 | 기본값 | 필수 |\n'
              '| -- | -- | -- | -- | -- | -- |\n'
              '| 1 | Angle | `"iMETHOD"` | Integer | - | Optional |\n')
        name, aid = "03_fixture.md", "35807178748569"
        sources = catalog((chunk(aid, name, "## Node Local Axis", md), {}))
        rows = self.run_fixture(name, md, {aid: article(specs((1, "Angle", '"iMETHOD"', "Integer", '"ANGLE"', "Optional")))}, sources)
        default = next(row for row in rows if row["field"] == "default")
        self.assertEqual((default["status"], default["official"], default["article_id"]), ("실제 차이", '"ANGLE"', aid))

    def test_dreult_main_and_om_fields_use_their_own_article(self):
        def row(no, key, value):
            return f'| {no} | Value | `"{key}"` | number | {value} | Optional |\n'

        header = '| No. | 설명 | Key | 타입 | 기본값 | 필수 |\n| -- | -- | -- | -- | -- | -- |\n'
        main_aid, other_aid = "57390686440345", "56823620531865"
        name, section = "25_fixture.md", "## 26. DREULT — Steel Design Result"
        main_md = section + '\n\n' + header + row(1, "A", "0") + row(2, "B", "0") + row(3, "C", "false")
        other_md = f'<!-- om-fields:{other_aid} -->\n' + header + row(4, "D", "true") + '<!-- /om-fields -->\n'
        sources = catalog((chunk(main_aid, name, section, main_md), {}),
                          (chunk(other_aid, name, section, other_md, verbatim=True), {}))
        main = specs(*[(n, "Value", f'"{key}"', "number", value, "Optional")
                       for n, key, value in ((1, "A", 0), (2, "B", 0), (3, "C", "false"))])
        other = specs((1, "Value", '"A"', "number", 45, "Optional"),
                      (2, "Value", '"B"', "number", 60, "Optional"),
                      (3, "Value", '"C"', "number", "true", "Optional"),
                      (4, "Value", '"D"', "number", "true", "Optional"))
        rows = self.run_fixture(name, main_md + '\n' + other_md, {main_aid: article(main), other_aid: article(other)}, sources)
        self.assertEqual([(row["article_id"], row["official"], row["status"]) for row in rows if row["field"] == "default"],
                         [(main_aid, "0", "일치"), (main_aid, "0", "일치"), (main_aid, "false", "일치"),
                          (other_aid, "true", "일치")])

    def test_reaction_head_is_mode_specific_and_case_sensitive(self):
        name, section, aid = "19_fixture.md", "## Reaction", "36009349748249"
        global_head = ["Index", "Node", "Load", "FX"]
        local_head = ["Index", "Node", "Load", "Fx"]
        cases = [("Global", "REACTIONG", global_head), ("Local", "REACTIONL", local_head)]
        official = examples("Request Examples", [(label, {"Argument": {"TABLE_TYPE": mode, "TABLE_NAME": label}})
                                                  for label, mode, _ in cases])
        official += examples("Response Examples", [(label, {label: {"HEAD": columns}}) for label, _, columns in cases])
        for swap in (False, True):
            md = section + '\n\n### Response HEAD\n\n' + '\n'.join(
                f'- `{mode}`: `{json.dumps(cases[1-i][2] if swap else value)}`' for i, (_, mode, value) in enumerate(cases))
            sources = catalog((chunk(aid, name, section, md), {"TABLE_TYPE": ["REACTIONG", "REACTIONL"]}))
            rows = self.run_fixture(name, md, {aid: article(official)}, sources)
            self.assertEqual([r["variants"] for r in rows], [[("TABLE_TYPE", "REACTIONG")], [("TABLE_TYPE", "REACTIONL")]])
            self.assertEqual([r["status"] for r in rows], ["실제 차이" if swap else "일치"] * 2)

    def test_hold_is_watched_even_after_source_matches_local(self):
        row = dict(file="06_fixture.md", article_id="123", no="8", keys=["FV"], field="required", local="Required")
        hold = dict(row, doc_value="Required", om_value="Requirel", reason="Review note")
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "spec_holds.json"
            path.write_text(json.dumps({"holds": [hold]}), encoding="utf-8")
            holds = load_holds(path)
        self.assertIn(hold_key(row), holds)
        self.assertEqual(compare(dict(row), "Requirel", holds)["status"], "보류")
        self.assertEqual(compare(dict(row), "Optional", holds)["status"], "실제 차이")
        self.assertEqual(compare(dict(row), "Required", holds)["status"], "실제 차이")

    def test_head_subtable_uses_its_named_response_path(self):
        name, section, aid = "20_fixture.md", "## Eigenvalue Mode", "36017669319321"
        md = (section + '\n\n### Response HEAD\n\n| Table | HEAD |\n| --- | --- |\n'
              '| `EIGENVALUEANALYSIS` | `["ModeNo", "Tolerance"]` |\n')
        official = examples("Response Examples", [("Modes", {"EigenvalueMode": {
            "HEAD": ["Index", "Node", "Mode"], "SUB_TABLES": [
                {"EIGENVALUEANALYSIS": {"HEAD": ["ModeNo", "Tolerance"]}},
                {"OTHER": {"HEAD": ["ModeNo", "Frequency"]}},
            ]}})])
        sources = catalog((chunk(aid, name, section, md), {"TABLE_TYPE": ["EIGENVALUEMODE"]}))
        rows = self.run_fixture(name, md, {aid: article(official)}, sources)
        self.assertEqual([(row["official"], row["status"]) for row in rows], [(["ModeNo", "Tolerance"], "일치")])

    def test_scraped_json_recovers_nbsp_and_unescaped_windows_path(self):
        parsed, warning = load_json('{\xa0"EXPORT_PATH": "D:\\00.2023\\test.json", "HEAD": ["X"]}')
        self.assertEqual(parsed["EXPORT_PATH"], r"D:\00.2023\test.json")
        self.assertEqual(parsed["HEAD"], ["X"])
        self.assertTrue(warning)


if __name__ == "__main__":
    unittest.main()
