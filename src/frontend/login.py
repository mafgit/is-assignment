import streamlit as st


def main():
    st.title("Hospital Management System")

    form = st.form("login", True)
    email = form.text_input("Email", key="email")
    password = form.text_input("Password", type="password", key="password")
    submitted = form.form_submit_button(label="Submit", width="stretch")

    if submitted:
        st.session_state["email"] = email


main()
