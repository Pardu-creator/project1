import re

# predefined skill list
SKILL_LIST = [
    "python", "java", "c", "c++", "html", "css", "javascript",
    "machine learning", "deep learning", "data science",
    "sql", "mongodb", "aws", "flask", "django"
]

def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in SKILL_LIST:
        if re.search(r'\b' + re.escape(skill) + r'\b', text):
            found_skills.append(skill)

    return list(set(found_skills))