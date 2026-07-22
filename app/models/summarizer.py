from transformers import pipeline


class ResumeSummarizer:
    def __init__(self):
        self.summarizer = pipeline(
            task="text2text-generation",
            model="google/flan-t5-small"
        )

    def summarize(self, text: str) -> str:
        prompt = (
            "Summarize the following resume professionally. "
            "Highlight the candidate's experience, skills, education, "
            "and key achievements.\n\n"
            f"{text}"
        )

        result = self.summarizer(
            prompt,
            max_new_tokens=150,
            do_sample=False
        )

        return result[0]["generated_text"]