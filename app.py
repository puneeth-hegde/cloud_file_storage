import streamlit as st
from auth import init_db, add_user, validate_user
from s3_utils import upload_file, download_file, list_files, delete_file

# Initialize database
init_db()

# --- Session State to track login ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""

# --- Function: Login Page ---
def login_page():
    st.title("☁️ Cloud File Storage System")
    st.subheader("🔑 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if validate_user(username, password):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success(f"Welcome, {username}!")
            st.experimental_rerun()  # Redirect to dashboard
        else:
            st.error("Invalid credentials. Try again.")

    st.write("Don't have an account?")
    if st.button("Signup"):
        signup_page()

# --- Function: Signup Page ---
def signup_page():
    st.title("☁️ Cloud File Storage System")
    st.subheader("📝 Signup")

    username = st.text_input("Choose a Username")
    password = st.text_input("Choose a Password", type="password")

    if st.button("Create Account"):
        add_user(username, password)
        st.success("Account created successfully! Please login.")

    if st.button("Back to Login"):
        st.experimental_rerun()

# --- Function: Dashboard Page ---
def dashboard_page():
    st.title(f"📂 Welcome {st.session_state.username}")
    st.sidebar.subheader("Menu")

    action = st.sidebar.radio("Choose Action", ["Upload File", "Download File", "Delete File", "View Files", "Logout"])

    if action == "Upload File":
        st.subheader("📤 Upload File")
        file = st.file_uploader("Choose a file")
        if file and st.button("Upload"):
            upload_file(file, file.name, st.session_state.username)
            st.success(f"{file.name} uploaded successfully!")

    elif action == "Download File":
        st.subheader("📥 Download File")
        files = list_files()
        if files:
            selected = st.selectbox("Select a file to download", files)
            if st.button("Download"):
                download_file(selected, st.session_state.username)
                st.success(f"{selected} downloaded successfully!")
        else:
            st.warning("No files found.")

    elif action == "Delete File":
        st.subheader("🗑️ Delete File")
        files = list_files()
        if files:
            selected = st.selectbox("Select a file to delete", files)
            if st.button("Delete"):
                delete_file(selected, st.session_state.username)
                st.success(f"{selected} deleted successfully!")
        else:
            st.warning("No files found.")

    elif action == "View Files":
        st.subheader("📄 Stored Files")
        files = list_files()
        if files:
            st.write(files)
        else:
            st.warning("No files uploaded yet.")

    elif action == "Logout":
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.experimental_rerun()

# --- App Flow ---
if not st.session_state.logged_in:
    login_page()
else:
    dashboard_page()
