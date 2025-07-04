from fastapi import APIRouter
import socket
import os
from datetime import datetime

router = APIRouter()

boot_time = datetime.utcnow().isoformat()

@router.get("/")
def status():
    response = {
        "agent": "weavr_agent",
        "status": "online",
        "host": socket.gethostname(),
        "ip": socket.gethostbyname(socket.gethostname()),
        "boot_time_utc": boot_time,
        "current_time_utc": datetime.utcnow().isoformat(),
        "env": os.environ.get("WEAVR_ENV", "undefined"),
        "stack": "🔁 operational"
    }
    return response
