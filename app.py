import streamlit as st
from backend import register_user, login_user

st.set_page_config(
    page_title="AI Employability",
    page_icon="⚡",
    layout="wide"
)

# ---------------- ADVANCED CSS ----------------
st.markdown("""
<style>

.stApp{
background:linear-gradient(-45deg,#020617,#0f172a,#111827,#1e293b);
background-size:400% 400%;
animation:bgmove 14s ease infinite;
overflow:hidden;
color:white;
}

@keyframes bgmove{
0%{background-position:0% 50%;}
50%{background-position:100% 50%;}
100%{background-position:0% 50%;}
}

.glow{
position:absolute;
width:450px;
height:450px;
border-radius:50%;
filter:blur(100px);
opacity:.35;
animation:float 8s infinite ease-in-out;
}

.g1{
background:#00eaff;
top:-80px;
left:-100px;
}

.g2{
background:#8b5cf6;
bottom:-100px;
right:-80px;
animation-delay:3s;
}

@keyframes float{
0%,100%{transform:translateY(0px);}
50%{transform:translateY(-60px);}
}

.login-card{
background:rgba(255,255,255,.08);
backdrop-filter:blur(25px);
padding:45px;
border-radius:28px;
border:1px solid rgba(255,255,255,.12);
box-shadow:0 0 45px rgba(0,234,255,.18);
}

.hero{
font-size:78px;
font-weight:900;
background:linear-gradient(90deg,#00eaff,#8b5cf6);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

.sub{
font-size:20px;
color:#cbd5e1;
line-height:1.8;
}

.stTextInput input{
background:#0f172a !important;
color:white !important;
border:1px solid #00eaff !important;
border-radius:16px !important;
height:50px;
}

.stButton>button{
width:100%;
height:52px;
border:none;
border-radius:16px;
font-weight:800;
font-size:16px;
background:linear-gradient(90deg,#00eaff,#8b5cf6);
color:white;
transition:.4s;
}

.stButton>button:hover{
transform:scale(1.03);
box-shadow:0 0 25px #00eaff;
}

</style>

<div class="glow g1"></div>
<div class="glow g2"></div>
""",unsafe_allow_html=True)

# ---------------- SESSION ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in=False


# ---------------- LOGIN PAGE ----------------
def login_page():

    left,right=st.columns([1.5,1])

    with left:

        st.markdown("""
        <div style="
        height:95vh;
        display:flex;
        flex-direction:column;
        justify-content:center;
        padding-left:50px;">

        <div class="hero">
        AI Employability
        </div>

        <br>

        <div class="sub">
        Next-generation career intelligence platform.

        <br><br>

        • Resume Intelligence Engine  
        • Skill Gap Detection  
        • Employability Prediction  
        • AI Career Assistant  
        • Placement Optimization
        </div>

        </div>
        """,unsafe_allow_html=True)

    with right:

        st.markdown(
            '<div class="login-card">',
            unsafe_allow_html=True
        )

        st.markdown("""
        <h1 style="text-align:center;">
        Secure Access
        </h1>
        """,unsafe_allow_html=True)

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
                    st.error("Invalid credentials")

        # REGISTER
        with tab2:

            user=st.text_input(
                "Create Username",
                key="reg_user"
            )

            pwd=st.text_input(
                "Create Password",
                type="password",
                key="reg_pass"
            )

            if st.button("Create Account"):

                if register_user(user,pwd):
                    st.success("Registered")

                else:
                    st.error("User exists")

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )


# ---------------- DASHBOARD ----------------
def dashboard():

    st.title("⚡ Dashboard")
    st.success("Login Successful")

    if st.button("Logout"):
        st.session_state.logged_in=False
        st.rerun()


# ---------------- RUN ----------------
if st.session_state.logged_in:
    dashboard()
else:
    login_page()
