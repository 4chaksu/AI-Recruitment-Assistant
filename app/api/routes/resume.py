from pathlib import Path

from fastapi import APIRouter, UploadFile, File

from app.services.resume_service import ResumeService

router = APIRouter()

UPLOAD_FOLDER = Path("uploads/resumes")
UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)


@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):

    destination = UPLOAD_FOLDER / file.filename

    with open(destination, "wb") as f:
        f.write(await file.read())

    result = ResumeService.parse_resume(str(destination))

    return result