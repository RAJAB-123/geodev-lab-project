# Month 1 Summary

## Question

How many buildings in Study area, Dar es Salaam, are located within
50 metres of rivers?

## Operation

Buffered the processed river network by 50 metres using
EPSG:32737 (WGS 84 / UTM Zone 37S), then used Select by Location
to identify buildings that intersect the buffered area.

## Expected

I expected several buildings to fall within the 50 metre river
buffer because my study area is a densely developed urban area with
buildings located close to rivers and drainage channels.

## Got

The analysis identified  1,838 building within or intersecting
the 50 metre river buffer.

## The four checks

**Looked at the map.** The 50 metre buffer follows the river
network, and the selected buildings are located within the
buffered areas as expected.

**Checked the row count.** **1,838 buildings** were selected.
This gives the number of buildings within or intersecting the
50 metre river buffer.

**Checked one by hand.** I selected individual buildings on the
map and checked that they were located within the 50 metre
buffer. The selected buildings were spatially consistent with
the buffer.

**Looked for empty geometry.** I checked the analysis result for
empty geometries.

## What surprised me

I was surprised by the large number of buildings located within
50 metres of rivers. The result shows that many buildings in
study area are close to the river and drainage network.

## Limitations, stated plainly

- A 50m etre buffer measures straight-line distance, not actual
  flood water travel distance.
- Being within 50 metres of a river does not automatically mean
  that a building will flood.

## What I still need

- DEM/elevation data to understand the relationship between
  buildings and low-lying areas.
- Flood depth or flood extent data to identify areas that have
  actually been affected or may be affected by flooding.
- Rainfall data to support further flood risk analysis.

## Output

The river buffer is saved as:

-data/processed/river_buffer_50m.gpkg

The final analysis map is saved as:

-maps/Map 1.png

