import requests
import json
from datetime import datetime

BACKEND_URL = "http://127.0.0.1:8000/sensor/alert"

def send_motion_alert(zone: str, lat: float, lng: float):
    payload = {
        "zone": zone,
        "lat": lat,
        "lng": lng,
        "timestamp": datetime.utcnow().isoformat(),
        "message": f"Motion detected in {zone}"
    }
    
    response = requests.post(BACKEND_URL, json=payload)
    print(f"Sent alert: {response.status_code} — {response.json()}")

if __name__ == "__main__":
    send_motion_alert("Front Gate", -26.2041, 28.0473)