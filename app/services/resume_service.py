from app.models.summarizer import ResumeSummarizer
from app.utils.pdf_parser import PDFParser

summarizer = ResumeSummarizer()


class ResumeService:

    @staticmethod
    def parse_resume(file_path: str):

        resume_text = PDFParser.extract_text(file_path)

        # Temporary limit because FLAN-T5 has a limited context window
        summary = summarizer.summarize(resume_text[:2000])

        return {
            "resume_text": resume_text,
            "summary": summary
        }