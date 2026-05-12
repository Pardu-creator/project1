import streamlit as st
from backend import register_user, login_user
import random

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Employability Platform",
    page_icon="⚡",
    layout="wide"
)

# ---------------- STYLING ----------------
st.markdown("""
<style>
.stApp{
    background:#0a0f1f;
    color:white;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:linear-gradient(180deg,#111827,#0f172a);
    border-right:2px solid #00eaff;
    padding-top:20px;
}

/* Sidebar text */
.css-1d391kg {
    color:white;
}

/* Cards */
.card{
    background:#111827;
    padding:25px;
    border-radius:20px;
    border:1px solid #00eaff55;
    box-shadow:0 0 20px #00eaff22;
    margin:15px 0;
}

/* Title */
.title{
    font-size:42px;
    font-weight:800;
    color:#00eaff;
    text-align:center;
    margin-bottom:30px;
}

/* Buttons */
.stButton>button{
    width:100%;
    background:#00eaff;
    color:black;
    font-weight:bold;
    border:none;
    border-radius:12px;
}

/* Inputs */
.stTextInput input,
textarea{
    background:#1f2937 !important;
    color:white !important;
    border-radius:12px !important;
    border:1px solid #00eaff !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SESSION ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in=False


# ---------------- LOGIN ----------------
def login_page():

    st.markdown(
        '<div class="title">⚡ AI Employability Platform</div>',
        unsafe_allow_html=True
    )

    tab1,tab2=st.tabs(["🔐 Login","📝 Register"])

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
                st.success("Registered Successfully")
            else:
                st.error("User Exists")


# ---------------- DASHBOARD ----------------
def dashboard():

    st.sidebar.markdown("## ⚡ Navigation")

    page = st.sidebar.selectbox(
        "Choose Section",
        [
            "🏠 Home",
            "📄 Resume Analysis",
            "📊 Skill Gap",
            "💼 Job Roles",
            "⚙ Profile"
        ]
    )

    st.markdown(
        '<div class="title">AI Employability Dashboard</div>',
        unsafe_allow_html=True
    )

    # ---------------- HOME ----------------
    if page=="🏠 Home":

        col1,col2,col3=st.columns(3)

        with col1:
            st.markdown("""
            <div class="card">
            <h2>📈 Score</h2>
            <h1>87%</h1>
            </div>
            """,unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div class="card">
            <h2>❌ Missing Skills</h2>
            <h1>4</h1>
            </div>
            """,unsafe_allow_html=True)

        with col3:
            st.markdown("""
            <div class="card">
            <h2>💼 Roles</h2>
            <h1>5</h1>
            </div>
            """,unsafe_allow_html=True)

    # ---------------- RESUME ----------------
    elif page=="📄 Resume Analysis":

        st.file_uploader("Upload Resume PDF")
        st.text_area("Paste Job Description")

        if st.button("Analyze"):
            score=random.randint(65,95)
            st.metric("Employability Score",f"{score}%")
            st.progress(score/100)

    # ---------------- SKILL GAP ----------------
    elif page=="📊 Skill Gap":

        skills={
            "Python":85,
            "SQL":70,
            "Machine Learning":55,
            "Cloud":45
        }

        for k,v in skills.items():
            st.write(k)
            st.progress(v/100)

    # ---------------- JOB ROLES ----------------
    elif page=="💼 Job Roles":

        roles=[
            "Data Analyst",
            "Backend Developer",
            "ML Engineer",
            "Cloud Associate"
        ]

        for r in roles:
            st.markdown(
                f"""
                <div class="card">
                <h2>{r}</h2>
                </div>
                """,
                unsafe_allow_html=True
            )

    # ---------------- PROFILE ----------------
    elif page=="⚙ Profile":

        st.markdown("""
        <div class="card">
        <h2>User Profile</h2>
        <p>Username: Active User</p>
        <p>Status: Logged In</p>
        </div>
        """,unsafe_allow_html=True)

    if st.sidebar.button("🚪 Logout"):
        st.session_state.logged_in=False
        st.rerun()


# ---------------- RUN ----------------
if st.session_state.logged_in:
    dashboard()
else:
    login_page()
