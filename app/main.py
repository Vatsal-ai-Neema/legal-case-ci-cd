from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.routes import about, auth, cases, health, users

app = FastAPI(title="Legal Case CI/CD App", version="1.0.0")

app.include_router(health.router)
app.include_router(about.router)
app.include_router(users.router)
app.include_router(cases.router)
app.include_router(auth.router)

BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/", include_in_schema=False)
def serve_frontend() -> FileResponse:
    return FileResponse(STATIC_DIR / "index.html")
