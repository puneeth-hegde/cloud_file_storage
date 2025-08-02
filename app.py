import streamlit as st
from auth import init_db, add_user, validate_user
from s3_utils import upload_file, download_file, list_files, delete_file

init_db()

st.title("☁️ Cloud File Storage System")

menu = ["Login", "Signup"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Signup":
    st.subheader("Create Account")
    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")
    if st.button("Signup"):
        add_user(user, pwd)
        st.success("Account created! Login to continue.")

elif choice == "Login":
    st.subheader("Login")
    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")
    if st.button("Login"):
        if validate_user(user, pwd):
            st.success(f"Welcome {user}!")

            action = st.selectbox("Choose Action", ["Upload File", "Download File", "Delete File", "View Files"])
            
            if action == "Upload File":
                file = st.file_uploader("Choose a file")
                if file and st.button("Upload"):
                    upload_file(file, file.name, user)
                    st.success(f"{file.name} uploaded!")

            elif action == "Download File":
                files = list_files()
                if files:
                    selected = st.selectbox("Select file", files)
                    if st.button("Download"):
                        download_file(selected, user)
                        st.success(f"{selected} downloaded!")
                else:
                    st.warning("No files found.")

            elif action == "Delete File":
                files = list_files()
                if files:
                    selected = st.selectbox("Select file", files)
                    if st.button("Delete"):
                        delete_file(selected, user)
                        st.success(f"{selected} deleted!")
                else:
                    st.warning("No files found.")

            elif action == "View Files":
                files = list_files()
                if files:
                    st.write(files)
                else:
                    st.warning("No files uploaded yet.")
        else:
            st.error("Invalid credentials")
