# AutoGenerationCmFactor

- Original (KO): https://support.midasuser.com/hc/ko/articles/60729138404761-AutoGenerationCmFactor
- Video: [04_AutoGenerationCmFactor.mp4](../videos/04_AutoGenerationCmFactor.mp4)
- GEN NX API CHALLENGE 2026

---

A plug-in that automatically computes the seismic-load Cm Factor (correction factor)
needed when generating load combinations in MIDAS GEN NX.

## Features

**01. Compute the seismic load correction factor**
Automatically calculates the seismic-load Cm Factor (correction factor) needed when
generating load combinations in MIDAS GEN NX.

**02. Automatic input**
Pulls in, in one step, all the values already entered in the model that are needed
to derive the correction factor.

**03. Applies KDS 41 17 00 §4.2.2**
Automatically judges and applies both of the following: (2) where bedrock depth
exceeds 20 m and the average shear-wave velocity of the soil is 360 m/s or more,
apply 80% of Fᵥ as specified in Table 4.2-2; (3) where the soil classification is S5
and the bedrock depth is unclear, apply 110% of Fₐ and Fᵥ as specified in Tables
4.2-1 and 4.2-2.

**04. Output a calculation report for the correction factor**
Outputs a calculation report documenting exactly what data the correction factor was
derived from.
