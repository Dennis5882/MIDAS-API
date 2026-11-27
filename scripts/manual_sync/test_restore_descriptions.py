"""Safety regressions for source restoration (offline, no model/API calls)."""
import contextlib
import html
import io
import json
import tempfile
from pathlib import Path
import unittest
from unittest.mock import patch

import restore_descriptions as rd


def spec(desc="Source description", no="1", group="", required="Required"):
    return dict(desc=desc, no=no, keys=["NAME"], group=group, required=required,
                type="String", default="-")


class RestoreSafetyTests(unittest.TestCase):
    def test_description_markup_and_missing_group_compare_equal(self):
        cases = [
            ("　　└ Name ᴶ⁾", "Name", ""),
            ("Type • DB: 1 ◦ USER: 2", "Type · DB: 1 · USER: 2", ""),
            (r"**Name**   `A` \| B", "Name A | B", ""),
            ("Name", "Name", 'When "iTYPE" is 1'),
        ]
        for local, description, group in cases:
            with self.subTest(local=local):
                rendered, _ = rd.render(spec(description, group=group), local)
                self.assertTrue(rd.description_matches(local, rendered, description))

    def test_case_punctuation_and_an_explicit_different_group_remain_differences(self):
        for local in ("name", "Name.", "Name,", "[When X is 2] Name"):
            with self.subTest(local=local):
                self.assertFalse(rd.description_matches(local, "[When X is 1] Name", "Name"))

    def test_required_condition_needs_evidence_and_value_must_be_standard(self):
        self.assertEqual(rd.compare_text("Required"), rd.compare_text("**Required**"))
        self.assertTrue(rd.required_hold('**Required** (`OPT_TR`)', spec(group="When OPT_TRIM")))
        self.assertEqual(rd.required_hold('Required (if OPT_TR=true)', spec(group='When "OPT_TR" = true')), "")
        self.assertEqual(rd.required_hold('Required (OPT_TR=true)', spec('Length if "OPT_TR": true')), "")
        self.assertTrue(rd.required_hold('Required (OPT_TR=true)', spec('Length if "OPT_TR": false')))
        self.assertEqual(rd.required_hold("Optional", spec(required="GET only")), "")
        for value in ("Require", "Requirel", "Optional9", "-", "", '"GET"only'):
            with self.subTest(official=value):
                self.assertTrue(rd.required_hold("Optional", spec(required=value)))

    def test_matching_nonstandard_source_overrides_a_registered_hold(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "02_test.md"
            original = '| 1 | Mode 1Required | `"NAME"` | String | - | Require |\n'
            path.write_bytes(original.encode("utf-8"))
            body = ('<h3>Specifications</h3><table><tr><td>1</td><td>Mode 1Required</td>'
                    '<td>"NAME"</td><td>String</td><td>-</td><td>Require</td></tr></table>')
            host = dict(file=path.name, level=2, start=0, end=1, text=original, endpoints={"DB/X"})
            held = dict(om_desc="Old mode", om_required="Optional", reason="Check source")
            with patch.object(rd.cf, "load_sections", return_value=([host], {})), \
                 patch.object(rd.cf, "mapped_headings", return_value={}), \
                 patch.object(rd.cf, "covering", return_value=([host], [])), \
                 patch.object(rd, "load_holds", return_value={(path.name, "a", ("NAME",), "1"): held}):
                records, outputs = rd.analyze({"a": {"body": body}}, [path])
            self.assertEqual(records[0]["status"], "일치")
            self.assertEqual(outputs[path][:2], (original, original))

    def test_section_number_is_ignored_without_losing_following_values(self):
        self.assertEqual(rd.loss_signals("　　└ 3.16.7.2 Deck Stiffness Number", "Deck Stiffness Number"), [])
        self.assertTrue(rd.loss_signals("　　└ 3.16.1 Dimensions — GI uses [B1, B2]", "Dimensions"))
        self.assertTrue(rd.loss_signals("　　└ 4.1.1 Dimensions — GI uses [Sg, Top, Bot]", "Dimensions"))
        self.assertTrue(rd.loss_signals("Minimum ratio: 0.4", "Minimum ratio"))

    def test_reviewer_numbering_only_applies_to_the_reviewed_sequence(self):
        source = dict(spec("Reviewed Data 2"), keys=["CDATE1"])
        project = ["35801869341337"]
        self.assertTrue(rd.project_reviewer_renumbering("Checker 1 Date", source, project))
        self.assertFalse(rd.project_reviewer_renumbering("Checker 1 Date (0–255)", source, project))
        self.assertFalse(rd.project_reviewer_renumbering("Checker 1 Date", source, ["other"]))
        self.assertFalse(rd.project_reviewer_renumbering("Checker 1 Date", dict(source, desc="Reviewed Data 3"), project))

    def test_english_apply_preserves_holds_and_detects_source_changes(self):
        original = (
            '| 1 | Keep this description | `"NAME"` | String | - | Required |\n'
            '| 2 | code. | `"CODE"` | String | - | Required |\n'
            '| 3 | 번역 | `"OTHER"` | String | - | Required |\n'
            '| 4 | Name | `"MODE"` | String | - | Required (Auto) |\n'
            '| 5 | Value | `"SPEC"` | String | - | Optional |\n'
        )
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            doc = root / "docs/manual/02_test.md"
            doc.parent.mkdir(parents=True)
            doc.write_bytes(original.encode("utf-8"))
            (doc.parent / "jp_only.json").write_text("{}", encoding="utf-8")
            holds = root / "scripts/manual_sync/description_holds.json"
            holds.parent.mkdir(parents=True)
            holds.write_text(json.dumps({"holds": [{
                "file": doc.name, "article_id": "a", "no": "1", "keys": ["NAME"],
                "om_desc": "Official name", "om_required": "Required", "reason": "Keep condition"
            }]}), encoding="utf-8")
            host = dict(file=doc.name, level=2, start=0, end=5, text=original, endpoints={"DB/X"})

            def body(name="Official name", required="Required"):
                rows = [
                    ("1", name, "NAME", required),
                    ("2", "Code", "CODE", "Required"),
                    ("3", "Other", "OTHER", "Required"),
                    ("4", "Name", "MODE", "Required"),
                    ("5", "Value", "SPEC", "Require"),
                ]
                return "<h3>Specifications</h3><table>" + "".join(
                    f'<tr><td>{no}</td><td>{html.escape(desc)}</td><td>"{key}"</td>'
                    f'<td>String</td><td>-</td><td>{req}</td></tr>'
                    for no, desc, key, req in rows
                ) + "</table>"

            args = ["--file", doc.name, "--english", "--report", str(root / "report.md")]
            with patch.object(rd, "ROOT", root), \
                 patch.object(rd.cf, "load_sections", return_value=([host], {})), \
                 patch.object(rd.cf, "mapped_headings", return_value={}), \
                 patch.object(rd.cf, "covering", return_value=([host], [])), \
                 contextlib.redirect_stdout(io.StringIO()):
                first = rd.main(args, articles={"a": {"body": body()}})
                self.assertEqual([r["status"] for r in first], ["보류", "변경", "보류", "보류"])
                expected = original.replace("| code. |", "| Code |").replace(
                    '`"CODE"` | String | - | Required |', '`"CODE"` | String | - | **Required** |')
                self.assertEqual(doc.read_bytes(), expected.encode("utf-8"))
                for changed in (body(name="Updated name"), body(required="Optional")):
                    recorded = rd.main([*args, "--dry-run"], articles={"a": {"body": changed}})
                    self.assertEqual(recorded[0]["status"], "보류 — 원문 변경")
                    self.assertEqual(doc.read_bytes(), expected.encode("utf-8"))
                report = (root / "report.md").read_text(encoding="utf-8")
                self.assertIn("영어 보류 — 원문 변경", report)
                self.assertIn("## 보류 — 원문 변경", report)

    def test_dry_run_preserves_documents_and_existing_report(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "docs/manual/13_test.md"
            source.parent.mkdir(parents=True)
            source.write_bytes(b"unchanged\r\n")
            report = root / "report.md"
            report.write_text("Previous descriptions\n", encoding="utf-8")
            with patch.object(rd, "ROOT", root), \
                 patch.object(rd, "analyze", return_value=([], {source: ("unchanged\n", "new\n", True)})), \
                 patch.object(rd, "fetch_bodies", side_effect=AssertionError("unexpected network")), \
                 contextlib.redirect_stdout(io.StringIO()):
                rd.main(["--file", source.name, "--dry-run", "--report", str(report)], articles={})
            self.assertEqual(source.read_bytes(), b"unchanged\r\n")
            self.assertTrue(report.read_text(encoding="utf-8").startswith("Previous descriptions\n"))

    def test_duplicate_key_needs_unique_number(self):
        rows = {"a": [spec(no="1"), spec(no="2")]}
        self.assertEqual(rd.pair(["NAME"], "2", {"a"}, rows)[1][0][1]["no"], "2")
        self.assertEqual(rd.pair(["NAME"], "—", {"a"}, rows)[0], "모호")
        rows["a"].append(spec(no="2"))
        self.assertEqual(rd.pair(["NAME"], "2", {"a"}, rows)[0], "모호")

    def test_nested_group_stops_at_enclosing_rowspan(self):
        html = """<h3>Specifications</h3><table>
          <tr><td colspan="6">When DGRM_TYPE = 0</td></tr>
          <tr><td rowspan="3">10</td><td>Stress Line</td><td>"STRESS_LINE"</td>
            <td>Object</td><td>-</td><td>Optional</td></tr>
          <tr><td colspan="5">When STRESS_LINE.OPT_USE = true</td></tr>
          <tr><td>Compression</td><td>"COMP"</td><td>Number</td><td>-</td><td>Required</td></tr>
          <tr><td>11</td><td>7th DOF Type</td><td>"7TH_DOF_TYPE"</td>
            <td>Integer</td><td>-</td><td>Required</td></tr></table>"""
        parent, child, peer = rd.spec_rows(html, scoped_groups=True)
        self.assertEqual(parent["group"], "When DGRM_TYPE = 0")
        self.assertEqual(child["group"], "When STRESS_LINE.OPT_USE = true")
        self.assertEqual(peer["group"], "")
        self.assertEqual(peer["keys"], ["7TH_DOF_TYPE"])

    def test_country_articles_must_agree(self):
        rows = {"a": [spec()], "b": [spec("Another meaning")]}
        self.assertEqual(rd.pair(["NAME"], "1", set(rows), rows)[0], "모호")
        rows["b"] = [spec()]
        self.assertEqual(rd.pair(["NAME"], "1", set(rows), rows)[0], "")

    def test_missing_key_is_not_guessed(self):
        self.assertEqual(rd.pair(["UNKNOWN"], "1", {"a"}, {"a": [spec()]})[0], "짝 없음")

    def test_composite_keys_are_counted_without_guessing_a_leaf(self):
        row = '| 1 | 번역 | `"DATA1.DESIGN.bLAMBDA"` | Boolean | - | 선택 |'
        keys = list(rd.table_rows(row))[0][-1]
        self.assertEqual(keys, ["DATA1.DESIGN.bLAMBDA"])
        self.assertEqual(rd.pair(keys, "1", {"a"}, {"a": [spec()]})[0], "짝 없음")

    def test_decorations_group_and_pipe(self):
        desc, required = rd.render(spec("Left | Right", group="When X is true"), "　　└ 번역 ᴴˢ⁾")
        self.assertEqual(desc, "　　└ [When X is true] Left \\| Right ᴴˢ⁾")
        self.assertEqual(required, "**Required**")

    def test_oneof_note_only_labels_the_named_alternatives(self):
        group = 'oneOf Choose exactly one of "NAME" or "OTHER".'
        self.assertIn(group, rd.render(spec(group=group), "번역")[0])
        row = spec(group=group)
        row["keys"] = ["UNRELATED"]
        self.assertEqual(rd.render(row, "번역")[0], "Source description")

    def test_generated_and_fenced_rows_are_untouched(self):
        row = '| 1 | 설명 \\| 보충 | `"NAME"` | String | - | 필수 |'
        text = f"```text\n{row}\n```\n<!-- om-fields:1 -->\n{row}\n<!-- /om-fields -->\n{row}"
        rows = list(rd.table_rows(text))
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][2][1], "설명 \\| 보충")
        self.assertEqual(rows[0][2][5], "필수")

    def test_warning_wrap_and_exact_key(self):
        host = dict(text="⚠️ 공식 설명 오류\n`NAME` 확인", endpoints={"DB/X"})
        self.assertTrue(rd.protected([], ["NAME"], host, {"a"}, []))
        self.assertFalse(rd.protected([], ["NAM"], host, {"a"}, []))
        self.assertTrue(rd.protected(["⚠️ 설명"], ["NAME"], None, set(), []))

    def test_jp_endpoint_and_qualified_field(self):
        host = dict(text="", endpoints={"VIEW/DISPLAY"})
        item = dict(type="field", uri="/view/DISPLAY", keys=["MISC.GRID_MODEL_LOAD_LINE"])
        self.assertTrue(rd.protected([], ["GRID_MODEL_LOAD_LINE"], host, set(), [item]))
        self.assertFalse(rd.protected([], ["NAME"], host, set(), [item]))
        item = dict(type="endpoint", article_id="a")
        self.assertTrue(rd.protected([], ["NAME"], host, {"a"}, [item]))

    def test_loss_hints_cover_numbers_and_enum(self):
        self.assertTrue(rd.loss_signals("빨강 (0–255)", "Line Color Red"))
        self.assertIn("원문에 없는 값: PLANE", rd.loss_signals('방향 `"PLANE"`', 'Direction "DIR"'))
        self.assertEqual(rd.loss_signals("점 1 – X 좌표", "Point 1 - X"), [])

    def test_only_allowed_cells_change_and_second_pass_is_stable(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "13_test.md"
            original = ('## 1. /db/X\n### Parameters\n'
                        '| 7 |　　└ 번역 ᴶ⁾ | `"NAME"` | WeirdType | `99` | 필수 | extra |\n'
                        '<!-- om-fields:1 -->\n| 1 | 생성 | `"NAME"` | String | - | 필수 |\n'
                        '<!-- /om-fields -->\n')
            path.write_bytes(original.replace("\n", "\r\n").encode("utf-8"))
            host = dict(file=path.name, level=2, start=0, end=7, text=original, endpoints={"DB/X"})
            body = ('<h3>Specifications</h3><table><tr><td>7</td><td>Left | Right</td>'
                    '<td>"NAME"</td><td>String</td><td>-</td><td>Required</td></tr></table>')
            with patch.object(rd.cf, "load_sections", return_value=([host], {})), \
                 patch.object(rd.cf, "mapped_headings", return_value={}), \
                 patch.object(rd.cf, "covering", return_value=([host], [])):
                records, outputs = rd.analyze({"a": dict(body=body)}, [path])
                before, after, crlf = outputs[path]
                self.assertTrue(crlf)
                self.assertEqual(before, original)
                self.assertEqual(path.read_bytes(), original.replace("\n", "\r\n").encode("utf-8"))
                self.assertEqual(after, original.replace("　　└ 번역 ᴶ⁾", "　　└ Left \\| Right ᴶ⁾")
                                 .replace("| 필수 | extra", "| **Required** | extra"))
                self.assertEqual(len(records[0]["differences"]), 2)
                rd.write(path, after, crlf)
                second, new_outputs = rd.analyze({"a": dict(body=body)}, [path])
                self.assertEqual(second[0]["status"], "일치")
                self.assertEqual(new_outputs[path][0], new_outputs[path][1])
                self.assertIn(b"\r\n", path.read_bytes())


if __name__ == "__main__":
    unittest.main()
