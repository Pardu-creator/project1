import streamlit as st
from backend import register_user, login_user

st.set_page_config(
    page_title="AI Employability",
    page_icon="⚡",
    layout="wide"
)

# ---------------- ADVANCED ANIMATION CSS ----------------
st.markdown("""
<style>

.stApp{
    background:linear-gradient(-45deg,#020617,#0f172a,#111827,#1e293b);
    background-size:400% 400%;
    animation:bgmove 15s ease infinite;
    overflow:hidden;
}

@keyframes bgmove{
0%{background-position:0% 50%;}
50%{background-position:100% 50%;}
100%{background-position:0% 50%;}
}

/* floating blobs */
.blob{
position:absolute;
border-radius:50%;
filter:blur(70px);
animation:float 12s infinite ease-in-out;
opacity:0.45;
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
50%{transform:translateY(-70px);}
}

/* login glass card */
.login-card{
background:rgba(255,255,255,0.07);
backdrop-filter:blur(28px);
border:1px solid rgba(255,255,255,0.15);
padding:45px;
border-radius:28px;
box-shadow:0 0 50px rgba(0,234,255,0.25);
animation:pulse 4s infinite;
}

@keyframes pulse{
0%,100%{box-shadow:0 0 30px rgba(0,234,255,0.18);}
50%{box-shadow:0 0 70px rgba(0,234,255,0.45);}
}

.hero{
font-size:72px;
font-weight:900;
background:linear-gradient(90deg,#00eaff,#8b5cf6);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
animation:glow 3s infinite alternate;
}

@keyframes glow{
from{text-shadow:0 0 20px #00eaff;}
to{text-shadow:0 0 45px #8b5cf6;}
}

.subtitle{
font-size:22px;
color:#cbd5e1;
line-height:1.7;
}

.stTextInput input{
background:#0f172a !important;
color:white !important;
border:1px solid #00eaff !important;
border-radius:16px !important;
height:52px;
}

.stButton>button{
width:100%;
height:52px;
border:none;
border-radius:16px;
font-size:18px;
font-weight:800;
background:linear-gradient(90deg,#00eaff,#8b5cf6);
color:white;
transition:.3s;
}

.stButton>button:hover{
transform:scale(1.03);
box-shadow:0 0 35px #00eaff;
}

section[data-testid="stSidebar"]{
display:none;
}

</style>

<div class="blob blob1"></div>
<div class="blob blob2"></div>

""", unsafe_allow_html=True)


# ---------------- SESSION ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# ---------------- LOGIN PAGE ----------------
def login_page():

    left,right = st.columns([1.35,1])

    with left:

        st.markdown("""
        <div style="
        height:95vh;
        display:flex;
        flex-direction:column;
        justify-content:center;
        padding-left:40px;
        ">

        <div class="hero">
        AI Employability
        </div>

        <br>

        <div class="subtitle">
        Advanced AI-powered employability intelligence platform.

        <br><br>

        • Resume Intelligence Engine  
        • Skill Gap Prediction  
        • Placement Readiness Analytics  
        • AI Job Role Matching  
        • Career Growth Insights

        </div>

        </div>
        """, unsafe_allow_html=True)

    with right:

        st.markdown('<div style="margin-top:90px;" class="login-card">', unsafe_allow_html=True)

        st.markdown("""
        <h1 style="
        text-align:center;
        color:white;
        font-weight:900;">
        Welcome Back
        </h1>
        """, unsafe_allow_html=True)

        tab1,tab2=st.tabs(["🔐 Login","✨ Register"])

        with tab1:

            u=st.text_input("Username")
            p=st.text_input("Password",type="password")

            if st.button("Secure Login"):

                if login_user(u,p):
                    st.success("Access Granted")
                    st.session_state.logged_in=True
                    st.rerun()
                else:
                    st.error("Invalid Credentials")

        with tab2:

            nu=st.text_input("Create Username")
            np=st.text_input("Create Password",type="password")

            if st.button("Create Account"):

                if register_user(nu,np):
                    st.success("Registered Successfully")
                else:
                    st.error("Username Exists")

        st.markdown("</div>", unsafe_allow_html=True)


# ---------------- DASHBOARD ----------------
def dashboard():
    st.success("Login Successful 🚀")
    if st.button("Logout"):
        st.session_state.logged_in=False
        st.rerun()


# ---------------- RUN ----------------
if st.session_state.logged_in:
    dashboard()
else:
    login_page()
