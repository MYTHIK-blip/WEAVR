from fastapi import APIRouter
import yaml
import os

router = APIRouter()

PIPELINE_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "pipeline.yaml")

@router.get("/")
def get_stack_pipeline():
    try:
        with open(PIPELINE_PATH, "r") as file:
            pipeline_data = yaml.safe_load(file)
            return {
                "status": "✅ stack pipeline loaded",
                "pipeline": pipeline_data
            }
    except FileNotFoundError:
        return {
            "status": "error",
            "message": "pipeline.yaml not found"
        }
    except yaml.YAMLError as e:
        return {
            "status": "error",
            "message": "invalid YAML format",
            "details": str(e)
        }

@router.get("/health")
def health_check():
    return {
        "health": "ok",
        "status": "running",
        "uptime_hint": "container reachable, FastAPI router functional"
    }
