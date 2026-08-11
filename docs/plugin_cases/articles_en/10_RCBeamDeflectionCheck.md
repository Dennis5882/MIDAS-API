# RCBeamDeflectionCheck

- Original (KO): https://support.midasuser.com/hc/ko/articles/60728330684697-RCBeamDeflectionCheck
- Video: [10_RCBeamDeflectionCheck.mp4](../videos/10_RCBeamDeflectionCheck.mp4)
- GEN NX API CHALLENGE 2026

---

A plug-in that reads an RC beam's section, material, rebar arrangement, and the
analysis moment for each load case from a MIDAS GEN NX model via the API, computes
short-term and long-term deflection automatically using the effective section
stiffness (Ie, Branson) per KDS 14 20 30 §4.2, compares it against the allowable
deflection, and outputs an A4 structural calculation sheet (deflection review
report).

## Features

**01. Automatic model data retrieval**
Automatically extracts the RC beam's section, material, rebar arrangement, and
analysis moment via the API.

**02. Automatic deflection calculation**
Automatically derives short-term and long-term deflection per the KDS 14 20 30
criteria.

**03. Automatic check against the allowable limit**
Compares the computed result against the allowable deflection and determines
pass/fail.

**04. Automatic structural calculation sheet output**
Generates an A4 deflection review report that includes the calculation process and
results.
