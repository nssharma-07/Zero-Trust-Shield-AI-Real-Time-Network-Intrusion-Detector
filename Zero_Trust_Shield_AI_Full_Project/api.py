from fastapi import FastAPI
from pydantic import BaseModel
from detector import detect

app = FastAPI(title="Zero-Trust Shield AI")

class NetworkData(BaseModel):
    packet_size:int
    connection_time:int
    failed_login:int
    request_rate:int
    port:int

@app.get("/")
def home():
    return {"message":"Zero-Trust Shield AI running"}

@app.post("/detect")
def detection(data:NetworkData):
    return detect(
        data.packet_size,
        data.connection_time,
        data.failed_login,
        data.request_rate,
        data.port
    )