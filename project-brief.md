# Mapping flood risks, affected communities and facilities in Dar es salaam city in Tanzania.

## The question 
Which areas have effected with flooding in Dar es salaam city and how many settlements and amenity are located within the effected areas?

## Why it matters
Flooding can dicrupt access to important social services like schools, health centar and religious facilties. The outcome can help local authorities and other emergency planners to identify which areas are need more attention before and after flooding occur.

## The data i need
- Dar es salaam administrative boundary 
- River ways and water ways.
- Elevation (DEM)
- Flood harzad areas
- Amenity location
- Roads
- Population data
- Seltlement data

## Where each data come from
 
|--------------------------|--------------|----------|----------|-------------------------------------------------------------------|
| Dataset                  |    Source    | Format   | Size     | link                                                              |
|--------------------------|--------------|----------|----------|-------------------------------------------------------------------|
| Administrative boundary  | GADM 4.1     |GeoPackage|  35 MB   |https://geodata.ucdavis.edu/gadm/gadm4.1/gpkg/gadm41_TZA.gpkg      |
| -------------------------|--------------|----------|----------|-------------------------------------------------------------------|
| Settlement extents       |GRID3 TZA v3.0|GeoPackage| 42.9 MB  |https://academiccommons.columbia.edu/doi/10.7916/gty3-ga70/download|
|--------------------------|--------------|----------|----------|-------------------------------------------------------------------|
| Flood hazard             | METEOR       | GeoTIFF  | 52.9 MB  | https://zenodo.org/records/19064462s                              |
|--------------------------|--------------|----------|----------|-------------------------------------------------------------------|
| Elevation (DEM)          | DEM          |GeoTIFF   |  35 MB   |https://dataspace.copernicus.eu/explore-data/data-collections      |
|--------------------------|--------------|----------|----------|-------------------------------------------------------------------|
| Rivers & watercourses    |OpenStreetMap |GeoPackage|  65 MB   |https://download.geofabrik.de/africa/tanzania.html                 |
|--------------------------|--------------|----------|----------|-------------------------------------------------------------------|

## What I would build 
I would build an intaractive web map of Dar es salaam city which show effected areas and amenity. The map allow users to identfy how many settlements are located in floods areas and can suggest best way that can be used to over come the effect.