from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# LOAD MODEL
model = SentenceTransformer(
    'all-MiniLM-L6-v2'
)

def calculate_similarity(
    job_description,
    resume_text
):

    # CONVERT TEXT TO EMBEDDINGS
    job_embedding = model.encode(
        [job_description]
    )

    resume_embedding = model.encode(
        [resume_text]
    )

    # CALCULATE COSINE SIMILARITY
    similarity = cosine_similarity(
        job_embedding,
        resume_embedding
    )

    score = similarity[0][0] * 100

    return round(score, 2)