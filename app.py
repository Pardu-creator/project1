import streamlit as st
from backend import register_user, login_user
import random

st.set_page_config(
    page_title="AI Employability Platform",
    page_icon="⚡",
    layout="wide"
)

# ---------------- ADVANCED CSS ----------------
st.markdown("""
<style>

.stApp{
background:linear-gradient(-45deg,#020617,#0f172a,#111827,#1e293b);
background-size:400% 400%;
animation:bgmove 15s ease infinite;
color:white;
}

@keyframes bgmove{
0%{background-position:0% 50%;}
50%{background-position:100% 50%;}
100%{background-position:0% 50%;}
}

.card{
background:rgba(255,255,255,.08);
backdrop-filter:blur(22px);
padding:28px;
border-radius:22px;
border:1px solid rgba(255,255,255,.12);
margin:12px 0;
box-shadow:0 0 30px rgba(0,234,255,.15);
transition:.4s;
}

.card:hover{
transform:translateY(-8px);
box-shadow:0 0 45px rgba(0,234,255,.35);
}

.hero{
font-size:65px;
font-weight:900;
background:linear-gradient(90deg,#00eaff,#8b5cf6);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

.stButton>button{
width:100%;
height:50px;
border:none;
border-radius:16px;
font-weight:bold;
background:linear-gradient(90deg,#00eaff,#8b5cf6);
color:white;
}

.stTextInput input,
textarea{
background:#0f172a !important;
color:white !important;
border:1px solid #00eaff !important;
border-radius:14px !important;
}

section[data-testid="stSidebar"]{
background:#0f172a;
}

</style>
""",unsafe_allow_html=True)

# ---------------- SESSION ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in=False


# ---------------- LOGIN ----------------
def login_page():

    left,right=st.columns([1.5,1])

    with left:
        st.markdown("""
        <div style="height:90vh;display:flex;flex-direction:column;justify-content:center;">
        <div class="hero">AI Employability</div>
        <h3>Future Career Intelligence Platform</h3>
        <p>Analyze resumes, predict employability, identify skill gaps and optimize placements.</p>
        </div>
        """,unsafe_allow_html=True)

    with right:

        st.markdown('<div class="card">',
                    unsafe_allow_html=True)

        tab1,tab2=st.tabs(["🔐 Login","✨ Register"])

        with tab1:
            u=st.text_input("Username",key="l1")
            p=st.text_input("Password",type="password",key="l2")

            if st.button("Secure Login"):
                if login_user(u,p):
                    st.session_state.logged_in=True
                    st.rerun()
                else:
                    st.error("Invalid Login")

        with tab2:
            u=st.text_input("Create Username",key="r1")
            p=st.text_input("Create Password",type="password",key="r2")

            if st.button("Create Account"):
                if register_user(u,p):
                    st.success("Registered")
                else:
                    st.error("User Exists")

        st.markdown("</div>",unsafe_allow_html=True)


# ---------------- AI ----------------
def ai_assistant():

    st.subheader("🤖 AI Career Mentor")

    q=st.text_input("Ask Question")

    if st.button("Ask AI"):

        q=q.lower()

        if "data analyst" in q:
            st.success("Learn Python, SQL, Tableau, Projects")

        elif "ml" in q:
            st.success("Learn ML, DL, Deployment, Cloud")

        elif "cloud" in q:
            st.success("Learn AWS, Docker, Kubernetes")

        else:
            st.info("Build strong projects + certifications")


# ---------------- DASHBOARD ----------------
def dashboard():

    page=st.sidebar.selectbox(
        "Navigation",
        [
            "🏠 Executive Dashboard",
            "📄 Resume Intelligence",
            "📊 Skill Analytics",
            "💼 Job Match Engine",
            "🛣 Learning Roadmap",
            "🤖 AI Assistant",
            "👤 Profile"
        ]
    )

    # HOME
    if page=="🏠 Executive Dashboard":

        st.markdown('<div class="hero">Dashboard</div>',
                    unsafe_allow_html=True)

        c1,c2,c3,c4=st.columns(4)

        c1.metric("Employability","87%","+5%")
        c2.metric("Missing Skills","4","-2")
        c3.metric("Jobs Matched","12","+4")
        c4.metric("Placement Chance","82%","+8%")

        st.markdown("""
        <div class="card">
        <h2>AI Insights</h2>
        <p>You are highly suited for backend and data roles. Improve cloud + deployment skills.</p>
        </div>
        """,unsafe_allow_html=True)

    # RESUME
    elif page=="📄 Resume Intelligence":

        st.file_uploader("Upload Resume PDF")
        st.text_area("Paste Job Description")

        if st.button("Analyze Resume"):

            score=random.randint(70,95)

            st.metric("Resume Match Score",f"{score}%")
            st.progress(score/100)

            st.success("Strong Python profile")
            st.warning("Missing Docker / AWS")

    # SKILL
    elif page=="📊 Skill Analytics":

        skills={
            "Python":92,
            "SQL":85,
            "Machine Learning":74,
            "Cloud":55,
            "Docker":41,
            "System Design":35
        }

        for s,v in skills.items():
            st.write(f"{s} - {v}%")
            st.progress(v/100)

    # JOB
    elif page=="💼 Job Match Engine":

        jobs=[
            ("Data Analyst",92),
            ("Backend Developer",88),
            ("ML Engineer",79),
            ("Cloud Engineer",72)
        ]

        for role,score in jobs:
            st.markdown(f"""
            <div class="card">
            <h2>{role}</h2>
            <h1>{score}% Match</h1>
            </div>
            """,unsafe_allow_html=True)

    # ROADMAP
    elif page=="🛣 Learning Roadmap":

        roadmap=[
            "Week 1-2 → SQL Mastery",
            "Week 3-4 → Docker",
            "Week 5-6 → AWS",
            "Week 7-8 → Deployment"
        ]

        for r in roadmap:
            st.success(r)

    # AI
    elif page=="🤖 AI Assistant":
        ai_assistant()

    # PROFILE
    elif page=="👤 Profile":

        st.markdown("""
        <div class="card">
        <h2>User Profile Analytics</h2>
        <p>Status: Active</p>
        <p>Resume Score Trend: Rising</p>
        <p>Learning Consistency: Strong</p>
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
