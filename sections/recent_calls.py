import pandas as pd
import streamlit as st

from api.client import get_cdr
from helpers import section_header


def render_recent_calls(params):

    section_header(
        "Most Recent Calls",
        "Latest call records available from the system."
    )

    ROWS_PER_PAGE = 10

    if "call_log_page" not in st.session_state:
        st.session_state.call_log_page = 0

    cdr_params = {
        **params,
        "page": st.session_state.call_log_page + 1,
        "limit": ROWS_PER_PAGE,
    }

    cdr_page = get_cdr(cdr_params)

    if cdr_page is None:
        st.error("Unable to load call records.")
        return

    total_pages = cdr_page["total_pages"]

    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:

        if st.button("⬅ Previous"):

            st.session_state.call_log_page = max(
                0,
                st.session_state.call_log_page - 1
            )

            st.rerun()

    with col2:

        st.markdown(
            f"<div style='text-align:center;'>"
            f"Page {st.session_state.call_log_page + 1} "
            f"of {total_pages}</div>",
            unsafe_allow_html=True,
        )

    with col3:

        if st.button("Next ➡"):

            st.session_state.call_log_page = min(
                total_pages - 1,
                st.session_state.call_log_page + 1
            )

            st.rerun()

    call_log_df = pd.DataFrame(cdr_page["records"])

    if call_log_df.empty:
        st.info("No call records found.")
        return

    call_log_df["callStartTime"] = (
        pd.to_datetime(
            call_log_df["callStartTime"],
            format="mixed",
        )
        .dt.strftime("%d %B %Y @ %H:%M:%S")
    )

    st.dataframe(
        call_log_df,
        use_container_width=True,
        hide_index=True,
    )
