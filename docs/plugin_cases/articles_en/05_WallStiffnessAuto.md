# WallStiffnessAuto

- Original (KO): https://support.midasuser.com/hc/ko/articles/60729084287897-WallStiffnessAuto
- Video: [05_WallStiffnessAuto.mp4](../videos/05_WallStiffnessAuto.mp4)
- GEN NX API CHALLENGE 2026

---

WallStiffnessAuto reads RC wall design (KDS-41-20-2022) results directly through the
GEN NX API, and progressively lowers the Wall Stiffness Scale Factor (WSSF) of any
wall that exceeds the code check, on its own, until all NG results are cleared.

## Features

**01. Automatic detection of NG members**
After running the structural analysis and wall design, automatically extracts the
walls that exceed the code check by story/Wall ID and shows the governing stress
ratio alongside each one.

**02. Configure reduction conditions**
Set the reduction step size, the lower bound for the factor, and the maximum number
of iterations, and the automatic loop runs within that range.

**03. Automatic iterative reduction**
Each iteration applies the reduced stiffness, re-runs the analysis, then re-checks
the design; the loop stops automatically once all NG results are cleared or the
factor reaches its lower bound.

**04. Restore the factor**
At any point during the iterations, the reduced factor can be restored to its
pre-reduction value (1.0) with a single button click.
