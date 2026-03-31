from datetime import date

from app.models import CreateCaseRequest, LegalCase, User


class InMemoryStore:
    def __init__(self) -> None:
        self.users = [
            User(id=1, name="Ava Sharma", email="ava.sharma@legalapp.dev", role="admin"),
            User(id=2, name="Rohan Mehta", email="rohan.mehta@legalapp.dev", role="lawyer"),
            User(id=3, name="Nisha Patel", email="nisha.patel@legalapp.dev", role="paralegal"),
        ]
        self.cases = [
            LegalCase(
                id=1,
                title="Property Ownership Dispute",
                client_name="R.K. Estates",
                assigned_to=2,
                status="in_review",
                priority="high",
                hearing_date=date(2026, 4, 12),
            ),
            LegalCase(
                id=2,
                title="Employment Contract Review",
                client_name="Blue Orbit Labs",
                assigned_to=3,
                status="open",
                priority="medium",
                hearing_date=date(2026, 4, 20),
            ),
        ]

    def list_users(self) -> list[User]:
        return self.users

    def list_cases(self) -> list[LegalCase]:
        return self.cases

    def create_case(self, payload: CreateCaseRequest) -> LegalCase:
        case = LegalCase(id=len(self.cases) + 1, **payload.model_dump())
        self.cases.append(case)
        return case


store = InMemoryStore()

