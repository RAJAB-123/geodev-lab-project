
import csv
def inspect_column(Dar_es_salaam, column):
    with open(Dar_es_salaam, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    values = []
    for row in rows:
        raw = row[column].strip()
        if raw == "":
            continue
        values.append(float(raw))
    return {
        "smallest": min(values),
        "largest": max(values),
        "count": len(values),
    }
area_result = inspect_column("Dar_es_salaam.csv", "area_km2")
print("Area:", area_result)