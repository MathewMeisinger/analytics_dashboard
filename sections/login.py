import streamlit as st

from api.auth import login, get_current_user


def render_login():
    st.title("Call Data Analytics")
    st.subheader("Sign In")
    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password",
    )

    if st.button("Login"):
        token = login(username, password)

        if token:
            st.session_state["access_token"] = token["access_token"]
            user = get_current_user()

            if user:
                st.session_state["user"] = user
                st.rerun()
            else:
                st.session_state["access_token"] = None
                st.error("Unable to retrieve user information.")
