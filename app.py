import streamlit as st
from backend import register_user, login_user
import random

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Employability Platform",
    page_icon="🚀",
    layout="wide"
)

# ---------------- CSS ----------------
st.markdown("""
<style>
.stApp{
background:linear-gradient(-45deg,#0f0c29,#302b63,#24243e,#ff512f);
background-size:400% 400%;
animation:gradient 15s ease infinite;
color:white;
}

@keyframes gradient{
0%{background-position:0% 50%;}
50%{background-position:100% 50%;}
100%{background-position:0% 50%;}
}

.glass{
background:rgba(255,255,255,0.12);
border-radius:25px;
backdrop-filter:blur(20px);
padding:30px;
box-shadow:0 8px 32px rgba(0,0,0,0.4);
margin:15px;
}

.stButton>button{
width:100%;
background:linear-gradient(90deg,#ff512f,#dd2476);
color:white;
border:none;
border-radius:15px;
font-size:18px;
}

.glow{
text-align:center;
font-size:50px;
font-weight:bold;
animation:glow 2s ease-in-out infinite alternate;
}

@keyframes glow{
from{text-shadow:0 0 10px #fff;}
to{text-shadow:0 0 30px #ff00ff;}
}
</style>
""", unsafe_allow_html=True)

# ---------------- SESSION ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# ---------------- LOGIN ----------------
def login_page():

    st.markdown(
        '<div class="glow">🚀 AI Employability Platform</div>',
        unsafe_allow_html=True
    )

    tab1, tab2 = st.tabs(["🔐 Login", "📝 Register"])

    with tab1:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if login_user(username, password):
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Invalid Credentials")

    with tab2:
        new_user = st.text_input("Create Username")
        new_pass = st.text_input(
            "Create Password",
            type="password"
        )

        if st.button("Register"):
            if register_user(new_user, new_pass):
                st.success("Registered Successfully")
            else:
                st.error("User Exists")


# ---------------- DASHBOARD ----------------
def dashboard():

    st.markdown(
        '<div class="glow">🎯 Dashboard</div>',
        unsafe_allow_html=True
    )

    resume = st.file_uploader(
        "Upload Resume PDF"
    )

    jd = st.text_area(
        "Paste Job Description"
    )

    if st.button("Analyze Resume"):

        score = random.randint(60,95)

        missing_skills = [
            "Python",
            "SQL",
            "Machine Learning"
        ]

        improvements = [
            "Improve problem solving",
            "Add real-world projects",
            "Learn cloud deployment"
        ]

        roles = [
            "Data Analyst",
            "ML Engineer",
            "Backend Developer"
        ]

        # SCORE
        st.markdown(
            f"""
            <div class="glass">
            <h1>📊 Employability Score: {score}%</h1>
            </div>
            """,
            unsafe_allow_html=True
        )

        col1,col2,col3=st.columns(3)

        with col1:
            st.markdown("""
            <div class="glass">
            <h2>❌ Missing Skills</h2>
            """,unsafe_allow_html=True)

            for i in missing_skills:
                st.write("•",i)

            st.markdown("</div>",
                        unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div class="glass">
            <h2>🚀 Improvements</h2>
            """,unsafe_allow_html=True)

            for i in improvements:
                st.write("•",i)

            st.markdown("</div>",
                        unsafe_allow_html=True)

        with col3:
            st.markdown("""
            <div class="glass">
            <h2>💼 Suggested Roles</h2>
            """,unsafe_allow_html=True)

            for i in roles:
                st.write("•",i)

            st.markdown("</div>",
                        unsafe_allow_html=True)

    if st.button("Logout"):
        st.session_state.logged_in=False
        st.rerun()


# ---------------- RUN ----------------
if st.session_state.logged_in:
    dashboard()
else:
    login_page()
