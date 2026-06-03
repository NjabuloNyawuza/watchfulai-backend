import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()

TWILIO_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP = os.getenv("TWILIO_WHATSAPP_FROM")  # e.g. whatsapp:+14155238886
ALERT_RECIPIENT = os.getenv("ALERT_RECIPIENT")        # your number e.g. whatsapp:+27660349195

def send_cluster_alert(cluster: list):
    client = Client(TWILIO_SID, TWILIO_TOKEN)

    count = len(cluster)
    labels = [r["label"] for r in cluster]
    location = cluster[0]["location_name"]
    messages = [r["message"][:60] for r in cluster]

    dominant = "EMERGENCY" if "EMERGENCY" in labels else "SUSPICIOUS"

    body = f"""🚨 *WatchfulAI Cluster Alert*

{count} {dominant} reports detected within 200m in the last 2 hours.

📍 Area: {location}
🔺 Threat level: {dominant}

Reports:
""" + "\n".join([f"• {m}" for m in messages]) + f"""

⚙️ Detected by: Haversine clustering (200m radius, 2hr window)
🤖 Classified by: WatchfulAI keyword engine
"""

    message = client.messages.create(
        from_=TWILIO_WHATSAPP,
        to=ALERT_RECIPIENT,
        body=body
    )

    print(f"Alert sent: {message.sid}")
    return message.sid