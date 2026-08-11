# WallMark Auto Mapper

- Original (KO): https://support.midasuser.com/hc/ko/articles/60809496186521-WallMarkAutoMapper
- Video: [02_WallMarkAutoMapper.mp4](../videos/02_WallMarkAutoMapper.mp4)
- GEN NX API CHALLENGE 2026

---

WallMark Auto Mapper is a plug-in that extracts wall names and location information
from a DXF structural plan, automatically matches them against the wall locations
already assigned to each Wall ID in the MIDAS GEN NX analysis model, and assigns the
drawing's wall names to the matching Wall ID as its Wall Mark. The automatic matching
results can be reviewed and edited in a preview and result table before being
selectively applied to the model.

## Features

**01. Extract wall names and locations from the DXF drawing**
Extracts wall names and location information from a specified layer of the selected
DXF structural plan, automatically building the drawing-side dataset to be matched
against the GEN NX model.

**02. Compute wall centroid coordinates per GEN NX Wall ID**
Selects the wall elements corresponding to the chosen story and Wall Type (Membrane
or Plate), and uses their Node and Element data to compute the wall centroid
coordinates for each existing Wall ID.

**03. Automatic matching of drawing wall data to Wall ID**
Compares the wall names and locations extracted from the DXF structural plan against
the wall centroid coordinates of each Wall ID in the GEN NX analysis model, within a
tolerance distance, and links the closest candidate. Matching results are classified
as matched, needs review, or failed, and shown in the preview and result table.

**04. Review, apply, and manage Wall Marks**
After reviewing and editing the matching results between drawing wall names and Wall
IDs in the preview and result table, assigns the selected drawing wall name as the
Wall Mark to one or more matching Wall IDs. Supports adding, editing, and deleting
existing Wall Marks, Excel import/export, and PDF result table output.
