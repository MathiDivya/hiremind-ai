service_companies = [

    "TCS",
    "Infosys",
    "Wipro",
    "Accenture",
    "Cognizant",
    "Capgemini"
]


def production_score(candidate):

    keywords = [

        "retrieval",
        "ranking",
        "recommendation",
        "embeddings",
        "production",
        "pipeline",
        "evaluation",
        "search",
        "vector",
        "real-time"
    ]

    text = str(candidate).lower()

    count = 0

    for word in keywords:

        if word in text:
            count += 1

    return count / len(keywords)


def behavior_score(candidate):

    s = candidate["redrob_signals"]

    open_to_work = 1 if s["open_to_work_flag"] else 0

    recruiter = min(
        s["recruiter_response_rate"], 1
    )

    interview = min(
        s["interview_completion_rate"], 1
    )

    github = min(
        s["github_activity_score"] / 10, 1
    )

    score = (

        0.25 * open_to_work +
        0.25 * recruiter +
        0.25 * interview +
        0.25 * github
    )

    return min(score, 1)


def company_score(candidate):

    score = 0

    for job in candidate["career_history"]:

        if job["company"] not in service_companies:
            score += 1

    return min(score / 3, 1)


def experience_score(candidate):

    exp = candidate["profile"][
        "years_of_experience"
    ]

    if 5 <= exp <= 9:
        return 1

    elif exp > 9:
        return 0.8

    return exp / 5