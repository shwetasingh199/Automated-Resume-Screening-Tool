def analyze_skills(
    matched_skills,
    required_skills
):

    missing_skills = []

    for skill in required_skills:

        if skill not in matched_skills:

            missing_skills.append(skill)

    match_percentage = (
        len(matched_skills)
        /
        len(required_skills)
    ) * 100

    return {

        "matched": matched_skills,

        "missing": missing_skills,

        "match_percentage": round(
            match_percentage,
            2
        )
    }