Week 10: GeoPandas, layers as tables

## What this folder contains
- explore_pandas.py: first look at the ward population table
- join_population.py: joins population to ward polygons after cleaning names
- facilities_map.png: map of health facilities by ward
- 
## How to run it
From the repository root:
uv run month-03/week-10/join_population.py

## What I found
The ward population data helped me understand how population information is organized by ward. The health facilities map shows the distribution of health facilities across different wards and helps me understand their spatial locations.

## What went wrong and how I fixed it
Some ward names did not match between the population table and the ward polygons, which caused problems during the join. I cleaned the ward names to make them match, then performed the join successfully.
