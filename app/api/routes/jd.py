from pathlib import Path

from fastapi import APIRouter, UploadFile, File

from app.services.jd_service import JDService

router = APIRouter()

UPLOAD_FOLDER = Path("uploads/jd")
UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)


@router.post("/upload")
async def upload_jd(file: UploadFile = File(...)):

    destination = UPLOAD_FOLDER / file.filename

    with open(destination, "wb") as buffer:
        buffer.write(await file.read())

    result = JDService.parse_jd(str(destination))

    return result