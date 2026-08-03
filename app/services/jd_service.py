from app.models.summarizer import TextSummarizer
from app.utils.pdf_parser import PDFParser

summarizer = TextSummarizer()


class JDService:

    @staticmethod
    def parse_jd(file_path: str):

        jd_text = PDFParser.extract_text(file_path)

        summary = summarizer.summarize(jd_text[:2000],document_type="job_description")

        return {
            "jd_text": jd_text,
            "summary": summary
        }