import streamlit as st
from backend import register_user, login_user
import random

st.set_page_config(
    page_title="Skill-Gap AI Platform",
    page_icon="⚡",
    layout="wide"
)

# ---------------- ADVANCED UI ----------------
st.markdown("""
<style>

.stApp{
background:
radial-gradient(circle at top left,#00eaff22,transparent 25%),
radial-gradient(circle at bottom right,#8b5cf622,transparent 25%),
linear-gradient(135deg,#020617,#0f172a,#111827);
color:white;
}

.card{
background:rgba(255,255,255,.08);
backdrop-filter:blur(28px);
padding:28px;
border-radius:24px;
border:1px solid rgba(255,255,255,.1);
margin:15px 0;
box-shadow:0 0 25px rgba(0,234,255,.15);
transition:.4s;
}

.card:hover{
transform:translateY(-8px);
box-shadow:0 0 45px rgba(0,234,255,.35);
}

.hero{
font-size:55px;
font-weight:900;
background:linear-gradient(90deg,#00eaff,#8b5cf6,#fff);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

.subtitle{
font-size:24px;
color:#e5e7eb;
}

.description{
font-size:18px;
color:#cbd5e1;
line-height:1.7;
}

.stButton>button{
width:100%;
height:52px;
border:none;
border-radius:18px;
font-weight:800;
background:linear-gradient(90deg,#00eaff,#8b5cf6);
color:white;
}

.stButton>button:hover{
box-shadow:0 0 30px rgba(0,234,255,.5);
transform:scale(1.02);
}

.stTextInput input,
textarea{
background:rgba(255,255,255,.06)!important;
color:white!important;
border:1px solid #00eaff!important;
border-radius:16px!important;
}

section[data-testid="stSidebar"]{
background:rgba(15,23,42,.96);
border-right:1px solid rgba(255,255,255,.08);
}

[data-testid="stMetric"]{
background:rgba(255,255,255,.08);
padding:22px;
border-radius:22px;
border:1px solid rgba(255,255,255,.1);
box-shadow:0 0 20px rgba(0,234,255,.12);
}

</style>
""", unsafe_allow_html=True)


# ---------------- SESSION ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""


