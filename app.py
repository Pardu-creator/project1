import streamlit as st
from backend import register_user, login_user
import random

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Employability Platform",
    page_icon="⚡",
    layout="wide"
)

# ---------------- CSS ----------------
st.markdown("""
<style>
.stApp{
    background:#0b0f19;
    color:white;
}

section[data-testid="stSidebar"]{
    background:#111827;
    border-right:2px solid #00f7ff;
}

.card{
    background:#111827;
    padding:25px;
    border-radius:18px;
    border:1px solid #00f7ff55;
    box-shadow:0 0 20px #00f7ff22;
    transition:0.4s;
    margin:15px 0;
}

.card:hover{
    transform:translateY(-8px);
    box-shadow:0 0 35px #00f7ff88;
}

.title{
    font-size:42px;
    font-weight:800;
    color:#00f7ff;
    text-align:center;
    margin-bottom:30px;
}

.stButton>button{
    background:#00f7ff;
    color:black;
    font-weight:bold;
    border:none;
    border-radius:12px;
    width:100%;
}

.stTextInput input,
textarea{
    background:#1f2937 !important;
    color:white !important;
    border-radius:12px !important;
    border:1px solid #00f7ff !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SESSION ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# ---------------- LOGIN ----------------
def login_page():

    st.markdown(
        '<div class="title">⚡ AI Employability Platform</div>',
        unsafe_allow_html=True
    )

    menu = st.sidebar.radio(
        "Menu",
        ["Login", "Register"]
    )

    if menu == "Login":

        u = st.text_input("Username")
        p = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Login"):
            if login_user(u, p):
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Invalid Login")

    else:

        u = st.text_input("Create Username")
        p = st.text_input(
            "Create Password",
            type="password"
        )

        if st.button("Register"):
            if register_user(u, p):
                st.success("Registered Successfully")
            else:
                st.error("User Exists")


# ---------------- DASHBOARD ----------------
def dashboard():

    st.markdown(
        '<div class="title">⚡ Employability Analytics</div>',
        unsafe_allow_html=True
    )

    page = st.sidebar.radio(
        "Dashboard",
        [
            "Resume Analysis",
            "Skill Gap",
            "Job Roles"
        ]
    )

    # ---------------- RESUME ----------------
    if page == "Resume Analysis":

        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.file_uploader("Upload Resume PDF")
        st.text_area("Paste Job Description")

        if st.button("Analyze Resume"):

            score = random.randint(65,95)

            st.metric(
                "Employability Score",
                f"{score}%"
            )

            st.progress(score/100)

        st.markdown('</div>', unsafe_allow_html=True)

    # ---------------- SKILL GAP ----------------
    elif page == "Skill Gap":

        st.subheader("📊 Skill Gap Heatmap")

        col1,col2 = st.columns(2)

        skills = {
            "Python":85,
            "SQL":70,
            "Machine Learning":55,
            "Cloud":45,
            "Docker":35,
            "System Design":25
        }

        with col1:
            for skill,val in list(skills.items())[:3]:
                st.markdown(
                    f"""
                    <div class="card">
                    <h3>{skill}</h3>
                    <h2>{val}%</h2>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        with col2:
            for skill,val in list(skills.items())[3:]:
                st.markdown(
                    f"""
                    <div class="card">
                    <h3>{skill}</h3>
                    <h2>{val}%</h2>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        st.write("### 🚀 Recommended Improvements")

        improve = [
            "Complete AWS Certification",
            "Build Dockerized Projects",
            "Practice SQL Joins",
            "Master API Development"
        ]

        for i in improve:
            st.success(i)

    # ---------------- JOB ROLES ----------------
    elif page == "Job Roles":

        st.subheader("💼 AI Recommended Roles")

        roles = [
            {"role":"Data Analyst","match":"92%"},
            {"role":"Backend Developer","match":"88%"},
            {"role":"ML Engineer","match":"79%"},
            {"role":"Cloud Associate","match":"72%"}
        ]

        cols = st.columns(2)

        for idx,r in enumerate(roles):

            with cols[idx % 2]:

                st.markdown(
                    f"""
                    <div class="card">
                    <h2>{r['role']}</h2>
                    <h1>{r['match']}</h1>
                    <p>Role Match Accuracy</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()


# ---------------- RUN ----------------
if st.session_state.logged_in:
    dashboard()
else:
    login_page()
