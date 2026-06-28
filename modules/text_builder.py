def create_candidate_text(candidate):

    text = ""

    profile = candidate.get("profile", {})

    text += profile.get("headline", "") + " "
    text += profile.get("summary", "") + " "

    for skill in candidate.get("skills", []):
        text += skill.get("name", "") + " "

    for job in candidate.get("career_history", []):

        text += job.get("title", "") + " "
        text += job.get("industry", "") + " "
        text += job.get("description", "") + " "

    return text