from fastapi import APIRouter
from pydantic import BaseModel

from app.services.interview_service import InterviewService

router = APIRouter()


class InterviewRequest(BaseModel):

    resume_summary: str

    jd_summary: str


@router.post("/generate")

def generate_questions(request: InterviewRequest):

    return InterviewService.generate(
        request.resume_summary,
        request.jd_summary
    )