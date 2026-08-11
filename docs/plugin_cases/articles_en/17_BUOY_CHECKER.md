# BUOY CHECKER

- Original (KO): https://support.midasuser.com/hc/ko/articles/60726911770905-BUOY-CHECKER
- Video: [17_BUOY_CHECKER.mp4](../videos/17_BUOY_CHECKER.mp4)
- GEN NX API CHALLENGE 2026

---

A plug-in that checks a structure's buoyancy (flotation) safety at completion and at
each construction stage, based on GEN NX analysis results and design conditions
entered by the user. It automatically pulls the analysis results needed for the
check straight from GEN NX, so the whole workflow — from the stage-by-stage safety
factor check, through deriving the control water level, to report output — runs as
one continuous process, without switching between separate result tables or
calculation sheets.

## Features

**01. Step-by-step guidance for first-time users**
An intuitive status bar at the top and pulsing highlights on input fields show the
current progress and the next action, so even first-time users can pick up the full
workflow quickly.

**02. Automatic linkage and cross-validation of GEN NX results**
Automatically pulls the per-story dead-load axial force and foundation support
reactions from GEN NX, then cross-validates the two analysis results to check for
missing or inconsistent data.

**03. Stage-by-stage buoyancy safety and control water level**
Automatically computes the buoyant force, resisting force, and buoyancy safety
factor for the completed state and each construction stage, and back-calculates the
control water level at each stage needed to satisfy the target safety factor.

**04. Report output with the calculation basis**
Provides a report-output feature that summarizes the input conditions,
cross-validation results, the stage-by-stage buoyancy safety factors, and the basis
for the control water level.
