import streamlit as st

st.title("Hospital Dashboard")

st.set_page_config("Home", initial_sidebar_state="collapsed")

if st.button("Go to Dashboard"):
    st.switch_page("pages/dashboard.py")