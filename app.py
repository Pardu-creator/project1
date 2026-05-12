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

.stButton>button{
width:100%;
height:52px;
border:none;
border-radius:18px;
font-weight:800;
background:linear-gradient(90deg,#00eaff,#8b5cf6);
color:white;
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

</style>
""",unsafe_allow_html=True)

# ---------------- SESSION ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in=False


# ---------------- LOGIN ----------------
def login_page():

    left,right=st.columns([1.7,1])

    with left:
        st.markdown("""
        <div style="height:95vh;display:flex;flex-direction:column;justify-content:center;">
        <div class="hero">
        Skill-Gap Aware Employability
        </div>

        <h3>Assessment Platform Using Artificial Intelligence</h3>

        <p>
        AI-powered employability prediction platform
        for resume intelligence, skill-gap analysis,
        placement forecasting and career growth optimization.
        </p>
        </div>
        """,unsafe_allow_html=True)

    with right:

        st.markdown('<div class="card">',unsafe_allow_html=True)

        tab1,tab2=st.tabs(["🔐 Login","✨ Register"])

        with tab1:
            u=st.text_input("Username")
            p=st.text_input("Password",type="password")

            if st.button("Secure Login"):
                if login_user(u,p):
                    st.session_state.logged_in=True
                    st.rerun()
                else:
                    st.error("Invalid Login")

        with tab2:
            u=st.text_input("Create Username")
            p=st.text_input("Create Password",type="password")

            if st.button("Create Account"):
                if register_user(u,p):
                    st.success("Registered")
                else:
                    st.error("User Exists")

        st.markdown("</div>",unsafe_allow_html=True)


# ---------------- DASHBOARD ----------------
def dashboard():

    st.sidebar.markdown("## ⚡ AI Navigation")

    page=st.sidebar.radio(
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

    if page=="🏠 Executive Dashboard":

        st.markdown(
        '<div class="hero">Executive Dashboard</div>',
        unsafe_allow_html=True)

        c1,c2,c3,c4=st.columns(4)

        c1.metric("Employability","91%","+7%")
        c2.metric("Missing Skills","4")
        c3.metric("Job Matches","18")
        c4.metric("Placement Chance","88%")

    elif page=="📄 Resume Intelligence":

        st.file_uploader("Upload Resume PDF")
        st.text_area("Paste Job Description")

        if st.button("Analyze Resume"):

            score=random.randint(70,96)

            st.metric("Resume Match",f"{score}%")
            st.progress(score/100)

            st.success("Strong Python + SQL")
            st.warning("Improve AWS + Docker")

    elif page=="📊 Skill Matrix":

        st.markdown(
        '<div class="hero">Advanced Skill Matrix</div>',
        unsafe_allow_html=True)

        skills={
            "Python":94,
            "SQL":88,
            "Machine Learning":79,
            "Cloud":61,
            "Docker":48,
            "System Design":39
        }

        for skill,val in skills.items():

            status=(
                "Elite"
                if val>90 else
                "Strong"
                if val>75 else
                "Moderate"
                if val>55 else
                "Needs Improvement"
            )

            st.markdown(f"""
            <div class="card">
            <h2>{skill}</h2>
            <h3>{val}%</h3>
            <p>{status}</p>
            </div>
            """,unsafe_allow_html=True)

            st.progress(val/100)

        st.markdown("""
        <div class="card">
        <h2>AI Recommendation</h2>
        <p>
        Focus on Cloud + Docker + System Design
        to unlock senior engineering opportunities.
        </p>
        </div>
        """,unsafe_allow_html=True)

    elif page=="💼 Job Match Engine":

        jobs=[
            ("Senior Data Analyst","94%"),
            ("Backend Engineer","89%"),
            ("ML Engineer","81%"),
            ("Cloud Engineer","73%")
        ]

        for role,score in jobs:
            st.markdown(f"""
            <div class="card">
            <h2>{role}</h2>
            <h1>{score}</h1>
            </div>
            """,unsafe_allow_html=True)

    elif page=="🛣 Learning Roadmap":

        for x in [
            "Week 1 → Advanced SQL",
            "Week 2 → Docker",
            "Week 3 → AWS",
            "Week 4 → System Design"
        ]:
            st.success(x)

    elif page=="🤖 AI Mentor":

        q=st.text_input("Ask AI")

        if st.button("Analyze"):
            st.success(
            "Recommended: Build Cloud + ML deployment projects."
            )

    elif page=="👤 Profile":

        st.markdown("""
        <div class="card">
        <h2>Performance Profile</h2>
        <p>Consistency: Excellent</p>
        <p>Placement Readiness: High</p>
        <p>Growth Curve: Rising</p>
        </div>
        """,unsafe_allow_html=True)

    if st.sidebar.button("Logout"):
        st.session_state.logged_in=False
        st.rerun()


# ---------------- RUN ----------------
if st.session_state.logged_in:
    dashboard()
else:
    login_page()
