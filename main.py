from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
history = []

class Metrics(BaseModel):
    cpu: float
    ram: float
    disk: float

@app.post("/metrics")
def receive_metrics(m: Metrics):
    print(m)
    history.append(m)
    return {"status": "ok"}

@app.get("/metrics/latest")
def get_latest():
    if not history:
        raise HTTPException(status_code=404, detail="No metrics found")
    return history[-1]
