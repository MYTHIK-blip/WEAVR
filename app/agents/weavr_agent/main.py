# main.py — Entrypoint for WEAVR Agent (FastAPI)

from fastapi import FastAPI
from app.agents.weavr_agent.weavr_core import app  # adjust path if needed

app = FastAPI()
app.include_router(stack_router)

@app.get("/")
def root():
    return {"message": "WEAVR agent online and breathing"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=5151, reload=False)
