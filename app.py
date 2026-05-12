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
backdrop-filter:blur(20px);
padding:25px;
border-radius:20px;
margin:15px 0;
border:1px solid rgba(255,255,255,.15);
}

.hero{
font-size:70px;
font-weight:900;
background:linear-gradient(90deg,#00eaff,#8b5cf6);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

.stButton>button{
width:100%;
height:50px;
border:none;
border-radius:14px;
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
        Resume analysis, skill gap prediction,
        employability scoring and AI career guidance.
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

        with tab1:

            u=st.text_input(
                "Username",
                key="login_user"
            )

            p=st.text_input(
                "Password",
                type="password",
                key="login_pass"
            )

            if st.button("Secure Login"):

                if login_user(u,p):
                    st.session_state.logged_in=True
                    st.rerun()
                else:
                    st.error("Invalid Login")

        with tab2:

            u=st.text_input(
                "Create Username",
                key="reg_user"
            )

            p=st.text_input(
                "Create Password",
                type="password",
                key="reg_pass"
            )

            if st.button("Create Account"):

                if register_user(u,p):
                    st.success("Registered")
                else:
                    st.error("User Exists")

        st.markdown("</div>",
                    unsafe_allow_html=True)


# ---------------- AI ----------------
def ai_assistant():

    st.subheader("🤖 Career AI Assistant")

    q=st.text_input("Ask Career Question")

    if st.button("Ask AI"):

        q=q.lower()

        if "data analyst" in q:
            st.success("Learn Python, SQL, Power BI")

        elif "ml" in q:
            st.success("Learn ML, Deep Learning, Deployment")

        elif "cloud" in q:
            st.success("Learn AWS, Docker, Kubernetes")

        else:
            st.info("Build projects and improve skills")


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
        c3.metric("Job Matches","5")

    # RESUME
    elif page=="📄 Resume Analysis":

        st.file_uploader("Upload Resume")
        st.text_area("Paste Job Description")

        if st.button("Analyze Resume"):

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
            "SQL":81,
            "Cloud":55,
            "Docker":38
        }

        for s,v in skills.items():
            st.write(s)
            st.progress(v/100)

    # JOB ROLES
    elif page=="💼 Job Roles":

        roles=[
            ("Data Analyst","92%"),
            ("ML Engineer","80%"),
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
