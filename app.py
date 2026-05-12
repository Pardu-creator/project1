import streamlit as st
from backend import register_user, login_user

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Employability Platform",
    page_icon="🚀",
    layout="wide"
)

# ---------------- ANIMATED CSS ----------------
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
padding:40px;
box-shadow:0 8px 32px rgba(0,0,0,0.4);
transition:0.4s;
}

.glass:hover{
transform:translateY(-10px);
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


# ---------------- LOGIN PAGE ----------------
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

            if login_user(username, password):
                st.session_state.logged_in = True
                st.success("Login Success ✅")
                st.rerun()
            else:
                st.error("Invalid Credentials ❌")

        st.markdown('</div>',
                    unsafe_allow_html=True)

    with tab2:

        st.markdown('<div class="glass">',
                    unsafe_allow_html=True)

        new_user = st.text_input("Create Username")
        new_pass = st.text_input("Create Password",
                                 type="password")

        if st.button("Register"):

            if register_user(new_user, new_pass):
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

    choice = st.radio(
        "",
        [
            "📄 Resume Analysis",
            "📊 Skill Gap",
            "💼 Job Roles"
        ],
        horizontal=True
    )

    st.write("")

    # Resume Upload
    if choice == "📄 Resume Analysis":

        st.markdown('<div class="glass">',
                    unsafe_allow_html=True)

        st.subheader("Upload Resume")

        file = st.file_uploader(
            "Upload PDF Resume",
            type=["pdf"]
        )

        if file:
            st.success("Resume Uploaded ✅")

        st.markdown('</div>',
                    unsafe_allow_html=True)

    # Skill Gap
    elif choice == "📊 Skill Gap":

        st.markdown('<div class="glass">',
                    unsafe_allow_html=True)

        st.subheader("Skill Gap Analysis")

        jd = st.text_area(
            "Paste Job Description"
        )

        if st.button("Analyze"):

            if jd:
                st.success(
                    "Analysis Complete ✅"
                )

                st.write(
                    "Missing Skills:"
                )

                st.write("• Python")
                st.write("• SQL")
                st.write("• Machine Learning")

            else:
                st.error(
                    "Enter Job Description"
                )

        st.markdown('</div>',
                    unsafe_allow_html=True)

    # Job Roles
    elif choice == "💼 Job Roles":

        st.markdown('<div class="glass">',
                    unsafe_allow_html=True)

        st.subheader(
            "Recommended Roles"
        )

        st.success("AI Suggested Roles")

        st.write("• Data Analyst")
        st.write("• Backend Developer")
        st.write("• ML Engineer")
        st.write("• Cloud Engineer")

        st.markdown('</div>',
                    unsafe_allow_html=True)

    st.write("")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()


# ---------------- RUN ----------------
if st.session_state.logged_in:
    dashboard()
else:
    login_page()
