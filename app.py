import streamlit as st
from backend import register_user, login_user
import random
import pandas as pd

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="AI Employability Platform",
    page_icon="🚀",
    layout="wide"
)

# ---------------- CSS ----------------
st.markdown("""
<style>
.stApp{
background:linear-gradient(-45deg,#141e30,#243b55,#302b63,#ff512f);
background-size:400% 400%;
animation:bg 15s ease infinite;
color:white;
}

@keyframes bg{
0%{background-position:0% 50%;}
50%{background-position:100% 50%;}
100%{background-position:0% 50%;}
}

.glass{
background:rgba(255,255,255,0.12);
border-radius:25px;
backdrop-filter:blur(20px);
padding:30px;
box-shadow:0 8px 32px rgba(0,0,0,0.35);
margin:15px;
}

.glow{
text-align:center;
font-size:48px;
font-weight:bold;
animation:glow 2s infinite alternate;
}

@keyframes glow{
from{text-shadow:0 0 10px white;}
to{text-shadow:0 0 30px #ff00ff;}
}

.stButton>button{
width:100%;
background:linear-gradient(90deg,#ff512f,#dd2476);
color:white;
border:none;
border-radius:15px;
font-size:18px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SESSION ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in=False


# ---------------- LOGIN ----------------
def login_page():

    st.markdown(
        '<div class="glow">🚀 AI Employability Platform</div>',
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
        nu=st.text_input("New Username")
        np=st.text_input("New Password",type="password")

        if st.button("Register"):
            if register_user(nu,np):
                st.success("Registered")
            else:
                st.error("User Exists")


# ---------------- DASHBOARD ----------------
def dashboard():

    st.markdown(
        '<div class="glow">🎯 AI Employability Dashboard</div>',
        unsafe_allow_html=True
    )

    col1,col2=st.columns([2,2])

    with col1:
        resume=st.file_uploader(
            "Upload Resume PDF"
        )

    with col2:
        jd=st.text_area(
            "Paste Job Description"
        )

    if st.button("Analyze Resume"):

        score=random.randint(65,95)

        st.metric(
            "Employability Score",
            f"{score}%"
        )

        st.progress(score/100)

        st.write("")

        # Skill proficiency
        st.subheader("📊 Skill Proficiency")

        skills={
            "Python":90,
            "SQL":75,
            "Machine Learning":60,
            "Communication":80,
            "Cloud":55
        }

        for skill,val in skills.items():
            st.write(skill)
            st.progress(val/100)

        # Missing skills chart
        st.subheader("❌ Missing Skills")

        missing=pd.DataFrame({
            "Skill":[
                "AWS",
                "Docker",
                "Deep Learning",
                "System Design"
            ],
            "Priority":[90,75,80,65]
        })

        st.bar_chart(
            missing.set_index("Skill")
        )

        # Improvement roadmap
        st.subheader("🚀 Improvement Roadmap")

        roadmap=[
            "Learn Docker Deployment",
            "Build 2 Real-world Projects",
            "Practice SQL Queries",
            "Master AWS Basics"
        ]

        for i in roadmap:
            st.success(i)

        # Job Roles
        st.subheader("💼 Recommended Roles")

        roles=[
            "Data Analyst",
            "Backend Developer",
            "ML Engineer",
            "Cloud Associate"
        ]

        cols=st.columns(4)

        for c,r in zip(cols,roles):
            c.info(r)

    if st.button("Logout"):
        st.session_state.logged_in=False
        st.rerun()


# ---------------- RUN ----------------
if st.session_state.logged_in:
    dashboard()
else:
    login_page()
