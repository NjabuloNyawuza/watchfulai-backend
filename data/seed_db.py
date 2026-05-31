import csv
from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))

print("Seeding database with fake reports...")

with open("data/fake_reports.csv", "r") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

success = 0
failed = 0

for row in rows:
    try:
        supabase.table("reports").insert({
            "source": "whatsapp",
            "message": row["message"],
            "label": "PENDING",
            "confidence": 0.0,
            "lat": float(row["lat"]),
            "lng": float(row["lng"]),
            "location_name": row["location_name"],
            "sender_hash": "test_seed",
            "created_at": row["timestamp"]
        }).execute()
        success += 1
    except Exception as e:
        print(f"Failed row: {e}")
        failed += 1

print(f"Done! {success} inserted, {failed} failed.")