from transformers import pipeline


class TextSummarizer:

    def __init__(self):
        self.pipeline = pipeline(
            "text2text-generation",
            model="google/flan-t5-small"
        )

    def summarize(self, text: str, document_type: str):

        prompts = {
            "resume": (
                "Summarize the following resume. "
                "Focus on candidate skills, experience, education, projects, and achievements.\n\n"
            ),
            "job_description": (
                "Summarize the following job description. "
                "Focus on required skills, responsibilities, qualifications, and experience.\n\n"
            )
        }

        prompt = prompts[document_type] + text

        result = self.pipeline(
            prompt,
            max_new_tokens=150,
            do_sample=False
        )

        return result[0]["generated_text"]