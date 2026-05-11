import streamlit as st
import os

from resume_parser import extract_text_from_resume
from skill_extraction.skill_extractor import extract_skills
from skill_gap_analysis import analyze_skill_gap
from employability_score import calculate_employability_score
from job_role_suggester import suggest_job_role
from resume_improvement import improvement_suggestions


def recommend_courses(missing_skills):
    course_map = {
        "python": "Python Programming - Coursera",
        "machine learning": "Machine Learning by Andrew Ng",
        "sql": "SQL for Data Science",
        "aws": "AWS Cloud Practitioner",
        "flask": "Flask Web Development Course",
        "data science": "IBM Data Science Professional Certificate"
    }

    return {
        skill: course_map.get(
            skill.lower(),
            "Search online learning resources"
        )
        for skill in missing_skills
    }


st.title("Skill-Gap Aware Employability Assessment")

resume_file = st.file_uploader("Upload Resume PDF")
job_desc = st.text_area("Paste Job Description")

if st.button("Analyze"):

    if resume_file and job_desc:

        with open(resume_file.name, "wb") as f:
            f.write(resume_file.getbuffer())

        resume_text = extract_text_from_resume(
            resume_file.name
        )

        resume_skills = extract_skills(
            resume_text
        )

        job_skills = extract_skills(
            job_desc
        )

        matched, missing = analyze_skill_gap(
            resume_skills,
            job_skills
        )

        score = calculate_employability_score(
            matched,
            job_skills
        )

        recommendations = recommend_courses(
            missing
        )

        job_role = suggest_job_role(
            resume_skills
        )

        improvements = improvement_suggestions(
            missing
        )

        st.success(f"Employability Score: {score}%")
        st.write("Matched Skills:", matched)
        st.write("Missing Skills:", missing)
        st.write("Recommended Role:", job_role)
        st.write("Course Recommendations:", recommendations)
        st.write("Resume Improvements:", improvements)

    else:
        st.error("Upload resume and enter job description")
