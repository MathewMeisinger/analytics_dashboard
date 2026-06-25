import streamlit as st


def render_sidebar():
    with st.sidebar:
        st.subheader("Account")
        user = st.session_state.get("user")

        if user:
            st.write(f"**User:** {user['username']}")
            st.write(f"**Role:** {user['role'].title()}")
            st.divider()

        if st.button("Logout"):
            st.session_state["access_token"] = None
            st.session_state["user"] = None
            st.rerun()
