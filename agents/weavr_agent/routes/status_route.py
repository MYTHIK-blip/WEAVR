from flask import Blueprint, jsonify
import socket
import datetime
import os

status_bp = Blueprint('status', __name__)
boot_time = datetime.datetime.utcnow().isoformat()

@status_bp.route('/', methods=['GET'])
def status():
    response = {
        "agent": "weavr_agent",
        "status": "online",
        "host": socket.gethostname(),
        "ip": socket.gethostbyname(socket.gethostname()),
        "boot_time_utc": boot_time,
        "current_time_utc": datetime.datetime.utcnow().isoformat(),
        "env": os.environ.get("WEAVR_ENV", "undefined"),
        "stack": "🧵 operational"
    }
    return jsonify(response), 200