# ---------------- LOGIN PAGE ----------------
def login_page():

    left, right = st.columns([1.7, 1])

    with left:
        st.markdown("""
        <div style="height:95vh;display:flex;flex-direction:column;justify-content:center;">
            <div class="hero">
                Skill-Gap Aware Employability
            </div>

            <h3 class="subtitle">
                Assessment Platform Using Artificial Intelligence
            </h3>

            <p class="description">
                AI-powered employability prediction platform for resume intelligence,
                skill-gap analysis, placement forecasting and career growth optimization.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with right:

        st.markdown("<br><br><br><br>", unsafe_allow_html=True)
        st.markdown('<div class="card">', unsafe_allow_html=True)

        tab1, tab2 = st.tabs(["🔐 Login", "✨ Register"])

        # ---------------- LOGIN TAB ----------------
        with tab1:
            login_username = st.text_input(
                "Username",
                key="login_username"
            )

            login_password = st.text_input(
                "Password",
                type="password",
                key="login_password"
            )

            if st.button("Secure Login", key="login_button"):
                if login_user(login_username, login_password):
                    st.session_state.logged_in = True
                    st.session_state.username = login_username
                    st.success("Login Successful")
                    st.rerun()
                else:
                    st.error("Invalid Username or Password")

        # ---------------- REGISTER TAB ----------------
        with tab2:
            register_username = st.text_input(
                "Create Username",
                key="register_username"
            )

            register_password = st.text_input(
                "Create Password",
                type="password",
                key="register_password"
            )

            confirm_password = st.text_input(
                "Confirm Password",
                type="password",
                key="confirm_password"
            )

            if st.button("Create Account", key="register_button"):

                if register_username.strip() == "" or register_password.strip() == "":
                    st.error("Username and password cannot be empty")

                elif register_password != confirm_password:
                    st.error("Passwords do not match")

                else:
                    if register_user(register_username, register_password):
                        st.success("Account Created Successfully. Now login.")
                    else:
                        st.error("User already exists")

        st.markdown("</div>", unsafe_allow_html=True)


# ---------------- DASHBOARD ----------------
def dashboard():

    st.sidebar.markdown("## ⚡ AI Navigation")

    st.sidebar.success(f"Logged in as: {st.session_state.username}")

    page = st.sidebar.radio(
        "",
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

    # ---------------- EXECUTIVE DASHBOARD ----------------
    if page == "🏠 Executive Dashboard":

        st.markdown(
            '<div class="hero">Executive Dashboard</div>',
            unsafe_allow_html=True
        )

        st.write("")

        c1, c2, c3, c4 = st.columns(4)

        c1.metric("Employability", "91%", "+7%")
        c2.metric("Missing Skills", "4")
        c3.metric("Job Matches", "18")
        c4.metric("Placement Chance", "88%")

        st.markdown("""
        <div class="card">
            <h2>AI Career Summary</h2>
            <p>
            Your profile shows strong employability readiness.
            Focus more on Cloud, Docker and System Design to improve your placement score.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # ---------------- RESUME INTELLIGENCE ----------------
    elif page == "📄 Resume Intelligence":

        st.markdown(
            '<div class="hero">Resume Intelligence</div>',
            unsafe_allow_html=True
        )

        uploaded_file = st.file_uploader("Upload Resume PDF", type=["pdf"])

        job_description = st.text_area("Paste Job Description")

        if st.button("Analyze Resume"):

            if uploaded_file is None:
                st.error("Please upload your resume PDF")

            elif job_description.strip() == "":
                st.error("Please paste the job description")

            else:
                score = random.randint(70, 96)

                st.metric("Resume Match", f"{score}%")
                st.progress(score / 100)

                st.markdown("""
                <div class="card">
                    <h2>Resume Analysis Result</h2>
                    <p><b>Strong Skills:</b> Python, SQL, Machine Learning</p>
                    <p><b>Missing Skills:</b> AWS, Docker, System Design</p>
                    <p><b>Suggestion:</b> Add project experience and deployment details.</p>
                </div>
                """, unsafe_allow_html=True)

                st.success("Strong Python + SQL")
                st.warning("Improve AWS + Docker")

    # ---------------- SKILL MATRIX ----------------
    elif page == "📊 Skill Matrix":

        st.markdown(
            '<div class="hero">Advanced Skill Matrix</div>',
            unsafe_allow_html=True
        )

        skills = {
            "Python": 94,
            "SQL": 88,
            "Machine Learning": 79,
            "Cloud": 61,
            "Docker": 48,
            "System Design": 39
        }

        for skill, val in skills.items():

            if val > 90:
                status = "Elite"
            elif val > 75:
                status = "Strong"
            elif val > 55:
                status = "Moderate"
            else:
                status = "Needs Improvement"

            st.markdown(f"""
            <div class="card">
                <h2>{skill}</h2>
                <h3>{val}%</h3>
                <p>{status}</p>
            </div>
            """, unsafe_allow_html=True)

            st.progress(val / 100)

        st.markdown("""
        <div class="card">
            <h2>AI Recommendation</h2>
            <p>
            Focus on Cloud + Docker + System Design to unlock better software,
            data engineering and AI deployment opportunities.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # ---------------- JOB MATCH ENGINE ----------------
    elif page == "💼 Job Match Engine":

        st.markdown(
            '<div class="hero">Job Match Engine</div>',
            unsafe_allow_html=True
        )

        jobs = [
            ("Senior Data Analyst", "94%"),
            ("Backend Engineer", "89%"),
            ("ML Engineer", "81%"),
            ("Cloud Engineer", "73%")
        ]

        for role, score in jobs:
            st.markdown(f"""
            <div class="card">
                <h2>{role}</h2>
                <h1>{score}</h1>
                <p>AI-based job compatibility score</p>
            </div>
            """, unsafe_allow_html=True)

    # ---------------- LEARNING ROADMAP ----------------
    elif page == "🛣 Learning Roadmap":

        st.markdown(
            '<div class="hero">Learning Roadmap</div>',
            unsafe_allow_html=True
        )

        roadmap = [
            "Week 1 → Advanced SQL",
            "Week 2 → Docker Basics",
            "Week 3 → AWS Cloud Deployment",
            "Week 4 → System Design Fundamentals",
            "Week 5 → Resume Projects",
            "Week 6 → Mock Interviews"
        ]

        for item in roadmap:
            st.success(item)

    # ---------------- AI MENTOR ----------------
    elif page == "🤖 AI Mentor":

        st.markdown(
            '<div class="hero">AI Mentor</div>',
            unsafe_allow_html=True
        )

        question = st.text_input("Ask AI Mentor")

        if st.button("Analyze", key="mentor_button"):

            if question.strip() == "":
                st.error("Please enter a question")
            else:
                st.markdown("""
                <div class="card">
                    <h2>AI Mentor Response</h2>
                    <p>
                    Recommended: Build Cloud + ML deployment projects.
                    Add one resume project using Streamlit, Python, SQL and Machine Learning.
                    </p>
                </div>
                """, unsafe_allow_html=True)

    # ---------------- PROFILE ----------------
    elif page == "👤 Profile":

        st.markdown(
            '<div class="hero">Performance Profile</div>',
            unsafe_allow_html=True
        )

        st.markdown(f"""
        <div class="card">
            <h2>User Profile</h2>
            <p><b>Username:</b> {st.session_state.username}</p>
            <p><b>Consistency:</b> Excellent</p>
            <p><b>Placement Readiness:</b> High</p>
            <p><b>Growth Curve:</b> Rising</p>
        </div>
        """, unsafe_allow_html=True)

    # ---------------- LOGOUT ----------------
    st.sidebar.markdown("---")

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()


# ---------------- RUN APP ----------------
if st.session_state.logged_in:
    dashboard()
else:
    login_page()
