from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


def load_embedding_model():

    model = SentenceTransformer(
        "BAAI/bge-small-en-v1.5"
    )

    return model


def get_embeddings(model, texts):

    return model.encode(
        texts,
        batch_size=64,
        show_progress_bar=True
    )


def calculate_similarity(jd_embedding,
                         candidate_embeddings):

    similarities = cosine_similarity(
        [jd_embedding],
        candidate_embeddings
    )[0]

    return similarities