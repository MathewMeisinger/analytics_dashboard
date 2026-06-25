import streamlit as st
from api.client import get_metadata
import pandas as pd


@st.cache_data(ttl=300)
def load_metadata():
    return get_metadata()


def render_filters(metadata):
    metadata = load_metadata()
    # FILTER LOGIC
    filter_col1, filter_col2, filter_col3, filter_col4 = st.columns(4)

    with filter_col1:
        # city filter
        selected_city = st.selectbox(
            "City",
            ["All"] + metadata["cities"],
            key="city_filter"
        )
    with filter_col2:
        # caller number filter
        caller_status = st.selectbox(
            "Caller Number",
            ["All"] + metadata["callerNumbers"],
            key="caller_filter"
        )
    with filter_col3:
        # receiver number filter
        receiver_status = st.selectbox(
            "Receiver Number",
            ["All"] + metadata["receiverNumbers"],
            key="receiver_filter"
        )
    with filter_col4:
        # date filter
        date_range = st.date_input(
            "Date Range",
            value=(
                pd.to_datetime(metadata["minDate"]).date(),
                pd.to_datetime(metadata["maxDate"]).date(),
            ),
            key="date_filter"
        )

    return (
        selected_city,
        caller_status,
        receiver_status,
        date_range
        )
