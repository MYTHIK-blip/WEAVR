from fastapi import APIRouter, Request
from datetime import datetime

router = APIRouter()

@router.post("/")
async def run_trigger(request: Request):
    data = await request.json()
    user = data.get("user", "anonymous")
    note = data.get("note", "no context provided")
    timestamp = datetime.utcnow().isoformat()

    log = {
        "status": "🧵 stackweaving initiated",
        "user": user,
        "note": note,
        "timestamp": timestamp
    }

    print(f"[RUN_TRIGGER] {log}")
    return log
