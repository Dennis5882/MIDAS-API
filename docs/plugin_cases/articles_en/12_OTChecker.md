# OT CHECKER

- Original (KO): https://support.midasuser.com/hc/ko/articles/60728235211801-OTChecker
- Video: [12_OTChecker.mp4](../videos/12_OTChecker.mp4)
- GEN NX API CHALLENGE 2026

---

A plug-in that checks a structure's overturning stability under wind and seismic
loads, based on GEN NX analysis results and design conditions entered by the user.
It automatically pulls the dead-load support reactions and overturning moments
needed for the check straight from GEN NX, so the whole workflow — from reviewing
analysis results, through the overturning stability check and governing-condition
determination, to report output — runs as one continuous process without switching
between separate result tables or calculation sheets.

## Features

**01. Step-by-step guidance for first-time users**
An intuitive status bar at the top and pulsing highlights on input fields show the
current progress and the next action, so even first-time users can pick up the full
workflow quickly.

**02. Automatic linkage of GEN NX results**
Automatically pulls the dead-load support reactions and the foundation-level
overturning moments for the wind and seismic load cases from GEN NX, and derives the
resisting moment using the actual lever-arm distance and the self-weight of
foundations/walls outside the model.

**03. Overturning stability and governing-condition determination**
Builds the KDS load combinations per the strength design method or the allowable
stress design method, and compares the overturning moment, resisting moment, and
safety factor for wind and seismic loads together to determine the governing
condition.

**04. Report output with the calculation basis**
Provides a report-output feature that summarizes the input conditions, GEN NX
analysis results, overturning stability check results, and the detailed calculation
basis.
