from transformers import pipeline


class QuestionGenerator:

    def __init__(self):

        self.pipeline = pipeline(
            "text2text-generation",
            model="google/flan-t5-small"
        )

    def generate_questions(
        self,
        resume_summary: str,
        jd_summary: str
    ):

        prompt = f"""
You are an experienced technical interviewer.

Candidate Resume Summary:
{resume_summary}

Job Description Summary:
{jd_summary}

Generate 10 interview questions.

The questions should cover:

1. Technical Skills
2. Projects
3. Problem Solving
4. Experience
5. Behavioural Questions

Return only the numbered questions.
"""

        result = self.pipeline(
            prompt,
            max_new_tokens=256,
            do_sample=False
        )

        return result[0]["generated_text"]