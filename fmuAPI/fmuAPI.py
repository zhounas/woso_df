from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from fmpy import simulate_fmu
import os
import tempfile
import shutil
import numpy as np
import pandas as pd
import uuid

app = FastAPI()

results_dir = "results"
os.makedirs(results_dir, exist_ok=True)
app.mount("/results", StaticFiles(directory=results_dir), name="results")

class SimulateRequest(BaseModel):
    fmu_path: str = Field(..., description="Path to the FMU file")
    fmi_type: str = Field(..., description="FMI type: ModelExchange or CoSimulation")

    start_time: Optional[float] = Field(None, description="Simulation start time")
    stop_time: Optional[float] = Field(None, description="Simulation stop time")
    step_size: Optional[float] = Field(None, description="Optional communication step size")
    output_interval: Optional[float] = Field(None, description="Optional output interval")

    start_values: Optional[Dict[str, Any]] = Field(None, description="Optional start values as dict")
    input_array: Optional[Dict[str, Any]] = Field(None, description="Optional input array as dict")

def convert_dict_to_numpy(d: Dict[str, Any]) -> Dict[str, np.ndarray]:
    return {key: np.array(val) for key, val in d.items()}

@app.get("/", response_class=HTMLResponse)
def serve_form():
    html_path = "simulate.html"  # HTML form path
    if not os.path.isfile(html_path):
        return HTMLResponse(content="<h2>HTML form not found</h2>", status_code=404)
    with open(html_path, "r") as f:
        return f.read()

@app.post("/simulate")
async def simulate(payload: SimulateRequest):
    if not os.path.isfile(payload.fmu_path):
        raise HTTPException(status_code=404, detail="FMU file not found")

    temp_dir = tempfile.mkdtemp()

    try:
        simulate_args = {
            "filename": payload.fmu_path,
            "fmi_type": payload.fmi_type,
        }

        if payload.start_time:
            simulate_args["start_time"] = payload.start_time
        if payload.stop_time:
            simulate_args["stop_time"] = payload.stop_time
        if payload.step_size:
            simulate_args["step_size"] = payload.step_size
        if payload.output_interval:
            simulate_args["output_interval"] = payload.output_interval

        if payload.start_values:
            simulate_args["start_values"] = convert_dict_to_numpy(payload.start_values)
        if payload.input_array:
            simulate_args["input"] = convert_dict_to_numpy(payload.input_array)

        result = simulate_fmu(**simulate_args)

        # Prepare CSV file path
        unique_id = uuid.uuid4().hex
        csv_filename = f"simulation_{unique_id}.csv"
        csv_path = os.path.join(results_dir, csv_filename)

        # Write simulation result to CSV
        df = pd.DataFrame(result)
        df.to_csv(csv_path, sep=';',index=False)

        return JSONResponse(
            content={
                "message": "Simulation successful",
                "csv_url": f"/results/{csv_filename}"
            }
        )

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

    finally:
        shutil.rmtree(temp_dir)
#to run : uvicorn fmuAPI:app --reload