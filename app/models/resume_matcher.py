from sentence_transformers import SentenceTransformer


class ResumeMatcher:

    def __init__(self):
        self.model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )

    def generate_embedding(self, text: str):

        embedding = self.model.encode(
            text,
            convert_to_tensor=False
        )

        return embedding