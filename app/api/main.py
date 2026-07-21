from fastapi import FastAPI

from app.api.routes.resume import router as resume_router

app = FastAPI(
    title="AI Recruitment Assistant"
)

app.include_router(
    resume_router,
    prefix="/resume",
    tags=["Resume"]
)


@app.get("/")
async def root():
    return {
        "message": "AI Recruitment Assistant"
    }