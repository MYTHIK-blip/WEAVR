from fastapi import FastAPI
from weavr_stacks.civicstack.routes.stack_route import router as stack_router

app = FastAPI(
    title="Civicstack API",
    version="1.0.0",
    description="FastAPI replacement for Flask-based Civicstack service."
)

# Add routers
app.include_router(stack_router, prefix="/stack", tags=["stack"])

# Optional root route for healthcheck
@app.get("/")
def root():
    return {"status": "Civicstack is online"}
