import streamlit as st
from backend import register_user, login_user
import random

st.set_page_config(
    page_title="Glass Cosmos AI",
    page_icon="⚡",
    layout="wide"
)

# ---------------- PREMIUM CSS ----------------
st.markdown("""
<style>

.stApp{
background:
radial-gradient(circle at top left,#00eaff22,transparent 25%),
radial-gradient(circle at bottom right,#8b5cf622,transparent 25%),
linear-gradient(135deg,#020617,#0f172a,#111827);
color:white;
overflow:hidden;
}

/* Floating orbs */
.orb{
position:absolute;
border-radius:50%;
filter:blur(100px);
opacity:.25;
animation:float 12s infinite ease-in-out;
}

.o1{
width:320px;height:320px;
background:#00eaff;
top:10%;left:5%;
}

.o2{
width:400px;height:400px;
background:#8b5cf6;
bottom:5%;right:5%;
animation-delay:4s;
}

@keyframes float{
0%,100%{transform:translateY(0);}
50%{transform:translateY(-60px);}
}

.card{
background:rgba(255,255,255,.08);
backdrop-filter:blur(30px);
padding:30px;
border-radius:28px;
border:1px solid rgba(255,255,255,.12);
margin:15px 0;
box-shadow:0 0 30px rgba(0,234,255,.12);
transition:.4s;
}

.card:hover{
transform:translateY(-8px);
box-shadow:0 0 55px rgba(0,234,255,.25);
}

.hero{
font-size:76px;
font-weight:900;
background:linear-gradient(90deg,#00eaff,#8b5cf6,#fff);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

.subhero{
font-size:20px;
color:#cbd5e1;
line-height:1.8;
}

.stButton>button{
width:100%;
height:55px;
border:none;
border-radius:18px;
font-weight:800;
background:linear-gradient(90deg,#00eaff,#8b5cf6);
color:white;
box-shadow:0 0 25px #00eaff55;
}

.stButton>button:hover{
transform:scale(1.03);
box-shadow:0 0 40px #00eaffaa;
}

.stTextInput input,
textarea{
background:rgba(255,255,255,.06)!important;
color:white!important;
border:1px solid #00eaff!important;
border-radius:18px!important;
}

section[data-testid="stSidebar"]{
background:rgba(15,23,42,.95);
backdrop-filter:blur(25px);
}

</style>

<div class="orb o1"></div>
<div class="orb o2"></div>
""",unsafe_allow_html=True)

# ---------------- SESSION ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in=False


# ---------------- LOGIN ----------------
def login_page():

    left,right=st.columns([1.6,1])

    with left:
        st.markdown("""
        <div style="
        height:95vh;
        display:flex;
        flex-direction:column;
        justify-content:center;
        padding-left:50px;
        ">

        <div class="hero">Glass Cosmos</div>

        <div class="subhero">
        The next-generation employability intelligence platform.

        <br><br>

        • Resume Intelligence  
        • Skill Gap Forecasting  
        • AI Career Optimization  
        • Placement Prediction  
        • Learning Acceleration
        </div>

        </div>
        """,unsafe_allow_html=True)

    with right:

        st.markdown('<div class="card">',unsafe_allow_html=True)

        st.markdown("<h2>Secure Access</h2>",unsafe_allow_html=True)

        tab1,tab2=st.tabs(["🔐 Login","✨ Register"])

        with tab1:
            u=st.text_input("Username",key="l1")
            p=st.text_input("Password",type="password",key="l2")

            if st.button("Login"):
                if login_user(u,p):
                    st.session_state.logged_in=True
                    st.rerun()
                else:
                    st.error("Invalid Login")

        with tab2:
            u=st.text_input("Create Username",key="r1")
            p=st.text_input("Create Password",type="password",key="r2")

            if st.button("Register"):
                if register_user(u,p):
                    st.success("Registered")
                else:
                    st.error("User Exists")

        st.markdown("</div>",unsafe_allow_html=True)


# ---------------- DASHBOARD ----------------
def dashboard():

    page=st.sidebar.selectbox("Navigation",[
        "🏠 Executive Dashboard",
        "📄 Resume Scanner",
        "📊 Skill Matrix",
        "💼 Career Engine",
        "🛣 Learning Roadmap",
        "👤 Profile"
    ])

    if page=="🏠 Executive Dashboard":

        st.markdown('<div class="hero">Dashboard</div>',
        unsafe_allow_html=True)

        c1,c2,c3,c4=st.columns(4)

        c1.metric("Employability","91%","+8%")
        c2.metric("Skills Matched","14","+5")
        c3.metric("Job Matches","18","+6")
        c4.metric("Placement Chance","89%","+10%")

        st.markdown("""
        <div class="card">
        <h2>AI Executive Insight</h2>
        <p>
        Strong backend and data capability.
        Improve AWS + deployment to unlock senior opportunities.
        </p>
        </div>
        """,unsafe_allow_html=True)

    elif page=="📄 Resume Scanner":

        st.file_uploader("Upload Resume")
        st.text_area("Paste JD")

        if st.button("Analyze"):

            score=random.randint(70,96)

            st.metric("Resume Match",f"{score}%")
            st.progress(score/100)

            st.success("Excellent Python + SQL")

    elif page=="📊 Skill Matrix":

        skills={
            "Python":94,
            "SQL":87,
            "ML":78,
            "Cloud":58,
            "Docker":44
        }

        for s,v in skills.items():
            st.write(f"{s} • {v}%")
            st.progress(v/100)

    elif page=="💼 Career Engine":

        roles=[
            ("Senior Data Analyst","94%"),
            ("Backend Engineer","90%"),
            ("ML Engineer","82%"),
            ("Cloud Engineer","74%")
        ]

        for r,m in roles:
            st.markdown(f"""
            <div class="card">
            <h2>{r}</h2>
            <h1>{m}</h1>
            </div>
            """,unsafe_allow_html=True)

    elif page=="🛣 Learning Roadmap":

        for x in [
            "Week 1 → SQL Advanced",
            "Week 2 → Docker",
            "Week 3 → AWS",
            "Week 4 → Deployment"
        ]:
            st.success(x)

    elif page=="👤 Profile":

        st.markdown("""
        <div class="card">
        <h2>Performance Analytics</h2>
        <p>Consistency: Excellent</p>
        <p>Career Momentum: Rising</p>
        <p>Placement Readiness: High</p>
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
