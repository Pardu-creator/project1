import streamlit as st
from backend import register_user, login_user
import random

st.set_page_config(
    page_title="Glass Cosmos AI",
    page_icon="⚡",
    layout="wide"
)

# ---------------- GLASS COSMOS CSS ----------------
st.markdown("""
<style>

.stApp{
background:
radial-gradient(circle at top left,#00eaff22,transparent 35%),
radial-gradient(circle at bottom right,#8b5cf622,transparent 35%),
linear-gradient(135deg,#020617,#0f172a,#111827);
color:white;
overflow:hidden;
}

.card{
background:rgba(255,255,255,.08);
backdrop-filter:blur(28px);
padding:28px;
border-radius:28px;
border:1px solid rgba(255,255,255,.12);
margin:15px 0;
box-shadow:
0 0 25px rgba(0,234,255,.15),
0 0 45px rgba(139,92,246,.08);
transition:.4s;
}

.card:hover{
transform:translateY(-8px);
box-shadow:
0 0 35px rgba(0,234,255,.35),
0 0 65px rgba(139,92,246,.18);
}

.hero{
font-size:70px;
font-weight:900;
background:linear-gradient(90deg,#00eaff,#8b5cf6,#ffffff);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

.stButton>button{
width:100%;
height:52px;
border:none;
border-radius:18px;
font-weight:bold;
background:linear-gradient(90deg,#00eaff,#8b5cf6);
color:white;
box-shadow:0 0 20px #00eaff55;
}

.stButton>button:hover{
transform:scale(1.03);
box-shadow:0 0 35px #00eaff99;
}

.stTextInput input,
textarea{
background:rgba(255,255,255,.06)!important;
color:white!important;
border:1px solid #00eaff!important;
border-radius:18px!important;
}

section[data-testid="stSidebar"]{
background:rgba(15,23,42,.9);
backdrop-filter:blur(25px);
border-right:1px solid rgba(255,255,255,.08);
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
        <div class="hero">Glass Cosmos</div>
        <h3>Future Career Intelligence Platform</h3>
        <p>
        Analyze resumes, predict employability,
        identify skill gaps and optimize placements.
        </p>
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

    st.subheader("🤖 Glass Cosmos AI Mentor")

    q=st.text_input("Ask Question")

    if st.button("Ask AI"):

        q=q.lower()

        if "data analyst" in q:
            st.success("Learn Python • SQL • Tableau • Projects")

        elif "ml" in q:
            st.success("Learn ML • DL • Deployment • Cloud")

        elif "cloud" in q:
            st.success("Learn AWS • Docker • Kubernetes")

        else:
            st.info("Build strong projects + certifications")


# ---------------- DASHBOARD ----------------
def dashboard():

    page=st.sidebar.selectbox(
        "Cosmos Navigation",
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
        <p>You are highly suited for backend and data roles.
        Improve cloud + deployment skills.</p>
        </div>
        """,unsafe_allow_html=True)

    elif page=="📄 Resume Intelligence":

        st.file_uploader("Upload Resume PDF")
        st.text_area("Paste Job Description")

        if st.button("Analyze Resume"):

            score=random.randint(70,95)

            st.metric("Resume Match Score",f"{score}%")
            st.progress(score/100)

            st.success("Strong Python profile")
            st.warning("Missing Docker / AWS")

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

    elif page=="🛣 Learning Roadmap":

        roadmap=[
            "Week 1-2 → SQL Mastery",
            "Week 3-4 → Docker",
            "Week 5-6 → AWS",
            "Week 7-8 → Deployment"
        ]

        for r in roadmap:
            st.success(r)

    elif page=="🤖 AI Assistant":
        ai_assistant()

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
