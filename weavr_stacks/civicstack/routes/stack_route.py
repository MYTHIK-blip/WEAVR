from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def stack_root():
    return {
        "message": "Civicstack route is live and responding.",
        "stack": "weavr_stacks/civicstack"
    }
