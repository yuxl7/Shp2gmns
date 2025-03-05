import pandas as pd
import geopandas as gpd

# Define the input shapefile path and output CSV path
shapefile_path = "freeflow_nodes.shp"  # Path to input shapefile
csv_path = r"results\node.csv"  # Path to output CSV file

try:
    # Read the shapefile into a GeoDataFrame
    gdf = gpd.read_file(shapefile_path)

    # Convert geometry to WKT format for easy storage in CSV
    gdf["geometry"] = gdf["geometry"].apply(lambda geom: geom.wkt if geom else None)

    # Save the transformed data to CSV
    gdf.to_csv(csv_path, index=False)
    print(f"Converted {shapefile_path} to {csv_path} successfully.")

except Exception as e:
    print(f"Error converting {shapefile_path}: {e}")
