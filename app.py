from modules.data_loader import (
    load_candidates,
    load_job_description
)

from modules.text_builder import (
    create_candidate_text
)

from modules.embeddings import (
    load_embedding_model,
    get_embeddings,
    calculate_similarity
)

from modules.scorer import (
    production_score,
    behavior_score,
    company_score,
    experience_score
)

import pandas as pd


print("Loading candidates...")

candidates = load_candidates(
    "data/raw/[PUB] India_runs_data_and_ai_challenge/India_runs_data_and_ai_challenge/candidates.jsonl"
)

candidates = candidates[:10]

print("Loading JD...")

jd = load_job_description(
    "data/raw/[PUB] India_runs_data_and_ai_challenge/India_runs_data_and_ai_challenge/job_description.docx"
)

print("Creating candidate texts...")

candidate_texts = []

for candidate in candidates:
    candidate_texts.append(
        create_candidate_text(candidate)
    )

print("Loading embedding model...")

model = load_embedding_model()

print("Generating embeddings...")

candidate_embeddings = get_embeddings(
    model,
    candidate_texts
)

jd_embedding = model.encode(jd)

print("Calculating similarity...")

similarities = calculate_similarity(
    jd_embedding,
    candidate_embeddings
)

print("Calculating final scores...")

results = []

for idx, candidate in enumerate(candidates):

    semantic_score = similarities[idx]

    prod_score = production_score(candidate)

    beh_score = behavior_score(candidate)

    comp_score = company_score(candidate)

    exp_score = experience_score(candidate)

    final_score = (

            0.45 * semantic_score +

            0.20 * prod_score +

            0.15 * beh_score +

            0.10 * comp_score +

            0.10 * exp_score
    )

    results.append({

        "candidate_id":
            candidate["candidate_id"],

        "semantic_score":
            semantic_score,

        "production_score":
            prod_score,

        "behavior_score":
            beh_score,

        "company_score":
            comp_score,

        "experience_score":
            exp_score,

        "final_score":
            final_score
    })

print("Sorting candidates...")

results = sorted(
    results,
    key=lambda x: x["final_score"],
    reverse=True
)

df = pd.DataFrame(results)

print(df.head(10))

df.to_csv(
    "data/outputs/ranked_candidates.csv",
    index=False
)

print(
    "Ranking saved successfully!"
)