from routes.stack_route import router as stack_router
import uvicorn
from fastapi import FastAPI

app = FastAPI()
app.include_router(stack_router)

@app.get("/")
def root():
    return {"message": "WEAVR agent online and breathing"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5151, reload=False)
