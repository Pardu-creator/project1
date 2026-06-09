import json
import os
import hashlib
import re
from pypdf import PdfReader


# ==========================================================
# FILE PATHS
# ==========================================================
USER_FILE = "users.json"


# ==========================================================
# USER AUTHENTICATION SYSTEM
# ==========================================================
def load_users():
    """
    Load users from users.json.
    If file does not exist, return empty dictionary.
    """
    if not os.path.exists(USER_FILE):
        return {}

    try:
        with open(USER_FILE, "r") as file:
            return json.load(file)
    except Exception:
        return {}


def save_users(users):
    """
    Save users into users.json.
    """
    with open(USER_FILE, "w") as file:
        json.dump(users, file, indent=4)


def hash_password(password):
    """
    Convert password into secure hash.
    """
    return hashlib.sha256(password.encode()).hexdigest()


def register_user(username, password):
    """
    Register new user.
    Returns True if account is created.
    Returns False if username already exists or fields are empty.
    """
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
    """
    Login existing user.
    Returns True if username and password are correct.
    """
    username = username.strip().lower()

    if username == "" or password == "":
        return False

    users = load_users()

    if username not in users:
        return False

    return users[username]["password"] == hash_password(password)


# ==========================================================
# RESUME PDF TEXT EXTRACTION USING PYPDF
# ==========================================================
def extract_resume_text(uploaded_file):
    """
    Extract text from uploaded PDF resume.
    Works with Streamlit file_uploader.
    """
    text = ""

    try:
        reader = PdfReader(uploaded_file)

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    except Exception:
        return ""

    return text.lower()


# ==========================================================
# SKILL DATABASE
# ==========================================================
SKILLS = [
    # Programming Languages
    "python",
    "java",
    "c",
    "c++",
    "javascript",
    "typescript",
    "php",
    "ruby",
    "go",
    "rust",
    "kotlin",
    "swift",

    # Web Development
    "html",
    "css",
    "react",
    "angular",
    "vue",
    "node js",
    "express js",
    "bootstrap",
    "tailwind",
    "django",
    "flask",
    "fastapi",
    "streamlit",

    # Databases
    "sql",
    "mysql",
    "postgresql",
    "mongodb",
    "sqlite",
    "oracle",
    "firebase",
    "redis",

    # Data Science
    "data science",
    "data analysis",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "statistics",
    "numpy",
    "pandas",
    "matplotlib",
    "seaborn",
    "scikit learn",
    "tensorflow",
    "keras",
    "pytorch",
    "opencv",
    "nlp",
    "computer vision",
    "power bi",
    "tableau",
    "excel",

    # Cloud / DevOps
    "aws",
    "azure",
    "google cloud",
    "gcp",
    "docker",
    "kubernetes",
    "jenkins",
    "git",
    "github",
    "gitlab",
    "linux",
    "ci cd",

    # Software Engineering
    "data structures",
    "algorithms",
    "oops",
    "object oriented programming",
    "system design",
    "api",
    "rest api",
    "microservices",
    "software testing",
    "debugging",

    # Cybersecurity
    "cyber security",
    "network security",
    "ethical hacking",
    "cryptography",

    # Soft Skills
    "communication",
    "leadership",
    "problem solving",
    "teamwork",
    "critical thinking",
    "time management"
]


