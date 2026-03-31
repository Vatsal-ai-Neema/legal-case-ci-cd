from fastapi import APIRouter, status

from app.database import store
from app.models import CreateCaseRequest, LegalCase

router = APIRouter(prefix="/cases", tags=["cases"])


@router.get("", response_model=list[LegalCase])
def get_cases() -> list[LegalCase]:
    return store.list_cases()


@router.post("", response_model=LegalCase, status_code=status.HTTP_201_CREATED)
def create_case(payload: CreateCaseRequest) -> LegalCase:
    return store.create_case(payload)

