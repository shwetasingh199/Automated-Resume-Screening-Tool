def extract_skills(text, skills_list):

    matched_skills = []

    for skill in skills_list:

        if skill.lower() in text.lower():

            matched_skills.append(skill)

    return matched_skills