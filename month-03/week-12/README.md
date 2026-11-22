Week 12: Rasters

What this folder contains

- "inspect_raster.py": inspects raster information, including dimensions, resolution, CRS, and bounds.
- "read_values.py": reads pixel values from a raster.
- "pixel_coords.py": explores pixel coordinates.
- "sample_points.py": samples raster values at point locations.
- "ndvi.py": calculates NDVI from satellite imagery.
- "plot_raster.py": displays raster data.
- "clip_raster.py": clips raster data to a specified area.
- "zonal_stats.py": calculates raster statistics within polygon areas.
- "reproject_raster.py": reprojects a raster to another CRS.
- Challenge scripts: "my_inspect.py", "my_index.py", and "my_zonal.py".
- "ndvi_map.png": map showing the NDVI results.
- "my_map.png": map of my raster analysis results.
- CSV file containing my zonal statistics results.
- "data-notes.md": notes about the raster data used.

How to run it

From the repository root:

uv run month-03/week-12/ndvi.py

What I found

The NDVI results helped me understand vegetation conditions in my study area by showing differences in vegetation values. The zonal statistics summarized the raster values within each polygon, making it easier to compare vegetation conditions between areas.

What went wrong and how I fixed it

I encountered challenges when working with raster data, especially when reading raster values and matching raster data with polygon layers. I checked the raster properties and coordinate reference systems and corrected the issues to successfully perform the analysis.

Satellite scene

- Scene name: LC08_L2SP_166065_20261004_20261009_02_T1_SR_B4

Data source

The raster data source and details are described in "data-notes.md".
