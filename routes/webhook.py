from fastapi import APIRouter, Request
from services.classifier import classify_report
from database import get_db
import hashlib

router = APIRouter()

def anonymise(phone: str) -> str:
    return hashlib.sha256(phone.encode()).hexdigest()[:12]

@router.post("/incoming")
async def whatsapp_incoming(request: Request):
    form = await request.form()
    
    message = form.get("Body", "").strip()
    sender = form.get("From", "")
    
    if not message:
        return {"status": "ignored", "reason": "empty message"}
    
    # Classify the message
    result = classify_report(message)
    
    # Store in Supabase
    db = get_db()
    db.table("reports").insert({
        "source": "whatsapp",
        "message": message,
        "label": result["label"],
        "confidence": result["confidence"],
        "lat": -26.2041,
        "lng": 28.0473,
        "location_name": "Unknown — WhatsApp report",
        "sender_hash": anonymise(sender),
    }).execute()
    
    print(f"Stored: {result['label']} ({result['confidence']}) — {message[:50]}")
    
    return {"status": "received", "label": result["label"], "confidence": result["confidence"]}