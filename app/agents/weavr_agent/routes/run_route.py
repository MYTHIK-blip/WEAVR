from flask import Blueprint, jsonify, request
import datetime

run_bp = Blueprint('run', __name__)

@run_bp.route('/', methods=['POST'])
def run_trigger():
    data = request.get_json(silent=True) or {}

    timestamp = datetime.datetime.utcnow().isoformat()
    user = data.get("user", "anonymous")
    note = data.get("note", "no context provided")

    log = {
        "status": "🧵 stackweaving initiated",
        "user": user,
        "note": note,
        "timestamp": timestamp
    }

    print(f"[RUN_TRIGGER] {log}")
    return jsonify(log), 200
