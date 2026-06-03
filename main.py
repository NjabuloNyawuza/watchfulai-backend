from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.webhook import router as whatsapp_router
from routes.sensor import router as sensor_router
from routes.reports import router as reports_router

app = FastAPI(title="WatchfulAI Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(whatsapp_router, prefix="/whatsapp")
app.include_router(sensor_router, prefix="/sensor")
app.include_router(reports_router)

@app.get("/")
def health():
    return {"status": "WatchfulAI is running"}