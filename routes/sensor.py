from fastapi import APIRouter
from pydantic import BaseModel
from database import get_db

router = APIRouter()

class SensorAlert(BaseModel):
    zone: str
    lat: float
    lng: float
    timestamp: str
    message: str

@router.post("/alert")
async def receive_sensor_alert(alert: SensorAlert):
    db = get_db()
    db.table("reports").insert({
        "source": "sensor",
        "message": alert.message,
        "label": "motion_alert",
        "confidence": 1.0,
        "lat": alert.lat,
        "lng": alert.lng,
        "location_name": alert.zone,
        "sender_hash": "sensor_dev",
    }).execute()
    
    print(f"Sensor alert stored: {alert.zone} at {alert.timestamp}")
    
    return {"status": "alert_received", "zone": alert.zone}