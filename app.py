import streamlit as st
from backend import register_user, login_user
import random

# ---------------- PAGE ----------------
st.set_page_config(
    page_title="AI Employability",
    page_icon="⚡",
    layout="wide"
)

# ---------------- CSS ----------------
st.markdown("""
<style>

.stApp{
background:linear-gradient(135deg,#020617,#0f172a,#111827);
color:white;
}

.card{
background:rgba(255,255,255,.06);
padding:25px;
border-radius:20px;
margin:15px 0;
border:1px solid #00eaff33;
}

.hero{
font-size:60px;
font-weight:900;
color:#00eaff;
}

.stButton>button{
width:100%;
height:50px;
background:linear-gradient(90deg,#00eaff,#8b5cf6);
color:white;
font-weight:bold;
border:none;
border-radius:14px;
}

.stTextInput input,
textarea{
background:#1e293b !important;
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

    left,right=st.columns([1.3,1])

    with left:

        st.markdown("""
        <div style="
        height:90vh;
        display:flex;
        flex-direction:column;
        justify-content:center;">

        <div class="hero">
        AI Employability
        </div>

        <h3>Career Intelligence Platform</h3>

        <p>
        Analyze resumes, predict employability,
        detect skill gaps and get AI guidance.
        </p>

        </div>
        """,unsafe_allow_html=True)

    with right:

        st.markdown('<div class="card">',
                    unsafe_allow_html=True)

        tab1,tab2=st.tabs([
            "🔐 Login",
            "✨ Register"
        ])

        # LOGIN
        with tab1:

            user=st.text_input(
                "Username",
                key="login_user"
            )

            pwd=st.text_input(
                "Password",
                type="password",
                key="login_pass"
            )

            if st.button("Secure Login"):

                if login_user(user,pwd):
                    st.session_state.logged_in=True
                    st.rerun()
                else:
                    st.error("Invalid Login")

        # REGISTER
        with tab2:

            user=st.text_input(
                "New Username",
                key="reg_user"
            )

            pwd=st.text_input(
                "New Password",
                type="password",
                key="reg_pass"
            )

            if st.button("Create Account"):

                if register_user(user,pwd):
                    st.success("Registered")
                else:
                    st.error("User Exists")

        st.markdown("</div>",
                    unsafe_allow_html=True)


# ---------------- AI ASSISTANT ----------------
def ai_assistant():

    st.subheader("🤖 Career AI Assistant")

    q=st.text_input("Ask a Question")

    if st.button("Ask AI"):

        q=q.lower()

        if "data analyst" in q:
            st.success("""
Learn:
- Python
- SQL
- Power BI
- Data Visualization
""")

        elif "ml" in q:
            st.success("""
Roadmap:
- Python
- Machine Learning
- Deep Learning
- Deployment
""")

        elif "cloud" in q:
            st.success("""
Cloud:
- AWS
- Docker
- Kubernetes
""")

        else:
            st.info("""
Build projects and improve skills.
""")


# ---------------- DASHBOARD ----------------
def dashboard():

    page=st.sidebar.selectbox(
        "Navigation",
        [
            "🏠 Home",
            "📄 Resume Analysis",
            "📊 Skill Gap",
            "💼 Job Roles",
            "🤖 AI Assistant"
        ]
    )

    # HOME
    if page=="🏠 Home":

        c1,c2,c3=st.columns(3)

        c1.metric("Employability","87%")
        c2.metric("Missing Skills","4")
        c3.metric("Jobs Matched","5")

    # RESUME
    elif page=="📄 Resume Analysis":

        st.file_uploader("Upload Resume")
        st.text_area("Paste Job Description")

        if st.button("Analyze"):

            score=random.randint(65,95)

            st.metric(
                "Employability Score",
                f"{score}%"
            )

            st.progress(score/100)

    # SKILL GAP
    elif page=="📊 Skill Gap":

        skills={
            "Python":92,
            "SQL":80,
            "Cloud":55,
            "Docker":35
        }

        for s,v in skills.items():

            st.write(s)
            st.progress(v/100)

    # JOB ROLES
    elif page=="💼 Job Roles":

        roles=[
            ("Data Analyst","92%"),
            ("ML Engineer","79%"),
            ("Cloud Engineer","72%")
        ]

        for r,m in roles:

            st.markdown(f"""
            <div class="card">
            <h2>{r}</h2>
            <h1>{m}</h1>
            </div>
            """,unsafe_allow_html=True)

    # AI
    elif page=="🤖 AI Assistant":
        ai_assistant()

    if st.sidebar.button("Logout"):
        st.session_state.logged_in=False
        st.rerun()


# ---------------- RUN ----------------
if st.session_state.logged_in:
    dashboard()
else:
    login_page()
