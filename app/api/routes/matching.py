from fastapi import APIRouter
from pydantic import BaseModel

from app.services.matching_service import MatchingService

router = APIRouter()


class MatchRequest(BaseModel):

    resume_text: str

    jd_text: str


@router.post("/")

def match_candidate(request: MatchRequest):

    result = MatchingService.match(
        request.resume_text,
        request.jd_text
    )

    return result