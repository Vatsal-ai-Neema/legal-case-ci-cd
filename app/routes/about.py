from fastapi import APIRouter

router = APIRouter(tags=["about"])


@router.get("/about")
def get_about() -> dict[str, str]:
    return {
        "project": "Legal Case CI/CD App",
        "version": "1.0.0",
        "owner": "Vatsal-ai-Neema",
        "deployment_mode": "Self-hosted CD on laptop",
    }

