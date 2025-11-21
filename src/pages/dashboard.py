import streamlit as st
from utils import isLoggedIn
from services import get_patients


# if not isLoggedIn(st.session_state):
#     st.switch_page("pages/login.py")

# debugging:
st.session_state["role"] = "doctor"
st.session_state["user_id"] = 1
st.session_state["username"] = "Mr_Bob"

st.set_page_config("Dashboard", initial_sidebar_state="collapsed")


left, right = st.columns([0.85, 0.15], vertical_alignment="center")
with left:
    st.title(f"Hey {st.session_state["username"]}!")
with right:
    logout_btn = st.button("Logout", width="stretch", type="primary")
    if logout_btn:
        st.session_state["role"] = None
        st.session_state["user_id"] = None
        st.switch_page("pages/login.py")


role = st.session_state["role"]
if role == "admin":
    color = "blue"
elif role == "receptionist":
    color = "red"
elif role == "doctor":
    color = "green"
else:
    color = "yellow"


st.badge(role.upper(), color=color)

patients = get_patients("doctor")

st.subheader("Patients")
st.data_editor(patients)
