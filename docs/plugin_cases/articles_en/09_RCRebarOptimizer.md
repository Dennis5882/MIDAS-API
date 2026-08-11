# RCRebarOptimizer

- Original (KO): https://support.midasuser.com/hc/ko/articles/60728648218265-RCRebarOptimizer
- Video: [09_RCRebarOptimizer.mp4](../videos/09_RCRebarOptimizer.mp4)
- GEN NX API CHALLENGE 2026

---

A plug-in that uses MIDAS GEN NX's RC design API (DCRM, CD/BD-ANAL, design result
tables) to automatically sweep candidate bar sizes for the main reinforcement of RC
columns and beams, derive the minimum steel arrangement per member that satisfies
the check ratio (CHK), and unify members sharing the same section (same column mark
or beam mark) into a single standard rebar arrangement.

## Features

**01. Result-driven design**
Uses MIDAS GEN NX's RC design API (DCRM, CD/BD-ANAL, design result tables) to
automatically sweep candidate bar sizes for the main reinforcement of RC columns and
beams.

**02. Member review**
Derives, per member, the minimum steel arrangement that satisfies the check ratio
(CHK), and unifies members sharing the same section (same column mark or beam mark)
into a single standard rebar arrangement.

**03. Member design**
Every standard rebar arrangement is re-verified by re-running the GEN NX design,
guaranteeing safety, and a governing-factor diagnosis shows which members can still
be reduced further.

**04. Result review**
Outputs the rebar schedule and comparison results as PDF immediately, cutting the
time needed to prepare design, quantity, and review documents.
