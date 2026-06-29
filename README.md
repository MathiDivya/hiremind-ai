# HireMind-AI

> Next Generation Intelligent Hiring Candidate Discovery & Ranking System with the power of Semantic Search, Behavioral Intelligence & LLM powered Recruiters' Reasoning.

## Why Choose HireMind-AI?

Conventional ATS systems have a lot of dependency on keywords and hence don't find high-potential candidates.

HireMind-AI takes care of that problem through:

- Semantic understanding rather than keyword matching.
- Engagement of recruiters and behavioral intelligence.
- Recruiter's reasoning through LLM for candidate selection.
- Explainability of recommendations for recruiters.

## Workflow of the System

```text
Job Description
        ↓
Text Preprocessing
        ↓
Candidate Profile Creation
        ↓
Generation of Semantic Embeddings
        ↓
Search for Semantic Similarity
        ↓
Scoring of Career Contexts
        ↓
Analysis of Behavioral Signals
        ↓
Calculation of JD-Fit Score
        ↓
Calculation of Hybrid Score
        ↓
Top-K Candidate Selection
        ↓
Groq LLM Re-ranking
```

## Features

| Feature          | Description                                           |
|------------------|-------------------------------------------------------|
| Semantic Search  | Seeks relevant candidates based on semantics, not keywords |
| Hybrid Ranking   | Utilizes a combination of semantic similarity, behavioral intelligence, and career context ranking |
| Behavioral Intelligence | Utilizes behavioral intelligence factors such as recruiter response rate, profile activity, etc. |
| LLM Re-Ranking  | Utilizes Groq-powered LLMs to score shortlisted candidates as recruiters do |
| Explainability   | Generates human-understandable explanations for every candidate recommendation |
| Candidate Shortlisting | Generates recruiter-friendly ranked candidate shortlists |

## Behavioral Intelligence

HireMind-AI leverages various behavioral measures for predicting candidate availability and likelihood of being hired.

Some of the behavioral measures are:

- Recruiters’ response rates
- Candidate profile activity
- Behavior during assessments
- Recruiters’ save or bookmark rate
- Interview completion rate
- Candidate responsiveness

The score is generated based on the Behavioral Intelligence Signals.

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

Ranking is accomplished using the multi-step methodology offered by HireMind-AI:

1. Generation of textual representations of job descriptions and candidate profiles.
2. Generation of semantic embedding with the help of Sentence Transformers.
3. Calculation of semantic similarity of candidate profiles to job descriptions.
4. Career context evaluation based on experience, job title relevance, and career progression.
5. Calculating the behavioral intelligence through recruiter’s responsiveness, profile activity, and engagement.
6. Calculation of hybrid scores based on semantic similarity, behavioral intelligence, and career context.
7. Selection of Top-K candidates for subsequent evaluation.
8. Reranking of the selected candidates with the help of Groq-powered recruiter reasoning.

### Hybrid Scoring Equation

```text
Base Score =
(0.60 × Semantic Similarity) + 
(0.20 × Production Experience) +
(0.10 × Company Relevance) +
(0.10 × Experience Alignment)

Final Score =
(Base Score × Behavioral Multiplier)
```
## Robustness

The HireMind-AI architecture is based on a pipeline ranking approach.

In cases where access to Groq APIs is not possible, the HireMind-AI model is capable of producing rankings for candidates using:

- Semantic Similarity Scoring
- Behavioral Intelligence Scoring
- Career Context and JD-Fit Scoring

The layer responsible for recruiter re-ranking using the LLM model is merely optional, and not required in any way.

Moreover, the HireMind-AI solution includes behavioral anomaly detection and scoring penalties when ranking candidates.

## Scalability

HireMind-AI adopts a two-level ranking methodology.

1. The first level utilizes a scalable hybrid search module that ranks all candidates based on their semantic similarity, behavioral intelligence, and context scores.

2. Then, the Groq-enabled recruiter agent analyzes only the top-ranked K candidates to produce a detailed explanation.

Thus, the two-step procedure allows HireMind-AI to scale to big numbers of candidates but also to leverage sophisticated LLM reasoning.

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
