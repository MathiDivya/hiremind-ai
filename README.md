# HireMind-AI

> Next Generation Intelligent Hiring Candidate Discovery & Ranking System with the power of Semantic Search, Behavioral Intelligence & LLM powered Recruiters' Reasoning.

## Why Choose HireMind-AI?

Conventional ATS systems have a lot of dependency on keywords and hence don't find high-potential candidates.

HireMind-AI takes care of that problem through:

- Semantic understanding rather than keyword matching.
- Engagement of recruiters and behavioral intelligence.
- Recruiter's reasoning through LLM for candidate selection.
- Explainability of recommendations for recruiters.

## System Workflow

```text
Job Description
       ↓
Text Preprocessing
       ↓
Candidate Profile Construction
       ↓
Sentence Transformer Embeddings Creation
       ↓
Semantic Search
       ↓
Behavioral Signals Analysis
       ↓
JD-Fit Score Calculation
       ↓
Hybrid Score Calculation
       ↓
Top-K Candidates Retrieval
       ↓
Groq LLM Re-Ranking
       ↓
Final Explainable Ranking
```

## Features

| Feature                 | Description                                                                                |
| ----------------------- | ------------------------------------------------------------------------------------------ |
| Semantic Search         | Finds relevant candidates using semantics instead of keywords                              |
| Hybrid Ranking          | Considers semantic similarities, behavioral signals, and JD-fits                            |
| Behavioral Intelligence | Takes into account recruiter responsiveness, profile activity, and candidates' signals        |
| LLM Re-ranking          | Uses Groq LLMs to evaluate candidates similarly to recruiters                             |
| Explainability          | Creates human-readable explanation for each recommendation                               |
| Candidate Shortlisting  | Prepares recruiter-friendly shortlisted candidates                                         |

## Repository Structure

```text
HireMind-AI/
│
├── modules/
│   ├── candidate_parser.py
│   ├── data_loader.py
│   ├── embeddings.py
│   ├── explainability.py
│   ├── jd_parser.py
│   ├── reranker.py
│   ├── scorer.py
│   └── text_builder.py
│
├── HireMind_AI.ipynb
├── app.py
├── final_submission.csv
├── explanations.csv
├── requirements.txt
├── README.md
| .gitignore
```

## Technology Stack

Python, Sentence Transformers, Scikit-learn, Pandas, NumPy, Groq API, Google Colab, Git & GitHub.
## Installation

Clone the repository:

```bash
git clone https://github.com/MathiDivya/hiremind-ai.git
cd hiremind-ai
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```
## Usage

### 1. Import Candidate and Job Data

```python
candidates = load_candidates("candidates.jsonl")
job_description = load_job_description("job_description.txt")
```

### 2. Create Semantic Embeddings

```python
candidate_embeddings = model.encode(candidates)
jd_embedding = model.encode(job_description)
```

### 3. Calculate Candidate Similarity Scores

```python
similarities = cosine_similarity(
    [jd_embedding],
    candidate_embeddings
)[0]
```

### 4. Create Hybrid Ranking

The system uses:

- Semantic Similarity Score
- Behavioral Score
- JD Fit Score

for creating the ranking of candidates.

```python
final_score = (
    0.4 * semantic_score +
    0.3 * behavior_score +
    0.3 * jd_fit_score
)
```

### 5. LLM-based Recruiter Re-ranking

Selected candidates undergo additional evaluation with the help of the Groq-powered recruiter agent.

```python
llm_output = recruiter_rerank(candidate)
```

### 6. Result

The system produces:

```text
candidate_id | rank | score | reasoning
```

## Running the Project

This project can run either via the notebook:

```text
HireMind_AI.ipynb
```

or through the command line:

```bash
python app.py
```

## Methodology

Candidates are ranked using HireMind-AI’s multi-step pipeline:

1. Textual representation of job descriptions and candidate profiles.
2. Creating embeddings using Sentence Transformers.
3. Semantic similarity between candidates and job descriptions.
4. Behavioral features like recruiter response times and platform interaction.
5. Calculating hybrid scores.
6. Reranking of top candidates by Groq-backed recruiter agents.
7. Generating explanations and rankings.

## Outputs

Produced output will be:

* Candidate shortlists ranked (`final_submission.csv`)
* Explanations of candidates (`explanations.csv`)
* Recruiter-oriented recommendations.

## Sample Output

```text
Candidate ID: CAND_0000031
Final Score : 0.841
Decision    : Strong Hire

Strengths:
✓ Experience with retrieval and ranking
✓ Product-Company experience
✓ Excellent recruiter responsiveness

Concerns:
✓ 60 day notice period
```

## Challenges Encountered

- Ability to process huge volumes of candidate data effectively.
- Creating a rating mechanism that will take into account semantics and recruiters’ behavior.
- Reduction of the number of errors that are generated because of keyword search.
- Incorporation of the LLM’s reasoning while ranking candidates consistently.
## Future Work

Vector databases such as FAISS and Pinecone, learning to rank models, real-time recruiter feedback loop, continuous re-ranking of candidates.

## Authors

Mathi Naga Sai Divya, 
Yasaswini S

Built for the Redrob Intelligent Candidate Discovery & Ranking Challenge.
