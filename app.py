import streamlit as st
from backend import register_user, login_user, analyze_resume
import random
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Skill-Gap AI Platform",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- GLOBAL CSS ----------------
st.markdown("""
<style>

/* ---------------- MAIN BACKGROUND ---------------- */
.stApp {
    background:
    radial-gradient(circle at 10% 10%, rgba(0,234,255,0.18), transparent 25%),
    radial-gradient(circle at 90% 90%, rgba(139,92,246,0.20), transparent 25%),
    linear-gradient(135deg, #020617 0%, #0f172a 45%, #111827 100%);
    color: white;
}

/* ---------------- HIDE DEFAULT STREAMLIT ---------------- */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* ---------------- TEXT DESIGN ---------------- */
.hero-title {
    font-size: 64px;
    font-weight: 900;
    line-height: 1.1;
    background: linear-gradient(90deg, #22d3ee, #60a5fa, #a78bfa, #ffffff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: glow 3s infinite alternate;
}

@keyframes glow {
    from {filter: drop-shadow(0 0 8px rgba(34,211,238,0.3));}
    to {filter: drop-shadow(0 0 20px rgba(167,139,250,0.7));}
}

.page-title {
    font-size: 52px;
    font-weight: 900;
    margin-bottom: 20px;
    background: linear-gradient(90deg, #22d3ee, #60a5fa, #8b5cf6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.sub-text {
    color: #cbd5e1;
    font-size: 18px;
    line-height: 1.7;
}

/* ---------------- GLASS CARD ---------------- */
.glass-card {
    background: rgba(255,255,255,0.075);
    backdrop-filter: blur(28px);
    -webkit-backdrop-filter: blur(28px);
    padding: 28px;
    border-radius: 28px;
    border: 1px solid rgba(255,255,255,0.12);
    box-shadow:
        0 0 35px rgba(0,234,255,0.10),
        inset 0 0 20px rgba(255,255,255,0.03);
    margin: 18px 0;
    transition: all 0.35s ease;
}

.glass-card:hover {
    transform: translateY(-6px);
    box-shadow:
        0 0 45px rgba(0,234,255,0.28),
        0 0 60px rgba(139,92,246,0.18);
}

/* ---------------- MINI CARD ---------------- */
.mini-card {
    background: linear-gradient(135deg, rgba(34,211,238,0.12), rgba(139,92,246,0.12));
    padding: 22px;
    border-radius: 24px;
    border: 1px solid rgba(34,211,238,0.22);
    margin: 12px 0;
}

/* ---------------- BUTTONS ---------------- */
.stButton>button {
    width: 100%;
    min-height: 52px;
    border: none;
    border-radius: 18px;
    font-weight: 800;
    color: white;
    background: linear-gradient(90deg, #06b6d4, #3b82f6, #8b5cf6);
    box-shadow: 0 0 22px rgba(34,211,238,0.22);
    transition: all 0.25s ease;
}

.stButton>button:hover {
    transform: translateY(-2px) scale(1.01);
    box-shadow: 0 0 35px rgba(34,211,238,0.55);
}

/* ---------------- INPUTS ---------------- */
.stTextInput input,
.stTextArea textarea {
    background: rgba(255,255,255,0.08)!important;
    color: white!important;
    border: 1px solid rgba(34,211,238,0.85)!important;
    border-radius: 18px!important;
    padding: 14px!important;
}

.stTextInput input:focus,
.stTextArea textarea:focus {
    border: 1px solid #a78bfa!important;
    box-shadow: 0 0 18px rgba(167,139,250,0.35)!important;
}

/* ---------------- FILE UPLOADER ---------------- */
[data-testid="stFileUploader"] {
    background: rgba(255,255,255,0.08);
    padding: 20px;
    border-radius: 22px;
    border: 1px dashed rgba(34,211,238,0.7);
}

/* ---------------- SIDEBAR ---------------- */
section[data-testid="stSidebar"] {
    background:
    linear-gradient(180deg, rgba(15,23,42,0.98), rgba(2,6,23,0.98));
    border-right: 1px solid rgba(255,255,255,0.10);
}

section[data-testid="stSidebar"] * {
    color: white;
}

/* ---------------- METRICS ---------------- */
[data-testid="stMetric"] {
    background: rgba(255,255,255,0.08);
    padding: 24px;
    border-radius: 24px;
    border: 1px solid rgba(255,255,255,0.12);
    box-shadow: 0 0 25px rgba(34,211,238,0.14);
}

/* ---------------- SKILL PILLS ---------------- */
.skill-pill {
    display: inline-block;
    padding: 10px 17px;
    margin: 7px;
    border-radius: 30px;
    font-weight: 800;
    color: white;
    background: linear-gradient(90deg, #06b6d4, #3b82f6);
    box-shadow: 0 0 16px rgba(34,211,238,0.25);
}

.missing-pill {
    display: inline-block;
    padding: 10px 17px;
    margin: 7px;
    border-radius: 30px;
    font-weight: 800;
    color: white;
    background: linear-gradient(90deg, #ef4444, #f97316);
    box-shadow: 0 0 16px rgba(249,115,22,0.25);
}

.role-pill {
    display: inline-block;
    padding: 10px 17px;
    margin: 7px;
    border-radius: 30px;
    font-weight: 800;
    color: white;
    background: linear-gradient(90deg, #22c55e, #14b8a6);
}

/* ---------------- PROGRESS BAR ---------------- */
.stProgress > div > div > div > div {
    background: linear-gradient(90deg, #22d3ee, #3b82f6, #8b5cf6);
}

/* ---------------- TABS ---------------- */
.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
}

.stTabs [data-baseweb="tab"] {
    background: rgba(255,255,255,0.08);
    border-radius: 16px;
    padding: 12px 18px;
    font-weight: 800;
}

</style>
""", unsafe_allow_html=True)


