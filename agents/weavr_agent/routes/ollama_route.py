from flask import Blueprint, request, jsonify
import requests
import os

ollama_bp = Blueprint('ollama', __name__)

# Default Ollama API location (Docker container-to-container)
OLLAMA_API = os.getenv("OLLAMA_API", "http://ollama:11434")

# Optional model aliases for clarity/flex use
MODEL_ALIASES = {
    "mistral": "mistral:latest",
    "instruct": "mistral:instruct",
    "llama3": "llama3:latest",
    "hermes": "openhermes:latest",
    "openhermes": "openhermes:latest"
}

@ollama_bp.route('/', methods=['POST'])
def ollama_query():
    data = request.get_json(silent=True) or {}
    prompt = data.get("prompt", "").strip()
    model = data.get("model", "mistral")

    if not prompt:
        return jsonify({"error": "Missing prompt."}), 400

    # Handle alias translation
    model = MODEL_ALIASES.get(model.lower(), model)

    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(f"{OLLAMA_API}/api/generate", json=payload)
        response.raise_for_status()
        result = response.json()
        return jsonify({
            "prompt": prompt,
            "model": model,
            "response": result.get("response", "")
        }), 200
    except requests.RequestException as e:
        return jsonify({
            "error": "Ollama request failed.",
            "details": str(e)
        }), 502
