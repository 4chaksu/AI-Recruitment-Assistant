import whisper


class SpeechToText:

    def __init__(self):

        self.model = whisper.load_model("small")

    def transcribe(self, audio_path):

        result = self.model.transcribe(audio_path)

        return result["text"]