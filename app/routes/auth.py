from fastapi import APIRouter, HTTPException, status

from app.models import LoginRequest

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login")
def login(payload: LoginRequest) -> dict[str, str]:
    if payload.username == "admin" and payload.password == "admin123":
        return {
            "message": "Login successful",
            "token": "demo-jwt-token",
        }

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid credentials",
    )

