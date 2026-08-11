# WALL STACKER

- Original (KO): https://support.midasuser.com/hc/ko/articles/60809600655385-WALL-STACKER
- Video: [01_WALL_STACKER.mp4](../videos/01_WALL_STACKER.mp4)
- GEN NX API CHALLENGE 2026

---

A plug-in that automatically models walls and perimeter lintel beams from structural
drawings. It automatically splits wall intersections and aligns/merges nearby nodes
created by minor coordinate discrepancies in the drawing, quickly producing an
accurate analysis model free of disconnected elements and unnecessary nodes.

## Features

**01. Step-by-step guidance for first-time users**
An intuitive status bar at the top and pulsing highlights on input fields show the
current progress and the next action, so even first-time users can pick up the full
workflow quickly.

**02. Story-by-story DXF wall extraction and analysis**
Automatically extracts and analyzes wall centerlines and wall information from each
story's DXF drawing to build the set of modeling targets.

**03. Automatic wall and lintel beam modeling**
Automatically models each story's walls and opening lintel beams based on the
analyzed drawing.

**04. Automatic splitting at intersections**
Automatically detects wall intersections and splits elements there, producing a
well-connected analysis model with shared nodes.

**05. Automatic merging of nearby nodes**
Prevents multiple nodes from being created at the same joint due to minor coordinate
discrepancies in the drawing, automatically aligning and merging nearby nodes within
a configurable tolerance.
