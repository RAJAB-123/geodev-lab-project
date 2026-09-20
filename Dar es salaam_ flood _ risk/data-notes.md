# Data Notes

## Dar es salaam Wards
- Source: National Beureau of statistics Tanzania
- Downloade: September 12 2026
- Source link: https://www.nbs.go.tz
- Geometry: Polygon
- Columns: 1
- Missing values: No null values
- Coverage: Full/All

## Tabata Boundary

- Source: National Beureau of statistics Tanzania
- Downloade: September 12 2026
- Source link: https://www.nbs.go.tz
- Geometry: Polygon
- Columns: 1
- Missing values: No null values
- Coverage: Full/All

## Buildings
- Source: OpenStreetMap
- Source link: https://www.openstreetmap.org
- Extraction method: QuickOSM
- Query: building=*
- Features:16879
- Geometry: Polygon
- Columns: 16879
- Missing values: No null values
- Coverage: All

## Roads

- Source: OpenStreetMap
- Source link: https://www.openstreetmap.org/
- Extraction method: QuickOSM
- Query: highway=*
- Features: 3930
- Geometry: Line
- Columns: 3930
- Missing values:No null values
- Coverage: All

## Amenities

- Source: OpenStreetMap
- Source link: https://www.openstreetmap.org/
- Extraction method: QuickOSM
- Query: amenity=*
- Features:2832
- Geometry: Point   
- Columns: 2832
- Missing values: No null values
- Coverage: All

## Dar es salaam GeoTiff

- Source: National Beureau of statistics Tanzania
- Downloade: September 12 2026
- Source link: https://www.nbs.go.tz
-Elevetion: 258M to -4M

## Waterway 

- Source: OpenStreetMap
- Source link: https://www.openstreetmap.org/
- Extraction method: QuickOSM
- Query: Waterway=*
- Features:2231
- Geometry: Line   
- Columns: 2231
- Missing values: No null values
- Coverage: All

## CRS and preparation

- All source layers were checked for their original CRS before processing.
- Study area: Tabata, Dar es Salaam, Tanzania.
- Study area boundary extracted and saved as "study_area.gpkg".
- Working CRS: EPSG:32737 (WGS 84 / UTM 37S).
- Buildings, roads, and amenities clipped to the study area, then reprojected to EPSG:32737.
- Area calculated in square metres and converted to square kilometres.
- Area check: calculated Tabata area compared with a reliable published/reference figure.
- Quality checks completed for CRS, geometry, missing values, and clipping.
- Working files saved in "data/processed/"; raw files in "data/raw/" left untouched.