from fastapi import APIRouter

router = APIRouter(tags=["health"])


@router.get("/health")
def health_check() -> dict[str, str]:
    return {
        "message": "Legal CI/CD App is running",
        "status": "healthy",
    }

