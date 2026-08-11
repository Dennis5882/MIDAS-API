# Plant Frame Builder

- Original (KO): https://support.midasuser.com/hc/ko/articles/60728306572441-PlantFrameBuilder
- Video: [11_PlantFrameBuilder.mp4](../videos/11_PlantFrameBuilder.mp4)
- GEN NX API CHALLENGE 2026

---

A GEN NX API plug-in that automatically generates an initial steel frame model
(Node/Column/Beam/Brace/Support) for a two-row, multi-level pipe rack, for structural
analysis, from just the bay spacing, story height, and similar input values.

## Features

**01. Ultra-fast, parameter-driven modeling (removes repetitive input, adds practical flexibility)**
Completes a pipe-rack frame in one step from parameter input (bay spacing, story
height, etc.) alone, with no complex manual work. Existing model materials and
sections can be reused, and new ones can be created and assigned right in the UI, so
you can start even from an empty model. Everything from geometry to support
conditions is handled in one batch, meaningfully cutting down repetitive modeling
time.

**02. Real-time 3D preview with thorough pre-validation (eliminates human error)**
The 3D preview updates live as parameters change, so you can check the geometry
intuitively. Right before committing to the GEN NX model, it validates the expected
member count, the ID range to be assigned, and whether there is any conflict with
the existing model. The model is only created once validation passes, which
eliminates human error.