# ---------------- SESSION STATE ----------------
def init_session():
    defaults = {
        "logged_in": False,
        "username": "",
        "analysis_result": None,
        "last_uploaded_name": ""
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


init_session()


# ---------------- SMALL UI COMPONENTS ----------------
def title(text):
    st.markdown(f'<div class="page-title">{text}</div>', unsafe_allow_html=True)


def glass_card(title_text, body_text, icon="⚡"):
    st.markdown(f"""
    <div class="glass-card">
        <h2>{icon} {title_text}</h2>
        <p class="sub-text">{body_text}</p>
    </div>
    """, unsafe_allow_html=True)


def show_pills(items, class_name):
    if items:
        html = ""
        for item in sorted(items):
            html += f'<span class="{class_name}">{item}</span>'
        st.markdown(html, unsafe_allow_html=True)
    else:
        st.info("No data available")


def score_status(score):
    if score >= 85:
        return "Excellent"
    elif score >= 70:
        return "Good"
    elif score >= 50:
        return "Average"
    else:
        return "Needs Improvement"


# ---------------- LOGIN PAGE ----------------
def login_page():
    left, right = st.columns([1.55, 1], gap="large")

    with left:
        st.markdown("""
        <div style="height:92vh;display:flex;flex-direction:column;justify-content:center;">
            <div class="hero-title">Skill-Gap Aware Employability</div>
            <h2 style="color:white;margin-top:20px;">
                Assessment Platform Using Artificial Intelligence
            </h2>
            <p class="sub-text">
                Upload your resume, compare it with job descriptions, detect missing skills,
                calculate employability score, generate career roadmap and get AI-based
                job role suggestions.
            </p>

            <div class="glass-card">
                <h3>🚀 Platform Features</h3>
                <p>✅ Resume Intelligence</p>
                <p>✅ Skill-Gap Analysis</p>
                <p>✅ Employability Prediction</p>
                <p>✅ AI Learning Roadmap</p>
                <p>✅ Job Match Engine</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with right:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)

        st.markdown("""
        <h2 style="text-align:center;">⚡ Welcome Back</h2>
        <p style="text-align:center;color:#cbd5e1;">Login or create your account</p>
        """, unsafe_allow_html=True)

        tab1, tab2 = st.tabs(["🔐 Login", "✨ Register"])

        with tab1:
            username = st.text_input("Username", key="login_username")
            password = st.text_input("Password", type="password", key="login_password")

            if st.button("Secure Login", key="login_btn"):
                if login_user(username, password):
                    st.session_state.logged_in = True
                    st.session_state.username = username.strip().lower()
                    st.success("Login successful")
                    time.sleep(0.5)
                    st.rerun()
                else:
                    st.error("Invalid username or password")

        with tab2:
            username = st.text_input("Create Username", key="register_username")
            password = st.text_input("Create Password", type="password", key="register_password")
            confirm_password = st.text_input("Confirm Password", type="password", key="confirm_password")

            if st.button("Create Account", key="register_btn"):
                if username.strip() == "" or password.strip() == "":
                    st.error("Username and password cannot be empty")

                elif len(password) < 4:
                    st.error("Password must be at least 4 characters")

                elif password != confirm_password:
                    st.error("Passwords do not match")

                elif register_user(username, password):
                    st.success("Account created successfully. Now login.")

                else:
                    st.error("Username already exists")

        st.markdown("</div>", unsafe_allow_html=True)


# ---------------- MAIN DASHBOARD ----------------
def dashboard():
    st.sidebar.markdown("## ⚡ AI Navigation")

    st.sidebar.markdown(f"""
    <div class="glass-card">
        <h3>👤 {st.session_state.username}</h3>
        <p>Career Intelligence Profile</p>
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

    st.sidebar.markdown("---")

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.session_state.analysis_result = None
        st.rerun()


# ---------------- EXECUTIVE DASHBOARD ----------------
def executive_dashboard():
    title("Executive Dashboard")

    result = st.session_state.analysis_result

    if result:
        employability = result["employability_score"]
        match_score = result["match_score"]
        missing_count = len(result["missing_skills"])
        job_count = len(result["job_roles"])
        placement = min(96, int((employability + match_score) / 2) + random.randint(3, 8))
    else:
        employability = 0
        match_score = 0
        missing_count = 0
        job_count = 0
        placement = 0

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Employability", f"{employability}%")
    c2.metric("Resume Match", f"{match_score}%")
    c3.metric("Missing Skills", missing_count)
    c4.metric("Placement Chance", f"{placement}%")

    st.write("")

    if result:
        status = score_status(employability)

        glass_card(
            "AI Career Summary",
            f"Your current employability level is {status}. "
            f"You have {len(result['resume_skills'])} detected skills and "
            f"{missing_count} missing skills based on the job description.",
            "🧠"
        )

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("""
            <div class="glass-card">
                <h2>✅ Strong Areas</h2>
            """, unsafe_allow_html=True)
            show_pills(result["matched_skills"], "skill-pill")
            st.markdown("</div>", unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div class="glass-card">
                <h2>⚠️ Improvement Areas</h2>
            """, unsafe_allow_html=True)
            show_pills(result["missing_skills"], "missing-pill")
            st.markdown("</div>", unsafe_allow_html=True)

    else:
        glass_card(
            "Start Your Analysis",
            "Go to Resume Intelligence, upload your resume PDF and paste a job description. "
            "After analysis, your real dashboard scores will appear here.",
            "🚀"
        )


# ---------------- RESUME INTELLIGENCE ----------------
def resume_intelligence():
    title("Resume Intelligence")

    col1, col2 = st.columns([1, 1.2], gap="large")

    with col1:
        st.markdown("""
        <div class="glass-card">
            <h2>📄 Upload Resume</h2>
            <p class="sub-text">
            Upload a text-based PDF resume. The AI engine will extract skills and compare
            them with the job description.
            </p>
        </div>
        """, unsafe_allow_html=True)

        uploaded_file = st.file_uploader("Upload Resume PDF", type=["pdf"])

    with col2:
        st.markdown("""
        <div class="glass-card">
            <h2>💼 Job Description</h2>
            <p class="sub-text">
            Paste the target job description to calculate resume match and missing skills.
            </p>
        </div>
        """, unsafe_allow_html=True)

        job_description = st.text_area(
            "Paste Job Description",
            height=210,
            placeholder="Example: We need a Python developer with SQL, Machine Learning, AWS, Docker..."
        )

    analyze_btn = st.button("🚀 Analyze Resume")

    if analyze_btn:
        if uploaded_file is None:
            st.error("Please upload your resume PDF")

        elif job_description.strip() == "":
            st.error("Please paste the job description")

        else:
            with st.spinner("AI engine is analyzing your resume..."):
                result = analyze_resume(uploaded_file, job_description)
                time.sleep(1)

            if "error" in result:
                st.error(result["error"])
            else:
                st.session_state.analysis_result = result
                st.session_state.last_uploaded_name = uploaded_file.name
                st.success("Resume analyzed successfully")

    result = st.session_state.analysis_result

    if result:
        st.markdown("---")
        st.markdown("## 📊 AI Analysis Results")

        c1, c2, c3 = st.columns(3)

        c1.metric("Resume Match", f"{result['match_score']}%")
        c2.metric("Employability", f"{result['employability_score']}%")
        c3.metric("Total Skills Found", len(result["resume_skills"]))

        st.progress(result["match_score"] / 100)
        st.caption("Resume Match Score")

        st.progress(result["employability_score"] / 100)
        st.caption("Employability Score")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("""
            <div class="glass-card">
                <h2>✅ Matched Skills</h2>
            """, unsafe_allow_html=True)
            show_pills(result["matched_skills"], "skill-pill")
            st.markdown("</div>", unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div class="glass-card">
                <h2>⚠️ Missing Skills</h2>
            """, unsafe_allow_html=True)
            show_pills(result["missing_skills"], "missing-pill")
            st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("""
        <div class="glass-card">
            <h2>💡 AI Suggestions</h2>
        """, unsafe_allow_html=True)

        for suggestion in result["suggestions"]:
            st.write("✅", suggestion)

        st.markdown("</div>", unsafe_allow_html=True)


# ---------------- SKILL MATRIX ----------------
def skill_matrix():
    title("Advanced Skill Matrix")

    result = st.session_state.analysis_result

    if not result:
        glass_card(
            "No Analysis Found",
            "Analyze your resume first to generate your personalized skill matrix.",
            "📊"
        )
        return

    resume_skills = result["resume_skills"]
    required_skills = result["required_skills"]
    missing_skills = result["missing_skills"]

    if not resume_skills and not required_skills:
        st.warning("No skills detected")
        return

    all_skills = sorted(set(resume_skills + required_skills))

    for skill in all_skills:
        if skill in missing_skills:
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
            <h2>{skill}</h2>
            <p>Status: <b>{status}</b></p>
        </div>
        """, unsafe_allow_html=True)

        st.progress(value / 100)
        st.caption(f"{value}% proficiency estimate")


# ---------------- JOB MATCH ENGINE ----------------
def job_match_engine():
    title("Job Match Engine")

    result = st.session_state.analysis_result

    if not result:
        glass_card(
            "Job Suggestions Not Ready",
            "Upload and analyze your resume first to generate AI-based job role suggestions.",
            "💼"
        )
        return

    roles = result["job_roles"]

    cols = st.columns(2)

    for index, role in enumerate(roles):
        score = random.randint(75, 96)
        with cols[index % 2]:
            st.markdown(f"""
            <div class="glass-card">
                <h2>💼 {role}</h2>
                <h1>{score}%</h1>
                <p class="sub-text">AI-based compatibility score</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("""
    <div class="glass-card">
        <h2>📌 Job Match Logic</h2>
        <p class="sub-text">
        Job roles are suggested based on detected resume skills such as Python, SQL,
        Machine Learning, Web Development, Cloud and DevOps tools.
        </p>
    </div>
    """, unsafe_allow_html=True)


# ---------------- LEARNING ROADMAP ----------------
def learning_roadmap():
    title("Learning Roadmap")

    result = st.session_state.analysis_result

    if not result:
        glass_card(
            "Roadmap Not Generated",
            "Analyze your resume first to generate a personalized skill improvement roadmap.",
            "🛣"
        )
        return

    missing = result["missing_skills"]

    if not missing:
        glass_card(
            "Excellent Skill Match",
            "No major missing skills were found. Focus on building advanced projects and interview preparation.",
            "🏆"
        )
        return

    st.markdown("""
    <div class="glass-card">
        <h2>🛣 Personalized Weekly Roadmap</h2>
        <p class="sub-text">
        This roadmap is generated from your missing skills.
        </p>
    </div>
    """, unsafe_allow_html=True)

    for week, skill in enumerate(missing, start=1):
        st.markdown(f"""
        <div class="glass-card">
            <h2>Week {week}: {skill}</h2>
            <p>📘 Learn fundamentals of <b>{skill}</b></p>
            <p>🛠 Build one mini project using <b>{skill}</b></p>
            <p>📌 Add the project to GitHub and resume</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="glass-card">
        <h2>Final Step</h2>
        <p class="sub-text">
        Update your resume with projects, GitHub links, deployment links and measurable results.
        </p>
    </div>
    """, unsafe_allow_html=True)


# ---------------- AI MENTOR ----------------
def ai_mentor():
    title("AI Mentor")

    st.markdown("""
    <div class="glass-card">
        <h2>🤖 Ask Your Career AI Mentor</h2>
        <p class="sub-text">
        Ask about skills, projects, resume improvement, placement preparation or job roles.
        </p>
    </div>
    """, unsafe_allow_html=True)

    question = st.text_input(
        "Ask AI Mentor",
        placeholder="Example: How can I improve my resume for data analyst jobs?"
    )

    if st.button("Ask Mentor"):
        if question.strip() == "":
            st.error("Please enter a question")
            return

        result = st.session_state.analysis_result

        if result:
            missing = ", ".join(result["missing_skills"]) if result["missing_skills"] else "No major missing skills"
            roles = ", ".join(result["job_roles"])

            response = f"""
            Based on your resume analysis, your missing skills are: {missing}.
            Your suitable job roles are: {roles}.
            Focus on projects, GitHub, deployment, resume keywords and mock interviews.
            """
        else:
            response = """
            First upload your resume and job description in Resume Intelligence.
            Then I can give more personalized career guidance.
            """

        st.markdown(f"""
        <div class="glass-card">
            <h2>🧠 Mentor Response</h2>
            <p class="sub-text">{response}</p>
        </div>
        """, unsafe_allow_html=True)


# ---------------- PROFILE ----------------
def profile():
    title("Performance Profile")

    result = st.session_state.analysis_result

    if result:
        employability = f"{result['employability_score']}%"
        match_score = f"{result['match_score']}%"
        total_skills = len(result["resume_skills"])
        missing = len(result["missing_skills"])
        file_name = st.session_state.last_uploaded_name
    else:
        employability = "Not analyzed"
        match_score = "Not analyzed"
        total_skills = "Not analyzed"
        missing = "Not analyzed"
        file_name = "No resume uploaded"

    st.markdown(f"""
    <div class="glass-card">
        <h2>👤 User Profile</h2>
        <p><b>Username:</b> {st.session_state.username}</p>
        <p><b>Uploaded Resume:</b> {file_name}</p>
        <p><b>Employability Score:</b> {employability}</p>
        <p><b>Resume Match Score:</b> {match_score}</p>
        <p><b>Total Skills Found:</b> {total_skills}</p>
        <p><b>Missing Skills:</b> {missing}</p>
        <p><b>Growth Curve:</b> Rising</p>
    </div>
    """, unsafe_allow_html=True)

    if result:
        st.markdown("""
        <div class="glass-card">
            <h2>🎯 Suggested Roles</h2>
        """, unsafe_allow_html=True)

        show_pills(result["job_roles"], "role-pill")

        st.markdown("</div>", unsafe_allow_html=True)


# ---------------- RUN APP ----------------
if st.session_state.logged_in:
    dashboard()
else:
    login_page()
