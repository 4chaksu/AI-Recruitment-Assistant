from app.models.resume_matcher import ResumeMatcher
from app.utils.similarity import Similarity

matcher = ResumeMatcher()


class MatchingService:

    @staticmethod
    def match(resume_text: str, jd_text: str):

        resume_embedding = matcher.generate_embedding(resume_text)

        jd_embedding = matcher.generate_embedding(jd_text)

        score = Similarity.calculate_similarity(
            resume_embedding,
            jd_embedding
        )

        percentage = round(score * 100, 2)

        if percentage >= 85:
            recommendation = "Highly Recommended"

        elif percentage >= 70:
            recommendation = "Recommended"

        elif percentage >= 50:
            recommendation = "Consider"

        else:
            recommendation = "Not Recommended"

        return {
            "match_score": percentage,
            "recommendation": recommendation
        }