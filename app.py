import streamlit as st
from backend import register_user, login_user

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Employability Platform",
    page_icon="🚀",
    layout="wide"
)

# ---------------- FULL ANIMATION CSS ----------------
st.markdown("""
<style>

/* Background Animation */
.stApp {
    background: linear-gradient(-45deg,#0f0c29,#302b63,#24243e,#ff512f);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
    color:white;
}

@keyframes gradientBG {
    0% {background-position:0% 50%;}
    50% {background-position:100% 50%;}
    100% {background-position:0% 50%;}
}

/* Floating particles */
.particle {
    position:absolute;
    border-radius:50%;
    background:rgba(255,255,255,0.3);
    animation: float 10s infinite linear;
}

@keyframes float {
    0% {transform:translateY(100vh);}
    100% {transform:translateY(-100vh);}
}

/* Glass Card */
.glass {
    background: rgba(255,255,255,0.12);
    border-radius: 25px;
    backdrop-filter: blur(20px);
    padding:40px;
    box-shadow:0 8px 32px rgba(0,0,0,0.4);
    transition:0.4s;
}

.glass:hover {
    transform:translateY(-10px) scale(1.02);
}

/* Buttons */
.stButton>button {
    width:100%;
    background:linear-gradient(90deg,#ff512f,#dd2476);
    color:white;
    font-size:18px;
    border:none;
    border-radius:14px;
    transition:0.4s;
}

.stButton>button:hover{
    transform:scale(1.08);
}

/* Inputs */
.stTextInput>div>div>input{
    border-radius:14px;
}

/* Title Glow */
.glow {
    text-align:center;
    font-size:50px;
    font-weight:bold;
    color:white;
    animation: glow 2s ease-in-out infinite alternate;
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
        st.markdown('<div class="glass">',
                    unsafe_allow_html=True)

        username = st.text_input("Username")
        password = st.text_input("Password",
                                 type="password")

        if st.button("Login"):
            if login_user(username,password):
                st.session_state.logged_in=True
                st.success("Login Success ✅")
                st.rerun()
            else:
                st.error("Invalid Credentials ❌")

        st.markdown('</div>',
                    unsafe_allow_html=True)

    with tab2:
        st.markdown('<div class="glass">',
                    unsafe_allow_html=True)

        new_user=st.text_input("Create Username")
        new_pass=st.text_input("Create Password",
                               type="password")

        if st.button("Register"):
            if register_user(new_user,new_pass):
                st.success("Registered Successfully ✅")
            else:
                st.error("User Exists ❌")

        st.markdown('</div>',
                    unsafe_allow_html=True)


# ---------------- DASHBOARD ----------------
def dashboard():

    st.markdown(
        '<div class="glow">🎯 Dashboard</div>',
        unsafe_allow_html=True
    )

    col1,col2,col3=st.columns(3)

    with col1:
        st.markdown("""
        <div class="glass">
        <h2>📄 Resume Analysis</h2>
        <p>AI-powered parsing & evaluation</p>
        </div>
        """,unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="glass">
        <h2>📊 Skill Gap</h2>
        <p>Find missing skills instantly</p>
        </div>
        """,unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="glass">
        <h2>💼 Job Roles</h2>
        <p>Smart role recommendations</p>
        </div>
        """,unsafe_allow_html=True)

    st.write("")

    if st.button("Logout"):
        st.session_state.logged_in=False
        st.rerun()


# ---------------- RUN ----------------
if st.session_state.logged_in:
    dashboard()
else:
    login_page()
