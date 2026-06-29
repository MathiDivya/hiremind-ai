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

## Behavioral Intelligence

HireMind-AI utilizes various behavioral factors in estimating the availability of the candidate and the likelihood of the recruitment process.

Some of the behavioral signals include:

- Response rates of recruiters
- Activity level of profiles
- Assessment behavior
- Save/bookmark frequency by recruiters
- Interview completion rate
- Responsiveness of candidates
- Platform engagement signals

The signals are combined to form the behavioral intelligence score.

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

Ranking is performed via HireMind-AI’s multi-staged pipeline:

1. Creating text representations of job descriptions and candidate profiles.
2. Computing semantic embeddings using Sentence Transformers.
3. Computing semantic similarity between candidate profiles and job descriptions.
4. Performing career-context evaluation considering number of years of experience, job title similarity, and career progression.
5. Calculating behavioral intelligence using responsiveness, activity, and engagement of the candidate profile by recruiters.
6. Computing hybrid score based on the combination of semantic similarity, behavioral intelligence, and JD-Fit scores.
7. Selecting Top-K candidates for evaluation.
8. Re-ranking selected candidates with the help of Groq-powered recruiter reasoning.
9. Generating explainable recommendations.

### Hybrid Scoring Formula

```text
Final Score = 
0.4 x Semantic Similarity + 
0.3 x Behavioral Score + 
0.3 x JD-Fit Score
```
## Robustness

HireMind-AI is built on the principle of a multistep ranking pipeline.

In cases where access to Groq APIs is not possible, HireMind-AI will be able to independently generate a set of rankings based on:

- Semantic Similarity Score
- Behavioral Intelligence Score
- Career Context & JD-Fit Scores

The re-ranking by an LLM-based recruiter works as a supplementary step rather than a necessity.

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
