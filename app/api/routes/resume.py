from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def resume_home():
    return {
        "message": "Resume API"
    }