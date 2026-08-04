from fastapi import FastAPI

from app.api.routes.resume import router as resume_router
from app.api.routes.jd import router as jd_router
from app.api.routes.matching import router as matching_router
from app.api.routes.interview import router as interview_router
from app.api.routes.speech import router as speech_router


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

app.include_router(
    matching_router,
    prefix="/match",
    tags=["Matching"]
)

app.include_router(
    interview_router,
    prefix="/interview",
    tags=["Interview"]
)

app.include_router(
    speech_router,
    prefix="/speech",
    tags=["Speech"]
)


@app.get("/")
async def root():
    return {
        "message": "AI Recruitment Assistant API"
    }