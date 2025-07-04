from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
import os
import requests

router = APIRouter()

OLLAMA_API = os.getenv("OLLAMA_API", "http://ollama:11434")

MODEL_ALIASES = {
    "mistral": "mistral:latest",
    "instruct": "mistral:instruct",
    "llama3": "llama3:latest",
    "hermes": "openhermes:latest",
    "openhermes": "openhermes:latest"
}

class PromptRequest(BaseModel):
    prompt: str
    model: Optional[str] = "mistral"

@router.post("/")
async def ollama_query(data: PromptRequest):
    model = MODEL_ALIASES.get(data.model.lower(), data.model)
    payload = {
        "model": model,
        "prompt": data.prompt,
        "stream": False
    }

    try:
        response = requests.post(f"{OLLAMA_API}/api/generate", json=payload)
        response.raise_for_status()
        result = response.json()
        return {
            "prompt": data.prompt,
            "model": model,
            "response": result.get("response", "")
        }
    except requests.RequestException as e:
        raise HTTPException(status_code=502, detail=f"Ollama request failed: {str(e)}")
