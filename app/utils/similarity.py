from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


class Similarity:

    @staticmethod
    def calculate_similarity(vec1, vec2):

        similarity = cosine_similarity(
            np.array(vec1).reshape(1, -1),
            np.array(vec2).reshape(1, -1)
        )

        return float(similarity[0][0])