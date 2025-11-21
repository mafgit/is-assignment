import streamlit as st
from utils import isUsernameValid, isPasswordValid, isLoggedIn
from services import login


if isLoggedIn(st.session_state):
    st.switch_page("pages/dashboard.py")

st.set_page_config("Login", initial_sidebar_state="collapsed")

form = st.form("login")
form.title("Hospital Dashboard Login")
username = form.text_input("Username", key="username")
password = form.text_input("Password", type="password", key="password")
submitted = form.form_submit_button(label="Submit", width="stretch")

if submitted:
    username = st.session_state["username"]
    password = st.session_state["password"]

    error = ""
    if not isUsernameValid(username):
        error = "Username must be 3 to 20 characters long, containing only letters, numbers or underscores"
    elif not isPasswordValid(password):
        error = "Password must be at least 6 characters long, and not containing spaces at start or end"

    if error:
        form.error(error)
    else:
        result = login(username, password)
        if result is None:
            form.error("Invalid username or password")
        else:
            st.session_state["username"] = username
            st.session_state["role"] = result["role"]
            st.session_state["user_id"] = result["user_id"]
            st.switch_page("pages/dashboard.py")
