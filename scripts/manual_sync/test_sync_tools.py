"""Offline regressions for fill_fields, eval_retrieval, check_diff and build_index anchors."""
import contextlib
import io
import json
import os
import re
import sys
import tempfile
import unittest
from unittest.mock import patch

import build_index
import check_diff
import check_fields as cf
import eval_retrieval
import fill_fields

BODY = ('<h3>Specifications</h3><table><tr><td>1</td><td>Name</td><td>"NAME"</td>'
        '<td>String</td><td>-</td><td>Required</td></tr></table>')
DOC = "# 99. Test\n\n## 1. `/db/X` — X\n\nText.\n"


def run_fill(folder, articles, ko_ids=(), argv=(), spec_rows=None):
    """Run fill_fields.main on a temporary docs folder; every article covers section 1."""
    def analyze(articles_, sections, shared, mapping, skipped):
        host = next(s for s in sections if s["heading"].startswith("## 1."))
        return [dict(id=aid, title="T", missing=["NAME"], sections=[host]) for aid in sorted(articles_)], [], 0, 0

    with patch.object(cf, "_DOCS", folder), \
         patch.object(fill_fields, "fetch_bodies", return_value=articles), \
         patch.object(cf, "analyze", side_effect=analyze), \
         patch.object(cf, "mapped_headings", return_value={}), \
         patch.object(sys, "argv", ["fill_fields.py", *argv]), \
         contextlib.ExitStack() as stack:
        if spec_rows is not None:
            stack.enter_context(patch.object(fill_fields, "spec_rows", side_effect=spec_rows))
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            fill_fields.main()
        return out.getvalue()


def article(locale):
    return dict(body=BODY, locale=locale, html_url=f"https://x/hc/{locale}/articles/1")


class FillFieldsTests(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.mkdtemp()
        self.path = os.path.join(self.folder, "99_test.md")
        with open(self.path, "w", encoding="utf-8", newline="\n") as f:
            f.write(DOC)

    def text(self):
        with open(self.path, encoding="utf-8") as f:
            return f.read()

    def test_second_ko_only_twin_does_not_repeat_rows(self):
        run_fill(self.folder, {"801": article("ko"), "802": article("ko")})
        blocks = re.findall(r"<!-- om-fields:(\d+) -->", self.text())
        self.assertEqual(blocks, ["801"])

    def test_failure_after_strip_leaves_existing_blocks(self):
        run_fill(self.folder, {"801": article("en-us")})
        before = self.text()
        self.assertIn("om-fields:801", before)

        def broken(body):
            raise ValueError("bad table")

        with self.assertRaises(ValueError):
            run_fill(self.folder, {"801": article("en-us")}, spec_rows=broken)
        self.assertEqual(self.text(), before)

    def test_dry_run_counts_what_a_real_run_writes_and_changes_nothing(self):
        run_fill(self.folder, {"801": article("en-us")})
        before = self.text()
        dry = run_fill(self.folder, {"801": article("en-us")}, argv=["--dry-run"])
        self.assertEqual(self.text(), before)
        real = run_fill(self.folder, {"801": article("en-us")})
        count = lambda out: re.search(r"table keys copied: (\d+)", out).group(1)
        self.assertEqual(count(dry), count(real))
        self.assertEqual(count(dry), "1")
        self.assertEqual(self.text(), before)


class EvalRetrievalTests(unittest.TestCase):
    def test_failed_rebuild_keeps_existing_questions(self):
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "eval_questions.json")
            with open(path, "w", encoding="utf-8") as f:
                json.dump([{"q": "kept"}], f)
            with patch.object(eval_retrieval, "QUESTIONS", path), \
                 patch.object(eval_retrieval, "build_questions", side_effect=OSError("429")), \
                 patch.object(sys, "argv", ["eval_retrieval.py", "--rebuild"]):
                with self.assertRaises(OSError):
                    eval_retrieval.main()
            with open(path, encoding="utf-8") as f:
                self.assertEqual(json.load(f), [{"q": "kept"}])


class CheckDiffTests(unittest.TestCase):
    def note(self, url, moved):
        entry = {"id": "1", "html_url": url, "old_updated_at": "2026-01-01"}
        with patch.object(check_diff, "locales_changed_since", return_value=(moved, {})):
            check_diff.annotate_locales([entry])
        return entry["locale_note"]

    def test_ko_only_article_change_is_a_normal_review(self):
        self.assertEqual(self.note("https://x/hc/ko/articles/1-a", ["ko"]), "ko changed — normal review")

    def test_ko_edit_of_an_en_us_article_is_still_flagged(self):
        self.assertIn("en-us did NOT", self.note("https://x/hc/en-us/articles/1-a", ["ko"]))


class AnchorTests(unittest.TestCase):
    def test_repeated_headings_get_github_suffixes(self):
        text = "# T\n\n## Input\n\n```\n## Input\n```\n\n## Input\n\n### Input\n"
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "20_test.md")
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
            build_index._ANCHORS.clear()
            lines = text.splitlines()
            anchors = [build_index.anchor(dict(path=path, start=n, heading=line))
                       for n, line in enumerate(lines) if line.startswith("##") and n != 5]
            build_index._ANCHORS.clear()
        self.assertEqual(anchors, ["input", "input-1", "input-2"])


if __name__ == "__main__":
    unittest.main()
