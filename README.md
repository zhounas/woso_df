# EDF Building Data Knowledge Graph

This repository contains **scripts**, **data**, and **results** for constructing a **Knowledge Graph (KG)** from **building energy simulation** and **IoT sensor data** for an EDF building. The project aims to **semantically integrate simulation results with IoT data** to gain deeper insights into building performance, with a focus on **Zone 107**.

---

## Folder Structure

- `EDF building data KG v1.ipynb` - Jupyter notebook that constructs and processes the building Knowledge Graph.

- `credentials.py` - Contains **dummy authentication data** for demonstration purposes. Replace with your actual credentials as needed.

- `Data/`  
  - `iot_and_simulation_locations_mapping.csv`- Mapping between the location og the IoT devices and simulation zones in CSV format. 
  - `iot_locations.csv` - The location of the IoT devices in CSV format.  
  - `simulation data with input and outputs of zone 107.json` - Simulation data of Zone 107 in JSON format .  
  - `simulation_data.json` - Simulation data after the preprocessing data step in JSON format.  
  - `simulation_locations.csv` - The location of the simulation zones in CSV format. 
  - `transformed_iot_data.json` - IoT data after the preprocessing data step in  JSON format.  
  - `Zone107.json` - The structure of the Zone 107 .

- `fmuAPI/`  
  - `fmuAPI.py` – Python interface for FMU-based simulations.  
  - `README.md` – Usage guide of the FMU API.  
  - `simulate.html` – Optional web interface or viewer for simulations.

- `Results/` - Output KG files in RDF Turtle format.
  - `Building/`
    - `EDF_building_data_KG.ttl` - KG that include retrieved IoT and simulation data.
    - `EDF_building_data_KG_updated.ttl` - KG including retrieved IoT and simulation data after running the SPARQL query.
    - `EDF_building_data_KG_with_outputs.ttl` - KG including retrieved IoT and simulation data, SPARQL query results and simulation outputs.
  - `Zone107/`  
    - `EDF_building_data_KG_Z107.ttl`  - KG that include retrieved IoT and simulation data.
    - `EDF_building_data_KG_Z107_updated.ttl`  - KG including retrieved IoT and simulation data after running the SPARQL query.
    - `EDF_building_data_KG_Z107_with_outputs.ttl` - KG including retrieved IoT and simulation data, SPARQL query results and simulation outputs.

---
### Notes

- **Dummy authentication data**  is provided for demonstration purposes and should be replace with real API keys or config parameters as needed.
- The **simulation model of the EDF building is not included**  for confidentiality issues and should not be shared publicly.

---