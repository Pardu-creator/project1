import streamlit as st
from backend import register_user, login_user
import random

st.set_page_config(
    page_title="AI Employability",
    page_icon="⚡",
    layout="wide"
)

# ---------------- CSS ----------------
st.markdown("""
<style>
.stApp{
background:#0a0f1f;
color:white;
}

.card{
background:rgba(255,255,255,.06);
backdrop-filter:blur(25px);
padding:30px;
border-radius:20px;
margin:15px 0;
border:1px solid #00eaff33;
}

.hero{
font-size:55px;
font-weight:900;
color:#00eaff;
}

.stButton>button{
width:100%;
background:linear-gradient(90deg,#00eaff,#8b5cf6);
color:white;
border:none;
border-radius:14px;
font-weight:bold;
}

.stTextInput input, textarea{
background:#0f172a !important;
color:white !important;
border:1px solid #00eaff !important;
border-radius:14px !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SESSION ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in=False


# ---------------- LOGIN ----------------
def login_page():

    st.markdown(
        '<div class="hero">AI Employability</div>',
        unsafe_allow_html=True
    )

    tab1,tab2=st.tabs(["Login","Register"])

    with tab1:
        u=st.text_input("Username")
        p=st.text_input("Password",type="password")

        if st.button("Login"):
            if login_user(u,p):
                st.session_state.logged_in=True
                st.rerun()
            else:
                st.error("Invalid Login")

    with tab2:
        u=st.text_input("Create Username")
        p=st.text_input("Create Password",type="password")

        if st.button("Register"):
            if register_user(u,p):
                st.success("Registered")
            else:
                st.error("User Exists")


# ---------------- AI CHATBOT ----------------
def ai_assistant():

    st.subheader("🤖 Career AI Assistant")

    question = st.text_input(
        "Ask career-related question"
    )

    if st.button("Ask AI"):

        q = question.lower()

        if "data analyst" in q:
            st.success("""
Learn:
- Python
- SQL
- Power BI
- Statistics
- Projects using datasets
""")

        elif "ml engineer" in q:
            st.success("""
Roadmap:
- Python
- Machine Learning
- Deep Learning
- Deployment
- Cloud
""")

        elif "cloud" in q:
            st.success("""
Cloud Path:
- AWS Basics
- EC2
- S3
- Docker
- Kubernetes
""")

        else:
            st.info("""
Improve:
- Build Projects
- Learn Missing Skills
- Practice Interviews
- Add Certifications
""")


# ---------------- DASHBOARD ----------------
def dashboard():

    page=st.sidebar.selectbox(
        "Navigation",
        [
            "Home",
            "Resume Analysis",
            "Skill Gap",
            "Job Roles",
            "AI Assistant",
            "Profile"
        ]
    )

    # HOME
    if page=="Home":

        c1,c2,c3=st.columns(3)

        with c1:
            st.metric("Employability","87%")

        with c2:
            st.metric("Missing Skills","4")

        with c3:
            st.metric("Job Matches","5")

    # RESUME
    elif page=="Resume Analysis":

        st.file_uploader("Upload Resume")
        st.text_area("Paste Job Description")

        if st.button("Analyze"):
            score=random.randint(65,95)
            st.metric("Score",f"{score}%")
            st.progress(score/100)

    # SKILL GAP
    elif page=="Skill Gap":

        skills={
            "Python":92,
            "SQL":81,
            "Cloud":52,
            "Docker":38
        }

        for s,v in skills.items():
            st.write(s)
            st.progress(v/100)

    # JOB ROLES
    elif page=="Job Roles":

        roles=[
            ("Data Analyst","92%"),
            ("ML Engineer","79%"),
            ("Cloud Engineer","74%")
        ]

        for r,m in roles:
            st.markdown(f"""
            <div class="card">
            <h2>{r}</h2>
            <h1>{m}</h1>
            </div>
            """,unsafe_allow_html=True)

    # AI ASSISTANT
    elif page=="AI Assistant":
        ai_assistant()

    # PROFILE
    elif page=="Profile":
        st.success("Logged In User")

    if st.sidebar.button("Logout"):
        st.session_state.logged_in=False
        st.rerun()


# ---------------- RUN ----------------
if st.session_state.logged_in:
    dashboard()
else:
    login_page()
