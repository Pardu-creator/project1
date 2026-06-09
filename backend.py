import json
import os
import hashlib
import pdfplumber
import re

USER_FILE = "users.json"


# ---------------- USER AUTH ----------------
def load_users():
    if not os.path.exists(USER_FILE):
        return {}

    try:
        with open(USER_FILE, "r") as file:
            return json.load(file)
    except:
        return {}


def save_users(users):
    with open(USER_FILE, "w") as file:
        json.dump(users, file, indent=4)


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register_user(username, password):
    username = username.strip().lower()

    if username == "" or password == "":
        return False

    users = load_users()

    if username in users:
        return False

    users[username] = {
        "password": hash_password(password)
    }

    save_users(users)
    return True


def login_user(username, password):
    username = username.strip().lower()

    if username == "" or password == "":
        return False

    users = load_users()

    if username not in users:
        return False

    return users[username]["password"] == hash_password(password)


# ---------------- RESUME PARSER ----------------
def extract_resume_text(uploaded_file):
    text = ""

    try:
        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except:
        return ""

    return text.lower()


# ---------------- SKILL EXTRACTION ----------------
SKILLS = [
    "python", "java", "c", "c++", "sql", "mysql", "mongodb",
    "html", "css", "javascript", "react", "node js",
    "machine learning", "deep learning", "data science",
    "pandas", "numpy", "matplotlib", "tensorflow", "keras",
    "flask", "django", "streamlit", "fastapi",
    "aws", "azure", "docker", "kubernetes", "git", "github",
    "power bi", "tableau", "excel", "statistics",
    "data analysis", "nlp", "computer vision", "system design"
]


def extract_skills(text):
    found_skills = []

    for skill in SKILLS:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, text):
            found_skills.append(skill.title())

    return sorted(list(set(found_skills)))


def extract_required_skills(job_description):
    jd = job_description.lower()
    required = []

    for skill in SKILLS:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, jd):
            required.append(skill.title())

    return sorted(list(set(required)))


# ---------------- ANALYSIS ENGINE ----------------
def analyze_resume(uploaded_file, job_description):
    resume_text = extract_resume_text(uploaded_file)

    if resume_text == "":
        return {
            "error": "Unable to read resume PDF. Please upload a valid text-based PDF."
        }

    resume_skills = extract_skills(resume_text)
    required_skills = extract_required_skills(job_description)

    matched_skills = list(set(resume_skills) & set(required_skills))
    missing_skills = list(set(required_skills) - set(resume_skills))

    if len(required_skills) == 0:
        match_score = 60
    else:
        match_score = int((len(matched_skills) / len(required_skills)) * 100)

    employability_score = min(100, match_score + len(resume_skills) * 2)

    suggestions = []

    if missing_skills:
        suggestions.append("Improve these missing skills: " + ", ".join(missing_skills))
    else:
        suggestions.append("Your resume matches the job description very well.")

    if "Projects" not in resume_text.title():
        suggestions.append("Add strong real-time projects to your resume.")

    if "internship" not in resume_text:
        suggestions.append("Add internship, certification, or practical training details.")

    if "github" not in resume_text:
        suggestions.append("Add your GitHub profile and project links.")

    job_roles = suggest_jobs(resume_skills)

    return {
        "resume_skills": resume_skills,
        "required_skills": required_skills,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "match_score": match_score,
        "employability_score": employability_score,
        "suggestions": suggestions,
        "job_roles": job_roles
    }


# ---------------- JOB ROLE SUGGESTION ----------------
def suggest_jobs(skills):
    skills_lower = [s.lower() for s in skills]

    roles = []

    if "python" in skills_lower and "sql" in skills_lower:
        roles.append("Data Analyst")

    if "machine learning" in skills_lower or "data science" in skills_lower:
        roles.append("Machine Learning Engineer")

    if "flask" in skills_lower or "django" in skills_lower or "fastapi" in skills_lower:
        roles.append("Backend Developer")

    if "html" in skills_lower and "css" in skills_lower and "javascript" in skills_lower:
        roles.append("Frontend Developer")

    if "aws" in skills_lower or "docker" in skills_lower:
        roles.append("Cloud / DevOps Engineer")

    if not roles:
        roles.append("Software Developer Trainee")

    return roles
