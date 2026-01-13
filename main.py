from fastapi import FastAPI
from app.webhook import router as webhook_router

app = FastAPI(title="WhatsApp AI Assistant")

app.include_router(webhook_router)

@app.get("/")
def health():
    return {"status": "running"}
