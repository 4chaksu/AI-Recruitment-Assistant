from fastapi import FastAPI

from app.api.routes.resume import router as resume_router
from app.api.routes.jd import router as jd_router

app = FastAPI(
    title="AI Recruitment Assistant",
    version="1.0.0"
)

app.include_router(
    resume_router,
    prefix="/resume",
    tags=["Resume"]
)

app.include_router(
    jd_router,
    prefix="/jd",
    tags=["Job Description"]
)


@app.get("/")
async def root():
    return {
        "message": "AI Recruitment Assistant API"
    }