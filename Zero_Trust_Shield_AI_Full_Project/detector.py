import joblib
import numpy as np

model = joblib.load("intrusion_model.pkl")

def detect(packet_size, connection_time, failed_login, request_rate, port):

    data = np.array([[
        packet_size,
        connection_time,
        failed_login,
        request_rate,
        port
    ]])

    result = model.predict(data)[0]

    return {
        "status": "Threat Detected" if result else "Normal Traffic",
        "risk": "HIGH" if result else "LOW"
    }