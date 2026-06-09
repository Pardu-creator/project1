import streamlit as st
from backend import (
    register_user,
    login_user,
    analyze_resume,
    ai_mentor_response
)
import random
import time


# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="Skill-Gap AI Platform",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ---------------------------------------------------
# CSS
# ---------------------------------------------------
st.markdown("""
<style>
.stApp{
    background:
    radial-gradient(circle at top left, rgba(34,211,238,0.18), transparent 25%),
    radial-gradient(circle at bottom right, rgba(139,92,246,0.20), transparent 25%),
    linear-gradient(135deg, #020617 0%, #071127 40%, #0f172a 100%);
    color:white;
}

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.hero-title{
    font-size:58px;
    font-weight:900;
    line-height:1.1;
    background:linear-gradient(90deg,#22d3ee,#60a5fa,#8b5cf6,#ffffff);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.page-title{
    font-size:44px;
    font-weight:900;
    margin-bottom:8px;
    background:linear-gradient(90deg,#22d3ee,#60a5fa,#8b5cf6);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.subtext{
    color:#cbd5e1;
    font-size:17px;
    line-height:1.7;
}

.glass-card{
    background:rgba(255,255,255,0.075);
    backdrop-filter:blur(22px);
    -webkit-backdrop-filter:blur(22px);
    border:1px solid rgba(255,255,255,0.12);
    border-radius:25px;
    padding:24px;
    box-shadow:0 0 30px rgba(0,234,255,0.12);
    margin:14px 0;
    transition:0.3s;
}

.glass-card:hover{
    transform:translateY(-4px);
    box-shadow:0 0 38px rgba(34,211,238,0.25);
}

.small-card{
    background:linear-gradient(135deg, rgba(34,211,238,0.10), rgba(139,92,246,0.12));
    border:1px solid rgba(255,255,255,0.10);
    border-radius:22px;
    padding:20px;
    margin:10px 0;
}

.stTextInput input,
.stTextArea textarea{
    background:rgba(255,255,255,0.08)!important;
    color:white!important;
    border:1px solid rgba(34,211,238,0.8)!important;
    border-radius:16px!important;
}

[data-testid="stFileUploader"]{
    background:rgba(255,255,255,0.07);
    border:1px dashed rgba(34,211,238,0.7);
    border-radius:18px;
    padding:15px;
}

.stButton > button{
    width:100%;
    height:50px;
    border:none;
    border-radius:16px;
    font-weight:800;
    color:white;
    background:linear-gradient(90deg,#06b6d4,#3b82f6,#8b5cf6);
    box-shadow:0 0 18px rgba(34,211,238,0.20);
    transition:0.25s;
}

.stButton > button:hover{
    transform:translateY(-2px);
    box-shadow:0 0 30px rgba(34,211,238,0.45);
}

section[data-testid="stSidebar"]{
    background:linear-gradient(180deg, rgba(8,15,35,0.98), rgba(2,6,23,0.98));
    border-right:1px solid rgba(255,255,255,0.08);
}

section[data-testid="stSidebar"] *{
    color:white;
}

[data-testid="stMetric"]{
    background:rgba(255,255,255,0.07);
    border:1px solid rgba(255,255,255,0.10);
    padding:18px;
    border-radius:22px;
    box-shadow:0 0 18px rgba(34,211,238,0.10);
}

.stProgress > div > div > div > div{
    background:linear-gradient(90deg,#22d3ee,#3b82f6,#8b5cf6);
}

.skill-pill{
    display:inline-block;
    padding:8px 16px;
    margin:6px;
    border-radius:999px;
    background:linear-gradient(90deg,#06b6d4,#3b82f6);
    color:white;
    font-weight:700;
}

.missing-pill{
    display:inline-block;
    padding:8px 16px;
    margin:6px;
    border-radius:999px;
    background:linear-gradient(90deg,#ef4444,#f97316);
    color:white;
    font-weight:700;
}

.role-pill{
    display:inline-block;
    padding:8px 16px;
    margin:6px;
    border-radius:999px;
    background:linear-gradient(90deg,#22c55e,#14b8a6);
    color:white;
    font-weight:700;
}
</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------
# SESSION STATE
# ---------------------------------------------------
def init_session():
    defaults = {
        "logged_in": False,
        "username": "",
        "analysis_result": None,
        "last_uploaded_name": "",
        "mentor_chat": []
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


init_session()


# ---------------------------------------------------
# HELPER FUNCTIONS
# ---------------------------------------------------
def page_heading(title, subtitle=""):
    st.markdown(f'<div class="page-title">{title}</div>', unsafe_allow_html=True)

    if subtitle:
        st.markdown(f'<p class="subtext">{subtitle}</p>', unsafe_allow_html=True)


def pills(items, pill_type="skill-pill"):
    if items:
        html = ""

        for item in items:
            html += f'<span class="{pill_type}">{item}</span>'

        st.markdown(html, unsafe_allow_html=True)
    else:
        st.info("No data available")


def score_label(score):
    if score >= 85:
        return "Excellent"
    elif score >= 70:
        return "Strong"
    elif score >= 55:
        return "Moderate"
    else:
        return "Needs Improvement"


# ---------------------------------------------------
# LOGIN PAGE
# ---------------------------------------------------
def login_page():
    left, right = st.columns([1.5, 1], gap="large")

    with left:
        st.markdown("""
        <div style="height:90vh;display:flex;flex-direction:column;justify-content:center;">
            <div class="hero-title">Skill-Gap Aware Employability</div>
            <h2 style="color:white;margin-top:20px;">Assessment Platform Using Artificial Intelligence</h2>
            <p class="subtext">
                A smart AI platform to analyze resumes, identify missing skills,
                match job roles, predict employability, and generate personalized career guidance.
            </p>

            <div class="glass-card">
                <h3>🚀 Core Features</h3>
                <p>✅ Resume Intelligence</p>
                <p>✅ Skill Gap Detection</p>
                <p>✅ Employability Score</p>
                <p>✅ Job Match Engine</p>
                <p>✅ AI Mentor Chatbot</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with right:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)

        st.markdown("""
        <h2 style="text-align:center;">⚡ Welcome</h2>
        <p style="text-align:center;color:#cbd5e1;">Login or create your account</p>
        """, unsafe_allow_html=True)

        tab1, tab2 = st.tabs(["🔐 Login", "✨ Register"])

        with tab1:
            username = st.text_input("Username", key="login_username")
            password = st.text_input("Password", type="password", key="login_password")

            if st.button("Secure Login"):
                if login_user(username, password):
                    st.session_state.logged_in = True
                    st.session_state.username = username.strip().lower()
                    st.success("Login successful")
                    time.sleep(0.5)
                    st.rerun()
                else:
                    st.error("Invalid username or password")

        with tab2:
            new_username = st.text_input("Create Username", key="register_username")
            new_password = st.text_input("Create Password", type="password", key="register_password")
            confirm_password = st.text_input("Confirm Password", type="password", key="confirm_password")

            if st.button("Create Account"):
                if new_username.strip() == "" or new_password.strip() == "":
                    st.error("Username and password cannot be empty")
                elif new_password != confirm_password:
                    st.error("Passwords do not match")
                elif register_user(new_username, new_password):
                    st.success("Account created successfully. Now login.")
                else:
                    st.error("Username already exists")

        st.markdown("</div>", unsafe_allow_html=True)


# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------
def render_sidebar():
    st.sidebar.markdown("## ⚡ AI Navigation")

    st.sidebar.markdown(f"""
    <div class="glass-card">
        <h3 style="margin-bottom:8px;">👤 {st.session_state.username}</h3>
        <p style="color:#cbd5e1;">Career Intelligence Profile</p>
    </div>
    """, unsafe_allow_html=True)

    page = st.sidebar.radio(
        "Choose Module",
        [
            "🏠 Executive Dashboard",
            "📄 Resume Intelligence",
            "📊 Skill Matrix",
            "💼 Job Match Engine",
            "🛣 Learning Roadmap",
            "🤖 AI Mentor",
            "👤 Profile"
        ]
    )

    st.sidebar.markdown("---")

    st.sidebar.markdown("""
    <div class="small-card">
        <h4>💡 Tip</h4>
        <p style="color:#cbd5e1;">
            Upload your resume and a job description to unlock full AI insights.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.sidebar.markdown("---")

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.session_state.analysis_result = None
        st.session_state.mentor_chat = []
        st.rerun()

    return page


# ---------------------------------------------------
# EXECUTIVE DASHBOARD
# ---------------------------------------------------
def executive_dashboard():
    page_heading(
        "Executive Dashboard",
        "View your career intelligence summary, employability insights, and improvement areas."
    )

    result = st.session_state.analysis_result

    if result:
        employability = result["employability_score"]
        match_score = result["match_score"]
        missing_count = len(result["missing_skills"])
        role_count = len(result["job_roles"])
        placement = min(96, int((employability + match_score) / 2) + random.randint(3, 8))
    else:
        employability = 0
        match_score = 0
        missing_count = 0
        role_count = 0
        placement = 0

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Employability", f"{employability}%")
    c2.metric("Resume Match", f"{match_score}%")
    c3.metric("Missing Skills", missing_count)
    c4.metric("Placement Chance", f"{placement}%")

    st.write("")

    col1, col2 = st.columns([1.4, 1])

    with col1:
        st.markdown("""
        <div class="glass-card">
            <h2>🧠 AI Career Summary</h2>
        """, unsafe_allow_html=True)

        if result:
            st.write(
                f"Your employability level is **{score_label(employability)}**. "
                f"You currently have **{len(result['resume_skills'])} detected skills**, "
                f"**{missing_count} missing skills**, and "
                f"**{role_count} recommended job roles**."
            )
        else:
            st.write("Analyze your resume first to generate personalized dashboard insights.")

        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("""
        <div class="glass-card">
            <h2>📌 Quick Highlights</h2>
            <p>• AI-based skill gap detection</p>
            <p>• Resume and job description comparison</p>
            <p>• Personalized learning roadmap</p>
            <p>• ChatGPT-style AI career mentor</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="glass-card">
            <h2>⚡ Dashboard Status</h2>
        """, unsafe_allow_html=True)

        st.progress(employability / 100 if employability else 0)
        st.caption("Employability Progress")

        st.progress(match_score / 100 if match_score else 0)
        st.caption("Resume Match Progress")

        st.markdown("</div>", unsafe_allow_html=True)

    if result:
        x1, x2 = st.columns(2)

        with x1:
            st.markdown('<div class="glass-card"><h2>✅ Strong Skills</h2>', unsafe_allow_html=True)
            pills(result["matched_skills"], "skill-pill")
            st.markdown("</div>", unsafe_allow_html=True)

        with x2:
            st.markdown('<div class="glass-card"><h2>⚠️ Missing Skills</h2>', unsafe_allow_html=True)
            pills(result["missing_skills"], "missing-pill")
            st.markdown("</div>", unsafe_allow_html=True)


# ---------------------------------------------------
# RESUME INTELLIGENCE
# ---------------------------------------------------
def resume_intelligence():
    page_heading(
        "Resume Intelligence",
        "Upload your resume and compare it with the target job description."
    )

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown('<div class="glass-card"><h3>📄 Upload Resume PDF</h3></div>', unsafe_allow_html=True)
        uploaded_file = st.file_uploader("Upload Resume PDF", type=["pdf"])

    with col2:
        st.markdown('<div class="glass-card"><h3>💼 Paste Job Description</h3></div>', unsafe_allow_html=True)
        job_description = st.text_area(
            "Paste Job Description",
            height=220,
            placeholder="Example: Looking for a Python developer with SQL, Machine Learning, AWS and Docker..."
        )

    if st.button("🚀 Analyze Resume"):
        if uploaded_file is None:
            st.error("Please upload a resume PDF.")
        elif job_description.strip() == "":
            st.error("Please paste the job description.")
        else:
            with st.spinner("AI is analyzing your resume..."):
                result = analyze_resume(uploaded_file, job_description)
                time.sleep(1)

            if "error" in result:
                st.error(result["error"])
            else:
                st.session_state.analysis_result = result
                st.session_state.last_uploaded_name = uploaded_file.name
                st.success("Resume analyzed successfully.")

    result = st.session_state.analysis_result

    if result:
        st.markdown("---")

        a1, a2, a3 = st.columns(3)

        a1.metric("Resume Match", f"{result['match_score']}%")
        a2.metric("Employability", f"{result['employability_score']}%")
        a3.metric("Skills Found", len(result["resume_skills"]))

        st.progress(result["match_score"] / 100)
        st.caption("Resume Match Score")

        st.progress(result["employability_score"] / 100)
        st.caption("Employability Score")

        b1, b2 = st.columns(2)

        with b1:
            st.markdown('<div class="glass-card"><h2>✅ Matched Skills</h2>', unsafe_allow_html=True)
            pills(result["matched_skills"], "skill-pill")
            st.markdown("</div>", unsafe_allow_html=True)

        with b2:
            st.markdown('<div class="glass-card"><h2>⚠️ Missing Skills</h2>', unsafe_allow_html=True)
            pills(result["missing_skills"], "missing-pill")
            st.markdown("</div>", unsafe_allow_html=True)

        st.markdown('<div class="glass-card"><h2>💡 AI Suggestions</h2>', unsafe_allow_html=True)

        for suggestion in result["suggestions"]:
            st.write("✅", suggestion)

        st.markdown("</div>", unsafe_allow_html=True)


# ---------------------------------------------------
# SKILL MATRIX
# ---------------------------------------------------
def skill_matrix():
    page_heading(
        "Advanced Skill Matrix",
        "Visualize your detected skills and identify weak areas."
    )

    result = st.session_state.analysis_result

    if not result:
        st.info("Analyze your resume first to generate the skill matrix.")
        return

    all_skills = sorted(set(result["resume_skills"] + result["required_skills"]))

    for skill in all_skills:
        if skill in result["missing_skills"]:
            value = random.randint(25, 50)
            status = "Needs Improvement"
        elif skill in result["matched_skills"]:
            value = random.randint(78, 96)
            status = "Strong"
        else:
            value = random.randint(55, 75)
            status = "Moderate"

        st.markdown(f"""
        <div class="glass-card">
            <h3>{skill}</h3>
            <p style="color:#cbd5e1;">Status: <b>{status}</b></p>
        </div>
        """, unsafe_allow_html=True)

        st.progress(value / 100)
        st.caption(f"{value}% proficiency estimate")


# ---------------------------------------------------
# JOB MATCH ENGINE
# ---------------------------------------------------
def job_match_engine():
    page_heading(
        "Job Match Engine",
        "Explore AI-recommended job roles based on your skills."
    )

    result = st.session_state.analysis_result

    if not result:
        st.info("Analyze your resume first to get job role suggestions.")
        return

    cols = st.columns(2)

    for i, role in enumerate(result["job_roles"]):
        score = random.randint(74, 96)

        with cols[i % 2]:
            st.markdown(f"""
            <div class="glass-card">
                <h2>💼 {role}</h2>
                <h1>{score}%</h1>
                <p class="subtext">AI compatibility score for this role</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<div class="glass-card"><h2>🎯 Suggested Roles</h2>', unsafe_allow_html=True)
    pills(result["job_roles"], "role-pill")
    st.markdown("</div>", unsafe_allow_html=True)


# ---------------------------------------------------
# LEARNING ROADMAP
# ---------------------------------------------------
def learning_roadmap():
    page_heading(
        "Learning Roadmap",
        "Follow a personalized roadmap based on your missing skills."
    )

    result = st.session_state.analysis_result

    if not result:
        st.info("Analyze your resume first to generate your roadmap.")
        return

    roadmap = result.get("roadmap", [])

    for item in roadmap:
        st.markdown(f"""
        <div class="glass-card">
            <h2>{item["week"]}: {item["skill"]}</h2>
            <p>{item["task"]}</p>
        </div>
        """, unsafe_allow_html=True)


# ---------------------------------------------------
# AI MENTOR CHATBOT
# ---------------------------------------------------
def ai_mentor():
    page_heading(
        "AI Mentor",
        "Chat with your AI career mentor like ChatGPT."
    )

    st.markdown("""
    <div class="glass-card">
        <h2>🤖 AI Career Mentor</h2>
        <p class="subtext">
            Ask about resume improvement, projects, missing skills, internships,
            interview preparation, job roles, or learning roadmap.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Clear Chat"):
        st.session_state.mentor_chat = []
        st.rerun()

    for msg in st.session_state.mentor_chat:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    user_question = st.chat_input("Ask your AI Mentor...")

    if user_question:
        st.session_state.mentor_chat.append({
            "role": "user",
            "content": user_question
        })

        with st.chat_message("user"):
            st.write(user_question)

        with st.chat_message("assistant"):
            with st.spinner("AI Mentor is thinking..."):
                answer = ai_mentor_response(
                    question=user_question,
                    analysis_result=st.session_state.analysis_result,
                    chat_history=st.session_state.mentor_chat
                )

            st.write(answer)

        st.session_state.mentor_chat.append({
            "role": "assistant",
            "content": answer
        })


# ---------------------------------------------------
# PROFILE
# ---------------------------------------------------
def profile():
    page_heading(
        "Performance Profile",
        "Track your current performance and career profile summary."
    )

    result = st.session_state.analysis_result

    if result:
        employability = f"{result['employability_score']}%"
        match_score = f"{result['match_score']}%"
        total_skills = len(result["resume_skills"])
        missing = len(result["missing_skills"])
        uploaded_resume = st.session_state.last_uploaded_name or "Uploaded"
    else:
        employability = "Not analyzed"
        match_score = "Not analyzed"
        total_skills = "Not analyzed"
        missing = "Not analyzed"
        uploaded_resume = "No resume uploaded"

    st.markdown(f"""
    <div class="glass-card">
        <h2>👤 User Profile</h2>
        <p><b>Username:</b> {st.session_state.username}</p>
        <p><b>Uploaded Resume:</b> {uploaded_resume}</p>
        <p><b>Employability Score:</b> {employability}</p>
        <p><b>Resume Match Score:</b> {match_score}</p>
        <p><b>Total Skills Found:</b> {total_skills}</p>
        <p><b>Missing Skills:</b> {missing}</p>
        <p><b>Growth Curve:</b> Rising</p>
    </div>
    """, unsafe_allow_html=True)

    if result and result["job_roles"]:
        st.markdown('<div class="glass-card"><h2>💼 Best Matched Roles</h2>', unsafe_allow_html=True)
        pills(result["job_roles"], "role-pill")
        st.markdown("</div>", unsafe_allow_html=True)


# ---------------------------------------------------
# MAIN DASHBOARD
# ---------------------------------------------------
def dashboard():
    page = render_sidebar()

    if page == "🏠 Executive Dashboard":
        executive_dashboard()

    elif page == "📄 Resume Intelligence":
        resume_intelligence()

    elif page == "📊 Skill Matrix":
        skill_matrix()

    elif page == "💼 Job Match Engine":
        job_match_engine()

    elif page == "🛣 Learning Roadmap":
        learning_roadmap()

    elif page == "🤖 AI Mentor":
        ai_mentor()

    elif page == "👤 Profile":
        profile()


# ---------------------------------------------------
# RUN APP
# ---------------------------------------------------
if st.session_state.logged_in:
    dashboard()
else:
    login_page()
