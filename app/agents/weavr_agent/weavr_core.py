from fastapi import FastAPI
from app.agents.weavr_agent.routes.run_route import router as run_router
from app.agents.weavr_agent.routes.stack_route import router as stack_router
from app.agents.weavr_agent.routes.ollama_route import router as ollama_router
from app.agents.weavr_agent.routes.status_route import router as status_router

app = FastAPI(
    title="WEAVR Agent Core",
    description="Modular civic deployment agent for stack weaving.",
    version="1.0.0"
)

# Include modular routers
app.include_router(run_router, prefix="/run", tags=["run"])
app.include_router(stack_router, prefix="/stack", tags=["stack"])
app.include_router(ollama_router, prefix="/ollama", tags=["ollama"])
app.include_router(status_router, prefix="/status", tags=["status"])

@app.get("/")
def root():
    return {
        "weavr_agent": "online",
        "message": "🧠🕸️ operational",
        "status": "OK"
    }
