
# FMU Simulation API

This project provides a RESTful API and web interface to simulate Functional Mock-up Units (FMUs) using FMPy and FastAPI.

## Features

- Simulate FMUs via API or browser form
- Accepts `start_values` and `input_array` as JSON
- Returns structured simulation results in JSON

## Requirements

```bash
pip install fastapi uvicorn fmpy
```

## Running the Application

```bash
uvicorn main:app --reload
```

Access the web interface at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## API Usage

### POST /simulate

**Query Parameters:**

- `fmu_path`: Path to FMU file (required)
- `start_time`: Start time (default: 0.0)
- `stop_time`: Stop time (required)
- `step_size`, `output_interval`, `relative_tolerance`, `timeout`, `fmi_type`: Optional settings

**JSON Body:**
```json
{
  "start_values": {
    "x": 1.0
  },
  "input_array": {
    "time": [0.0, 1.0, 2.0],
    "u": [0.0, 0.5, 1.0]
  }
}
```

**Example:**
```bash
curl -X POST "http://127.0.0.1:8000/simulate?fmu_path=/path/to/model.fmu&start_time=0&stop_time=10" \
     -H "Content-Type: application/json" \
     -d '{"start_values": {"x": 1.0}, "input_array": {"time": [0, 1], "u": [0.0, 1.0]}}'
```

## Notes

- `fmu_path` must point to an accessible FMU file on the server
- All simulation output is returned as JSON

## License

MIT License

## Acknowledgments

Built with [FastAPI](https://fastapi.tiangolo.com/) and [FMPy](https://github.com/CATIA-Systems/FMPy)
