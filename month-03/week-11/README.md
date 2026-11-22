Week 11: CRS and spatial operations

What this folder contains

- "area_wrong_and_right.py": calculates area using different coordinate reference systems.
- "set_vs_to.py": changes the coordinate reference system of a layer.
- "one_point.py": works with a single point geometry.
- "spatial_ops.py": performs spatial operations on geographic data.
- "coverage_gap.py": examines coverage gaps in an area.
- "nearest.py": finds the nearest features.
- "clip_dissolve.py": clips and dissolves spatial layers.
- "fix_geometry.py": checks and fixes invalid geometries.
- Challenge scripts: "my_crs.py", "my_count.py", "my_reach.py", and "my_validity.py".
- Map showing the results of my spatial operations.

How to run it

From the repository root:

uv run month-03/week-11/nearest.py

What I found

I learned how coordinate reference systems affect spatial measurements and how spatial operations can be used to analyze geographic data. I also explored how to find the nearest features, count features within an area, and examine spatial coverage.

What went wrong and how I fixed it

I encountered problems when working with coordinate reference systems and spatial measurements. I solved them by checking the CRS of my layers and using an appropriate projected CRS for the spatial operations.


One limitation of the method

The accuracy of spatial analysis depends on the quality of the input data and the coordinate reference system used. Incorrect or incomplete spatial data can affect the results.
