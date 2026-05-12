import streamlit as st
import os

from resume_parser import extract_text_from_resume
from skill_extraction.skill_extractor import extract_skills
from skill_gap_analysis import analyze_skill_gap
from employability_score import calculate_employability_score
from job_role_suggester import suggest_job_role
from resume_improvement import improvement_suggestions


# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Employability Assessment",
    page_icon="🚀",
    layout="wide"
)

# ---------------- COLORFUL THEME ----------------
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #6a11cb, #2575fc);
        color: white;
    }

    .login-box {
        background: rgba(255,255,255,0.15);
        padding: 40px;
        border-radius: 20px;
        box-shadow: 0px 8px 32px rgba(0,0,0,0.3);
        backdrop-filter: blur(10px);
        text-align: center;
    }

    .stButton>button {
        background: linear-gradient(90deg,#ff512f,#dd2476);
        color: white;
        border-radius: 12px;
        font-size: 18px;
        font-weight: bold;
        width: 100%;
        padding: 12px;
        border: none;
    }

    .stTextInput>div>div>input {
        border-radius: 10px;
        padding: 12px;
    }
    </style>
""", unsafe_allow_html=True)


# ---------------- LOGIN ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


def login():
    st.markdown("<h1 style='text-align:center;'>🚀 Skill-Gap Assessment</h1>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        st.markdown('<div class="login-box">', unsafe_allow_html=True)

        st.subheader("🔐 Login")

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if username == "admin" and password == "1234":
                st.session_state.logged_in = True
                st.success("Login Successful ✅")
                st.rerun()
            else:
                st.error("Invalid Username or Password ❌")

        st.markdown("</div>", unsafe_allow_html=True)


# ---------------- COURSE RECOMMENDER ----------------
def recommend_courses(missing_skills):
    course_map = {
        "python": "Python Programming - Coursera",
        "machine learning": "Machine Learning by Andrew Ng",
        "sql": "SQL for Data Science",
        "aws": "AWS Cloud Practitioner",
        "flask": "Flask Web Development Course",
        "data science": "IBM Data Science Certificate"
    }

    return {
        skill: course_map.get(skill.lower(),
        "Search online learning resources")
        for skill in missing_skills
    }


# ---------------- MAIN APP ----------------
def main_app():
    st.title("🎯 Skill-Gap Aware Employability Assessment")

    resume_file = st.file_uploader("Upload Resume PDF")
    job_desc = st.text_area("Paste Job Description")

    if st.button("Analyze"):

        if resume_file and job_desc:

            with open(resume_file.name, "wb") as f:
                f.write(resume_file.getbuffer())

            resume_text = extract_text_from_resume(resume_file.name)

            resume_skills = extract_skills(resume_text)
            job_skills = extract_skills(job_desc)

            matched, missing = analyze_skill_gap(
                resume_skills,
                job_skills
            )

            score = calculate_employability_score(
                matched,
                job_skills
            )

            recommendations = recommend_courses(missing)

            job_role = suggest_job_role(resume_skills)

            improvements = improvement_suggestions(missing)

            st.success(f"📊 Employability Score: {score}%")
            st.write("✅ Matched Skills:", matched)
            st.write("❌ Missing Skills:", missing)
            st.write("💼 Recommended Role:", job_role)
            st.write("📚 Course Recommendations:", recommendations)
            st.write("📝 Resume Improvements:", improvements)

        else:
            st.error("Upload resume and enter job description")


# ---------------- RUN ----------------
if st.session_state.logged_in:
    main_app()
else:
    login()
