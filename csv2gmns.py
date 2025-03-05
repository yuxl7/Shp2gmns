import pandas as pd
from pyproj import Transformer

# Define file paths for input and output data
link_csv_path = "results/link.csv"  # Path to the link CSV file
node_csv_path = "results/node.csv"  # Path to the node CSV file
mapping_csv_path = "settings/bayarea_setting.csv"  # Path to the field mapping CSV
link_gmns_csv_path = "results/link_gmns.csv"  # Output path for GMNS-compatible link file
node_gmns_csv_path = "results/node_gmns.csv"  # Output path for GMNS-compatible node file

# Load input CSV files
link_df = pd.read_csv(link_csv_path)
node_df = pd.read_csv(node_csv_path)
mapping_df = pd.read_csv(mapping_csv_path)

# Define coordinate transformation from EPSG:2227 (California State Plane) to EPSG:4326 (WGS 84)
transformer = Transformer.from_crs("EPSG:2227", "EPSG:4326", always_xy=True)

# Apply coordinate transformation to node data
node_df[['lon', 'lat']] = node_df.apply(lambda row: pd.Series(transformer.transform(row['X'], row['Y'])), axis=1)

# Update the X and Y fields with transformed coordinates
node_df['X'] = node_df['lon']
node_df['Y'] = node_df['lat']

# Remove temporary columns after transformation
node_df.drop(columns=['lon', 'lat'], inplace=True)

# Filter mapping definitions for links and nodes
link_mapping_df = mapping_df[mapping_df['section'].str.lower() == 'link']
node_mapping_df = mapping_df[mapping_df['section'].str.lower() == 'node']

# Create dictionaries mapping original CSV column names to GMNS-compliant names
link_mapping = dict(zip(link_mapping_df['csv_field_name'], link_mapping_df['gmns_field_name']))
node_mapping = dict(zip(node_mapping_df['csv_field_name'], node_mapping_df['gmns_field_name']))

# Rename columns based on mapping
link_df.rename(columns=link_mapping, inplace=True)
node_df.rename(columns=node_mapping, inplace=True)

# Extract GMNS column names for links and nodes
link_gmns_columns = link_mapping_df['gmns_field_name'].tolist()
node_gmns_columns = node_mapping_df['gmns_field_name'].tolist()

# Ensure all required GMNS fields exist in the DataFrame
for col in link_gmns_columns:
    if col not in link_df.columns:
        link_df[col] = None  # Add missing columns with null values

for col in node_gmns_columns:
    if col not in node_df.columns:
        node_df[col] = None  # Add missing columns with null values

# Reorder columns to match GMNS specification
link_df = link_df[link_gmns_columns]
node_df = node_df[node_gmns_columns]

# Save the transformed data to GMNS-compatible CSV files
link_df.to_csv(link_gmns_csv_path, index=False)
node_df.to_csv(node_gmns_csv_path, index=False)

print("Done!")
