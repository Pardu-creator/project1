import streamlit as st
import re
from backend import register_user, login_user


# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Employability Platform",
    page_icon="🚀",
    layout="centered"
)


# ---------------- STYLING ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg,#141E30,#243B55);
    color:white;
}

.main-box{
    background: rgba(255,255,255,0.12);
    padding:40px;
    border-radius:20px;
    backdrop-filter: blur(20px);
    box-shadow:0px 8px 32px rgba(0,0,0,0.35);
}

.stButton>button{
    width:100%;
    border-radius:15px;
    background:linear-gradient(90deg,#ff512f,#dd2476);
    color:white;
    font-size:17px;
    font-weight:bold;
}

h1{
    text-align:center;
}
</style>
""", unsafe_allow_html=True)


# ---------------- SESSION ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# ---------------- VALIDATION ----------------
def valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)


def password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*]", password):
        score += 1

    return score


# ---------------- LOGIN PAGE ----------------
def login_page():

    st.markdown("<h1>🚀 AI Employability Platform</h1>",
                unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["🔐 Login", "📝 Register"])

    with tab1:

        st.markdown('<div class="main-box">',
                    unsafe_allow_html=True)

        username = st.text_input("Username")
        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Login"):

            if login_user(username, password):
                st.session_state.logged_in = True
                st.success("Login successful ✅")
                st.rerun()
            else:
                st.error("Invalid credentials ❌")

        st.markdown('</div>',
                    unsafe_allow_html=True)

    with tab2:

        st.markdown('<div class="main-box">',
                    unsafe_allow_html=True)

        email = st.text_input("Email")
        new_user = st.text_input("Create Username")
        new_pass = st.text_input(
            "Create Password",
            type="password"
        )

        strength = password_strength(new_pass)

        st.progress(strength / 4)

        if strength == 1:
            st.warning("Weak password")
        elif strength == 2:
            st.info("Medium password")
        elif strength >= 3:
            st.success("Strong password")

        if st.button("Register"):

            if not valid_email(email):
                st.error("Invalid email")

            elif strength < 3:
                st.error(
                    "Password must contain:\n"
                    "- 8 chars\n"
                    "- Uppercase\n"
                    "- Number\n"
                    "- Special symbol"
                )

            else:

                if register_user(
                    new_user,
                    new_pass
                ):
                    st.success(
                        "Registration Successful ✅"
                    )
                else:
                    st.error(
                        "Username already exists ❌"
                    )

        st.markdown('</div>',
                    unsafe_allow_html=True)


# ---------------- DASHBOARD ----------------
def dashboard():

    st.title("🎯 Dashboard")

    st.success("Welcome to AI Employability Platform")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

    st.info(
        "Now integrate your resume analyzer here."
    )


# ---------------- RUN ----------------
if st.session_state.logged_in:
    dashboard()
else:
    login_page()
