from pathlib import Path

from fastapi import APIRouter, UploadFile, File

from app.services.speech_service import SpeechService

router = APIRouter()

UPLOAD_FOLDER = Path("uploads/audio")
UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)


@router.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):

    destination = UPLOAD_FOLDER / file.filename

    with open(destination, "wb") as f:
        f.write(await file.read())

    return SpeechService.convert(str(destination))