# ==========================================================
# SKILL EXTRACTION
# ==========================================================
def normalize_text(text):
    """
    Clean text for better matching.
    """
    text = text.lower()
    text = text.replace("-", " ")
    text = text.replace("_", " ")
    text = re.sub(r"[^a-zA-Z0-9+#. ]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text


def extract_skills(text):
    """
    Extract known skills from resume text.
    """
    text = normalize_text(text)
    found_skills = []

    for skill in SKILLS:
        pattern = r"\b" + re.escape(skill.lower()) + r"\b"

        if re.search(pattern, text):
            found_skills.append(skill.title())

    return sorted(list(set(found_skills)))


def extract_required_skills(job_description):
    """
    Extract required skills from job description.
    """
    jd = normalize_text(job_description)
    required_skills = []

    for skill in SKILLS:
        pattern = r"\b" + re.escape(skill.lower()) + r"\b"

        if re.search(pattern, jd):
            required_skills.append(skill.title())

    return sorted(list(set(required_skills)))


# ==========================================================
# JOB ROLE SUGGESTION ENGINE
# ==========================================================
def suggest_jobs(skills):
    """
    Suggest job roles based on extracted resume skills.
    """
    skills_lower = [skill.lower() for skill in skills]

    roles = []

    if "python" in skills_lower and "sql" in skills_lower:
        roles.append("Data Analyst")

    if (
        "python" in skills_lower
        and ("machine learning" in skills_lower or "data science" in skills_lower)
    ):
        roles.append("Machine Learning Engineer")

    if (
        "deep learning" in skills_lower
        or "tensorflow" in skills_lower
        or "pytorch" in skills_lower
        or "keras" in skills_lower
    ):
        roles.append("AI Engineer")

    if (
        "html" in skills_lower
        and "css" in skills_lower
        and "javascript" in skills_lower
    ):
        roles.append("Frontend Developer")

    if (
        "flask" in skills_lower
        or "django" in skills_lower
        or "fastapi" in skills_lower
        or "node js" in skills_lower
    ):
        roles.append("Backend Developer")

    if (
        "react" in skills_lower
        or "angular" in skills_lower
        or "vue" in skills_lower
    ):
        roles.append("Web Developer")

    if (
        "aws" in skills_lower
        or "azure" in skills_lower
        or "google cloud" in skills_lower
        or "docker" in skills_lower
        or "kubernetes" in skills_lower
    ):
        roles.append("Cloud / DevOps Engineer")

    if (
        "cyber security" in skills_lower
        or "network security" in skills_lower
        or "ethical hacking" in skills_lower
    ):
        roles.append("Cyber Security Analyst")

    if (
        "power bi" in skills_lower
        or "tableau" in skills_lower
        or "excel" in skills_lower
    ):
        roles.append("Business Intelligence Analyst")

    if not roles:
        roles.append("Software Developer Trainee")

    return sorted(list(set(roles)))


# ==========================================================
# EMPLOYABILITY SCORE ENGINE
# ==========================================================
def calculate_employability_score(resume_skills, required_skills, matched_skills, missing_skills):
    """
    Calculate employability score using multiple factors.
    """
    if len(required_skills) == 0:
        skill_match_score = 60
    else:
        skill_match_score = int((len(matched_skills) / len(required_skills)) * 100)

    skill_strength_score = min(100, len(resume_skills) * 5)

    penalty = len(missing_skills) * 4

    final_score = int((skill_match_score * 0.7) + (skill_strength_score * 0.3) - penalty)

    if final_score < 0:
        final_score = 0

    if final_score > 100:
        final_score = 100

    return final_score


# ==========================================================
# RESUME IMPROVEMENT SUGGESTIONS
# ==========================================================
def generate_suggestions(resume_text, missing_skills):
    """
    Generate resume improvement suggestions.
    """
    suggestions = []

    if missing_skills:
        suggestions.append(
            "Improve these missing skills: " + ", ".join(missing_skills)
        )
    else:
        suggestions.append(
            "Your resume has good skill alignment with the job description."
        )

    if "project" not in resume_text and "projects" not in resume_text:
        suggestions.append(
            "Add at least 2 to 3 strong projects related to your target job role."
        )

    if "internship" not in resume_text:
        suggestions.append(
            "Add internship, training, certification, or practical experience details."
        )

    if "github" not in resume_text:
        suggestions.append(
            "Add your GitHub profile link and project repository links."
        )

    if "linkedin" not in resume_text:
        suggestions.append(
            "Add your LinkedIn profile for better professional visibility."
        )

    if "achievement" not in resume_text and "achievements" not in resume_text:
        suggestions.append(
            "Add achievements, certifications, hackathons, workshops, or awards."
        )

    if "sql" not in resume_text:
        suggestions.append(
            "Add SQL knowledge because it is important for most data and software roles."
        )

    if "communication" not in resume_text:
        suggestions.append(
            "Mention communication, teamwork, and problem-solving skills."
        )

    return suggestions


# ==========================================================
# LEARNING ROADMAP GENERATOR
# ==========================================================
def generate_learning_roadmap(missing_skills):
    """
    Generate weekly learning roadmap from missing skills.
    """
    roadmap = []

    if not missing_skills:
        roadmap.append({
            "week": "Week 1",
            "skill": "Advanced Projects",
            "task": "Build one real-time project and add it to GitHub."
        })

        roadmap.append({
            "week": "Week 2",
            "skill": "Interview Preparation",
            "task": "Practice aptitude, coding, resume explanation, and mock interviews."
        })

        return roadmap

    for index, skill in enumerate(missing_skills, start=1):
        roadmap.append({
            "week": f"Week {index}",
            "skill": skill,
            "task": f"Learn {skill}, practice basics, and build one mini project using {skill}."
        })

    roadmap.append({
        "week": "Final Week",
        "skill": "Resume Upgrade",
        "task": "Update resume with new skills, GitHub links, project details, and deployment links."
    })

    return roadmap


# ==========================================================
# MAIN RESUME ANALYSIS FUNCTION
# ==========================================================
def analyze_resume(uploaded_file, job_description):
    """
    Main function called from app.py.
    Returns complete analysis result.
    """
    resume_text = extract_resume_text(uploaded_file)

    if resume_text == "":
        return {
            "error": "Unable to read resume PDF. Please upload a valid text-based PDF."
        }

    resume_skills = extract_skills(resume_text)
    required_skills = extract_required_skills(job_description)

    matched_skills = sorted(list(set(resume_skills) & set(required_skills)))
    missing_skills = sorted(list(set(required_skills) - set(resume_skills)))

    if len(required_skills) == 0:
        match_score = 60
    else:
        match_score = int((len(matched_skills) / len(required_skills)) * 100)

    employability_score = calculate_employability_score(
        resume_skills,
        required_skills,
        matched_skills,
        missing_skills
    )

    suggestions = generate_suggestions(resume_text, missing_skills)

    job_roles = suggest_jobs(resume_skills)

    roadmap = generate_learning_roadmap(missing_skills)

    return {
        "resume_text": resume_text,
        "resume_skills": resume_skills,
        "required_skills": required_skills,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "match_score": match_score,
        "employability_score": employability_score,
        "suggestions": suggestions,
        "job_roles": job_roles,
        "roadmap": roadmap
    }
