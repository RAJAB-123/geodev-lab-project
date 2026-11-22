import geopandas as gpd

print(gpd.list_layers("Data/processed/study_area.gpkg"))

study_area = gpd.read_file("Data/processed/study_area.gpkg", layer="study_area")

print(study_area.head())

print("Rows and columns:", study_area.shape)

print(study_area.geom_type.value_counts())

print("CRS:", study_area.crs)

print("Bounds:", study_area.total_bounds)