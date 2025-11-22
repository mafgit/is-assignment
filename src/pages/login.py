import streamlit as st
from utils import isUsernameValid, isPasswordValid, isLoggedIn
from services import login


if isLoggedIn(st.session_state):
    st.switch_page("pages/dashboard.py")

st.set_page_config("Login", initial_sidebar_state="collapsed")

form = st.form("login")
form.title(":material/local_hospital: Hospital Dashboard Login")
username = form.text_input("Username")
password = form.text_input("Password", type="password")
submitted = form.form_submit_button(label="Login",icon=":material/login:", width="stretch")
form.warning("This website collects personal data and has data retention policy of 365 days. By continuing, you agree to our terms and policy.")
if submitted:
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
            st.session_state["consent_given"] = True
            st.switch_page("pages/dashboard.py")
