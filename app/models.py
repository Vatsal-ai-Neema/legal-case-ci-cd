from datetime import date
from typing import Literal

from pydantic import BaseModel


CaseStatus = Literal["open", "in_review", "closed"]
CasePriority = Literal["low", "medium", "high"]


class User(BaseModel):
    id: int
    name: str
    email: str
    role: str


class LegalCase(BaseModel):
    id: int
    title: str
    client_name: str
    assigned_to: int
    status: CaseStatus
    priority: CasePriority
    hearing_date: date


class CreateCaseRequest(BaseModel):
    title: str
    client_name: str
    assigned_to: int
    status: CaseStatus = "open"
    priority: CasePriority = "medium"
    hearing_date: date


class LoginRequest(BaseModel):
    username: str
    password: str
