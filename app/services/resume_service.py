from app.utils.pdf_parser import PDFParser


class ResumeService:

    @staticmethod
    def parse_resume(file_path: str):

        text = PDFParser.extract_text(file_path)

        return {
            "text": text,
            "characters": len(text)
        }