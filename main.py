from fastapi import FastAPI

app = FastAPI(title="WatchfulAI Backend")

@app.get("/")
def health():
    return {"status": "WatchfulAI is running"}