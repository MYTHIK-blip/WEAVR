from fastapi import FastAPI
from app.agents.weavr_agent.routes.run_route import run_bp
from app.agents.weavr_agent.routes.stack_route import stack_bp
from app.agents.weavr_agent.routes.ollama_route import ollama_bp
from app.agents.weavr_agent.routes.status_route import status_bp

app = FastAPI(
    title="WEAVR Agent Core",
    description="Modular API for routes: /run, /stack, /ollama, /status",
    version="0.1.0"
)

# Include modular routers
app.include_router(run_bp, prefix="/run")
app.include_router(stack_bp, prefix="/stack")
app.include_router(ollama_bp, prefix="/ollama")
app.include_router(status_bp, prefix="/status")

@app.get("/")
def root():
    return {
        "weavr_agent": "online",
        "message": "🧠 WEAVR is listening. Routes are active.",
        "status": "OK"
    }
