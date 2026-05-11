from flask import Flask, render_template, request
import os

from resume_parser import extract_text_from_resume
from skill_extraction.skill_extractor import extract_skills
from skill_gap_analysis import analyze_skill_gap
from employability_score import calculate_employability_score

from job_role_suggester import suggest_job_role
from resume_improvement import improvement_suggestions


app = Flask(__name__)

UPLOAD_FOLDER = "uploads/resumes"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def recommend_courses(missing_skills):

    course_map = {
        "python": "Python Programming - Coursera",
        "machine learning": "Machine Learning by Andrew Ng",
        "sql": "SQL for Data Science",
        "aws": "AWS Cloud Practitioner",
        "flask": "Flask Web Development Course",
        "data science": "IBM Data Science Professional Certificate"
    }

    recommendations = {}

    for skill in missing_skills:
        if skill in course_map:
            recommendations[skill] = course_map[skill]
        else:
            recommendations[skill] = "Search online learning resources"

    return recommendations


@app.route("/", methods=["GET","POST"])
def index():

    score = None
    matched = []
    missing = []
    recommendations = {}
    job_role = None
    improvements = []

    if request.method == "POST":

        resume_file = request.files["resume"]
        job_desc = request.form["job_desc"]

        resume_path = os.path.join(app.config["UPLOAD_FOLDER"], resume_file.filename)
        resume_file.save(resume_path)

        resume_text = extract_text_from_resume(resume_path)

        resume_skills = extract_skills(resume_text)
        job_skills = extract_skills(job_desc)

        matched, missing = analyze_skill_gap(resume_skills, job_skills)

        score = calculate_employability_score(matched, job_skills)

        recommendations = recommend_courses(missing)

        # NEW FEATURES
        job_role = suggest_job_role(resume_skills)

        improvements = improvement_suggestions(missing)

    return render_template(
        "index.html",
        score=score,
        matched=matched,
        missing=missing,
        recommendations=recommendations,
        job_role=job_role,
        improvements=improvements
    )


if __name__ == "__main__":
    app.run(debug=True)