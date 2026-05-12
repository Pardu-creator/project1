import streamlit as st
from backend import register_user, login_user
import random

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Employability Platform",
    page_icon="⚡",
    layout="wide"
)

# ---------------- HIGH-END CSS ----------------
st.markdown("""
<style>

.stApp{
background:linear-gradient(-45deg,#020617,#0f172a,#111827,#1e293b);
background-size:400% 400%;
animation:bgmove 15s ease infinite;
overflow:hidden;
color:white;
}

@keyframes bgmove{
0%{background-position:0% 50%;}
50%{background-position:100% 50%;}
100%{background-position:0% 50%;}
}

.blob{
position:absolute;
border-radius:50%;
filter:blur(80px);
animation:float 14s infinite ease-in-out;
opacity:.45;
}

.blob1{
width:300px;
height:300px;
background:#00eaff;
top:5%;
left:8%;
}

.blob2{
width:350px;
height:350px;
background:#8b5cf6;
bottom:10%;
right:8%;
animation-delay:4s;
}

@keyframes float{
0%,100%{transform:translateY(0px);}
50%{transform:translateY(-80px);}
}

.login-card,.card{
background:rgba(255,255,255,.06);
backdrop-filter:blur(28px);
padding:35px;
border-radius:24px;
border:1px solid rgba(255,255,255,.12);
box-shadow:0 0 35px rgba(0,234,255,.15);
margin:15px 0;
transition:.4s;
}

.card:hover{
transform:translateY(-8px);
box-shadow:0 0 45px rgba(0,234,255,.35);
}

.hero{
font-size:70px;
font-weight:900;
background:linear-gradient(90deg,#00eaff,#8b5cf6);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

.subtitle{
font-size:20px;
color:#cbd5e1;
line-height:1.7;
}

.stButton>button{
width:100%;
height:50px;
border:none;
border-radius:16px;
font-size:16px;
font-weight:800;
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

.title{
font-size:42px;
font-weight:900;
text-align:center;
color:#00eaff;
}

section[data-testid="stSidebar"]{
background:#0f172a;
border-right:2px solid #00eaff;
}

</style>

<div class="blob blob1"></div>
<div class="blob blob2"></div>
""", unsafe_allow_html=True)

# ---------------- SESSION ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in=False


# ---------------- LOGIN PAGE ----------------
def login_page():

    left,right=st.columns([1.35,1])

    with left:
        st.markdown("""
        <div style="
        height:95vh;
        display:flex;
        flex-direction:column;
        justify-content:center;
        padding-left:40px;">

        <div class="hero">
        AI Employability
        </div>

        <br>

        <div class="subtitle">
        AI-powered employability intelligence platform.

        <br><br>

        • Resume Intelligence Engine  
        • Skill Gap Prediction  
        • Placement Analytics  
        • AI Job Role Matching  
        • Career Growth Insights
        </div>

        </div>
        """, unsafe_allow_html=True)

    with right:

        st.markdown('<div class="login-card">',
                    unsafe_allow_html=True)

        st.markdown("""
        <h1 style="text-align:center;">
        Welcome Back
        </h1>
        """,unsafe_allow_html=True)

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
            nu=st.text_input("Create Username")
            np=st.text_input("Create Password",
                             type="password")

            if st.button("Create Account"):
                if register_user(nu,np):
                    st.success("Registered")
                else:
                    st.error("User Exists")

        st.markdown("</div>",
                    unsafe_allow_html=True)


# ---------------- DASHBOARD ----------------
def dashboard():

    st.sidebar.markdown("## ⚡ Navigation")

    page=st.sidebar.selectbox(
        "Choose",
        [
            "🏠 Home",
            "📄 Resume Analysis",
            "📊 Skill Gap",
            "💼 Job Roles",
            "⚙ Profile"
        ]
    )

    st.markdown(
        '<div class="title">AI Dashboard</div>',
        unsafe_allow_html=True
    )

    # HOME
    if page=="🏠 Home":

        c1,c2,c3=st.columns(3)

        with c1:
            st.markdown("""
            <div class="card">
            <h2>Employability</h2>
            <h1>87%</h1>
            </div>
            """,unsafe_allow_html=True)

        with c2:
            st.markdown("""
            <div class="card">
            <h2>Missing Skills</h2>
            <h1>4</h1>
            </div>
            """,unsafe_allow_html=True)

        with c3:
            st.markdown("""
            <div class="card">
            <h2>Job Roles</h2>
            <h1>5</h1>
            </div>
            """,unsafe_allow_html=True)

    # RESUME
    elif page=="📄 Resume Analysis":

        st.file_uploader("Upload Resume PDF")
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
            "Machine Learning":67,
            "Cloud":52,
            "Docker":38,
            "System Design":29
        }

        for s,v in skills.items():

            status=(
                "✅ Strong"
                if v>80 else
                "⚠ Moderate"
                if v>55 else
                "❌ Weak"
            )

            st.markdown(f"""
            <div class="card">
            <h3>{s}</h3>
            <h2>{v}%</h2>
            <p>{status}</p>
            </div>
            """,unsafe_allow_html=True)

        st.write("### Improvement Roadmap")

        for r in [
            "Master Docker",
            "Learn AWS",
            "Practice SQL",
            "Study System Design"
        ]:
            st.success(r)

    # JOB ROLES
    elif page=="💼 Job Roles":

        roles=[
            ("Data Analyst","92%"),
            ("Backend Developer","88%"),
            ("ML Engineer","79%"),
            ("Cloud Associate","72%")
        ]

        for role,match in roles:

            st.markdown(f"""
            <div class="card">
            <h2>{role}</h2>
            <h1>{match}</h1>
            </div>
            """,unsafe_allow_html=True)

    # PROFILE
    elif page=="⚙ Profile":

        st.markdown("""
        <div class="card">
        <h2>User Profile</h2>
        <p>Status: Logged In</p>
        <p>Platform: AI Skill Assessment</p>
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
