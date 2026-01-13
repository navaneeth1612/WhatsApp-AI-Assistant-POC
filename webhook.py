from fastapi import APIRouter, Request
from app.whatsapp import send_message
from app.llm.chatgpt import chat_response
from app.voice.stt import transcribe_audio

router = APIRouter()

@router.get("/webhook")
def verify(mode: str, token: str, challenge: str):
    if token == "verify_token":
        return int(challenge)
    return "Unauthorized"

@router.post("/webhook")
async def receive(req: Request):
    data = await req.json()
    msg = data["entry"][0]["changes"][0]["value"]["messages"][0]

    if msg["type"] == "text":
        reply = chat_response(msg["text"]["body"])
        send_message(reply, msg["from"])

    elif msg["type"] == "audio":
        text = transcribe_audio(msg)
        reply = chat_response(text)
        send_message(reply, msg["from"])

    return {"ok": True}
