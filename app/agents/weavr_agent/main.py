from fastapi import FastAPI
from app.agents.weavr_agent.weavr_core import app as core_app

# Entrypoint App
app = FastAPI()

# Mount the core app routes
app.mount("/", core_app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.agents.weavr_agent.main:app", host="0.0.0.0", port=5151, reload=False)
