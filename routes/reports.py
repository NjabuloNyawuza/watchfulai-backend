from fastapi import APIRouter
from database import get_db

router = APIRouter()

@router.get("/reports")
def get_reports():
    db = get_db()
    result = db.table("reports") \
        .select("*") \
        .order("created_at", desc=True) \
        .limit(200) \
        .execute()
    return result.data