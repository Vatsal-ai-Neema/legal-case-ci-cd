from fastapi import APIRouter

from app.database import store
from app.models import User

router = APIRouter(prefix="/users", tags=["users"])


@router.get("", response_model=list[User])
def get_users() -> list[User]:
    return store.list_users()

