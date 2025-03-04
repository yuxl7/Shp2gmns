import pandas as pd
import geopandas as gpd

# Define the shapefile path and output CSV path
shapefile_path = "freeflow_links.shp"
csv_path = r"results\link.csv"

try:
    # Read the shapefile
    gdf = gpd.read_file(shapefile_path)

    # Convert geometry to WKT format
    gdf["geometry"] = gdf["geometry"].apply(lambda geom: geom.wkt if geom else None)

    # Save to CSV
    gdf.to_csv(csv_path, index=False)
    print(f"Converted {shapefile_path} to {csv_path} successfully.")

except Exception as e:
    print(f"Error converting {shapefile_path}: {e}")
