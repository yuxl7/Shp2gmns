# Shp2gmns

**Shp2gmns** is a tool designed to convert shapefiles into GMNS (Generalized Modeling Network Specification) format. This repository provides functionalities for processing geospatial network data and preparing it for transportation modeling and analysis.

---

## 🚀 Project Overview

### **Code Logic**
The core functionality of **Shp2gmns** is to **convert shapefiles into GMNS-compliant network data**. The process follows these key steps:

1. **Read Input Shapefile**  
   - The program first reads the shapefile containing road network data.
   - It extracts key attributes such as `road type`, `number of lanes`, `speed limit`, and `geometry`.

2. **Preprocessing**  
   - The extracted data is cleaned and reformatted to align with **GMNS specifications**.
   - Additional attributes are inferred if missing, and network topology is validated.

3. **Conversion to GMNS Format**  
   - The processed road network data is structured into GMNS-compatible CSV files.
   - This includes files like `nodes.csv`and `links.csv`.

4. **Output Storage**  
   - The final GMNS network files are saved in the specified output directory.
   - These files can then be used in transportation modeling tools like Cube or DTALite.

---

## 🗺 **Test Sample: Bay Area**
The `test_sample/Bay_Area/` directory contains a sample road network extracted from the **San Francisco Bay Area**. This dataset serves as a real-world example for testing the conversion pipeline.

### **Dataset Description**
- The shapefile includes **major roadways, freeways, and arterial streets** in the Bay Area.
- Attributes such as road classification, number of lanes, and speed limits are available.
- This sample demonstrates how **Shp2gmns** can handle large-scale urban road networks.

## **Configuring the Settings File for Custom Network Conversion**

The **settings file** (`bayarea_setting.csv`) is used to map fields from the input shapefile (or CSV) to GMNS-compliant formats. Users can modify this file to suit their own transportation network datasets.

---

### **📂 Settings File Structure**
The settings file consists of **three sections**:
1. **File Names**: Specifies the input shapefiles for nodes and links.
2. **Configuration Parameters**: Defines global settings such as coordinate formatting and centroid thresholds.
3. **Field Mappings**: Maps input file column names to GMNS fields.

---

### **🔹 1. Define Input Files**
In the **file_name** section, specify the shapefile names for nodes and links:

| section   | gmns_field_name | csv_field_name        |
|-----------|---------------|----------------------|
| file_name | node         | freeflow_nodes.shp  |
| file_name | link         | freeflow_links.shp  |

- **`file_name`** → Defines the file type (`node` or `link`).
- **`csv_field_name`** → Name of the input shapefile.

---

### **🔹 2. Configure Global Settings**
The **configuration section** defines key processing settings:

| section         | gmns_field_name                           | csv_field_name |
|----------------|----------------------------------------|---------------|
| configuration  | with_decimal_long_lat                  | yes           |
| configuration  | node_number_threshold_as_centroid      | 0             |
| configuration  | identify_from_node_id_and_to_node_id_based_on_geometry | no |
| configuration  | number_of_lanes_oneway_vs_twoway       | oneway        |
| configuration  | lane_capacity_vs_link_capacity         | lane          |

**Explanation of Configuration Fields:**
- **`with_decimal_long_lat`** → Use decimal degrees for latitude/longitude (set to `yes` for WGS84-based networks).
- **`node_number_threshold_as_centroid`** → Defines the threshold for treating nodes as centroids (set to `0` to disable automatic centroid creation).
- **`identify_from_node_id_and_to_node_id_based_on_geometry`** → If `yes`, the script determines `from_node_id` and `to_node_id` based on link geometry.
- **`number_of_lanes_oneway_vs_twoway`** → If `oneway`, the input dataset assumes lanes are for one direction only.
- **`lane_capacity_vs_link_capacity`** → Defines whether capacity is given per lane (`lane`) or for the entire link (`link`).

---

### **🔹 3. Map Fields from Input Files to GMNS**
Each row in the **field mapping section** maps a column in the input file (`csv_field_name`) to the corresponding GMNS field (`gmns_field_name`).

#### **🛤️ Node Field Mappings**
| section | gmns_field_name | csv_field_name |
|---------|---------------|---------------|
| node    | node_id       | N             |
| node    | zone_id       | TAZID         |
| node    | x_coord       | X             |
| node    | y_coord       | Y             |

- **`node_id`** → Unique identifier for each node.
- **`zone_id`** → Zone ID associated with the node (if applicable).
- **`x_coord, y_coord`** → Coordinates of the node.

---

#### **🚗 Link Field Mappings**
| section | gmns_field_name | csv_field_name |
|---------|---------------|---------------|
| link    | from_node_id   | A             |
| link    | to_node_id     | B             |
| link    | name          | STREET        |
| link    | link_id       | I             |
| link    | link_type     | FT            |
| link    | direction     | ONEWAY        |
| link    | length        | DISTANCE      |
| link    | lanes         | LANES         |
| link    | hourly_capacity | CAP1HR1LN    |
| link    | speed_limit   | SFF           |
| link    | free_speed    | FFS           |
| link    | capacity      | CAP           |

- **`from_node_id, to_node_id`** → Start and end nodes of the link.
- **`direction`** → Defines whether the road is one-way (`ONEWAY` field in the input).
- **`hourly_capacity`** → Capacity per lane per hour.
- **`speed_limit` / `free_speed`** → Posted speed limit and free-flow speed.

---

### **🔹 4. Define Toll and VDF (Volume-Delay Functions)**
The **toll fields** and **VDF parameters** specify cost and congestion-related information:

| section | gmns_field_name | csv_field_name |
|---------|---------------|---------------|
| link    | VDF_tollsv1   | TOLLEA_DA     |
| link    | VDF_tollsv2   | TOLLEA_S2     |
| link    | VDF_tollsv3   | TOLLEA_S3     |

- **VDF_tollsv1, VDF_tollsv2, VDF_tollsv3** → Define tolls for different vehicle classes.

---

### **🔹 5. Example: Customizing for Your Network**
If your network uses different field names, simply modify the **`csv_field_name`** values to match your input data.

#### **Example: Adjusting for a Custom Dataset**
If your dataset has:
- `Node_ID` instead of `N`
- `Latitude` and `Longitude` instead of `X, Y`

Modify the **node section** as:
```csv
node,node_id,Node_ID
node,x_coord,Longitude
node,y_coord,Latitude
