# Crane Loader

- Original (KO): https://support.midasuser.com/hc/ko/articles/60726976341017-CRANE-LOADER
- Video: [16_CRANE_LOADER.mp4](../videos/16_CRANE_LOADER.mp4)
- GEN NX API CHALLENGE 2026

---

A plug-in that automatically derives wheel reactions from crane specifications and
the maximum envelope reaction on the columns supporting the runway beam. With a
single button, it generates the load cases needed for the crane's vertical and
horizontal loads and applies the computed nodal loads to the GEN NX model in a
batch. The entire workflow — from load derivation, through model input, to checking
the basis of application and producing the structural calculation report — runs as
one continuous process, without switching between a separate calculation tool and
GEN NX.

## Features

**01. Step-by-step guidance for first-time users**
An intuitive status bar at the top and pulsing highlights on input fields show the
current progress and the next action, so even first-time users can pick up the full
workflow quickly.

**02. Maximum envelope reaction for multiple cranes**
Reflects the simultaneous-operation condition of multiple cranes to compute each
crane's wheel reaction, and automatically derives, via influence-line analysis, the
maximum envelope reaction for each runway-beam support column.

**03. Batch input of load cases and nodal loads**
Automatically generates the load cases needed for the crane's vertical and
horizontal loads, and applies the computed nodal loads to the selected nodes of the
GEN NX model, in a batch, by load case.

**04. Report output with the calculation basis**
Provides a report-output feature summarizing the basis for deriving the wheel
reactions and applied loads from the crane specifications.
