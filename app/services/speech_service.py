from app.models.speech_to_text import SpeechToText

speech_model = SpeechToText()


class SpeechService:

    @staticmethod
    def convert(audio_path: str):

        transcript = speech_model.transcribe(audio_path)

        return {
            "transcript": transcript
        }