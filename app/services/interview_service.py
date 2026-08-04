from app.models.question_generator import QuestionGenerator

generator = QuestionGenerator()


class InterviewService:

    @staticmethod
    def generate(
        resume_summary: str,
        jd_summary: str
    ):

        questions = generator.generate_questions(
            resume_summary,
            jd_summary
        )

        return {
            "questions": questions
        }