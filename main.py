from fastapi import FastAPI
from routes.webhook import router as whatsapp_router
from routes.sensor import router as sensor_router

app = FastAPI(title="WatchfulAI Backend")

app.include_router(whatsapp_router, prefix="/whatsapp")
app.include_router(sensor_router, prefix="/sensor")

@app.get("/")
def health():
    return {"status": "WatchfulAI is running"}