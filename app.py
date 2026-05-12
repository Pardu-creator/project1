import streamlit as st
from backend import register_user, login_user
import random
import pandas as pd

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="AI Employability",
    page_icon="⚡",
    layout="wide"
)

# ---------------- NEW DESIGN ----------------
st.markdown("""
<style>

.stApp{
background:#0b0f19;
color:white;
}

/* Sidebar */
section[data-testid="stSidebar"]{
background:#111827;
border-right:2px solid #00f7ff;
}

/* Cards */
.card{
background:#111827;
padding:25px;
border-radius:18px;
border:1px solid #00f7ff55;
box-shadow:0 0 20px #00f7ff22;
transition:0.4s;
}

.card:hover{
transform:translateY(-8px);
box-shadow:0 0 35px #00f7ff88;
}

/* Title */
.title{
font-size:42px;
font-weight:800;
color:#00f7ff;
text-align:center;
margin-bottom:30px;
}

/* Buttons */
.stButton>button{
background:#00f7ff;
color:black;
font-weight:bold;
border:none;
border-radius:12px;
width:100%;
}

/* Inputs */
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
        ["Login","Register"]
    )

    if menu == "Login":

        u = st.text_input("Username")
        p = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Login"):
            if login_user(u,p):
                st.session_state.logged_in=True
                st.rerun()
            else:
                st.error("Invalid login")

    else:

        u = st.text_input("Create Username")
        p = st.text_input(
            "Create Password",
            type="password"
        )

        if st.button("Register"):
            if register_user(u,p):
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

    # Resume
    if page == "Resume Analysis":

        st.markdown('<div class="card">',unsafe_allow_html=True)

        st.file_uploader(
            "Upload Resume PDF"
        )

        st.text_area(
            "Paste Job Description"
        )

        if st.button("Analyze Resume"):

            score=random.randint(65,95)

            st.metric(
                "Employability Score",
                f"{score}%"
            )

            st.progress(score/100)

        st.markdown('</div>',unsafe_allow_html=True)

    # Skill Gap
    elif page=="Skill Gap":

        st.markdown('<div class="card">',unsafe_allow_html=True)

        skills={
            "Python":85,
            "SQL":72,
            "Machine Learning":55,
            "Cloud":45
        }

        for k,v in skills.items():
            st.write(k)
            st.progress(v/100)

        st.markdown('</div>',unsafe_allow_html=True)

    # Job Roles
    else:

        roles=pd.DataFrame({
            "Roles":[
                "Data Analyst",
                "ML Engineer",
                "Cloud Associate",
                "Backend Developer"
            ]
        })

        st.markdown('<div class="card">',unsafe_allow_html=True)

        st.table(roles)

        st.markdown('</div>',unsafe_allow_html=True)

    if st.sidebar.button("Logout"):
        st.session_state.logged_in=False
        st.rerun()


# ---------------- RUN ----------------
if st.session_state.logged_in:
    dashboard()
else:
    login_page()
