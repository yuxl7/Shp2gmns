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
