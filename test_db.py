from supabase import create_client

SUPABASE_URL = "https://fyiohznttsvfvmemmihj.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZ5aW9oem50dHN2ZnZtZW1taWhqIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc4MDE4MTY4NywiZXhwIjoyMDk1NzU3Njg3fQ.3dJI3gQBfFIlqhdiXQ-NXA2WF2aUBwpJUGDYG-mgaTA"

try:
    print("Connecting to Supabase...")
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
    result = supabase.table("reports").select("*").limit(1).execute()
    print("✅ Success! Connected to Supabase.")
    print(f"Reports table response: {result}")
except Exception as e:
    print(f"❌ Failed: {e}")