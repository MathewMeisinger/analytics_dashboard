# ---------------------------------------------------------------
# imports
# ---------------------------------------------------------------
import streamlit as st
import pandas as pd
from utils.api_filters import build_filter_params
from sections.overview import render_overview
from sections.activity import render_activity
from sections.performance import render_performance
from sections.cost import render_cost
from sections.regional import render_regional
from sections.recent_calls import render_recent_calls
from sections.login import render_login
from sections.sidebar import render_sidebar
from api.client import (
    get_summary,
    get_calls_by_hour,
    get_calls_by_day,
    get_calls_by_city,
    get_cost_by_city,
    get_call_records,
    get_metadata
)
from data.filters import (render_filters)

# ---------------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------------
st.set_page_config(
    page_title="Call Data Analysis Dashboard",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",
)

if "access_token" not in st.session_state:
    st.session_state["access_token"] = None


st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
}

div[data-testid="stMetric"] {
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------------
# Authentication
# ---------------------------------------------------------------
if "access_token" not in st.session_state:
    st.session_state["access_token"] = None

if "user" not in st.session_state:
    st.session_state["user"] = None

if not st.session_state["access_token"]:
    render_login()
    st.stop()


# ---------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------
render_sidebar()

# ---------------------------------------------------------------
# Page Header
# ---------------------------------------------------------------
st.title("Call Data Analytics")
st.caption("Monitor call volume, duration, cost, and regional performance.")
st.title("Filters")


# ---------------------------------------------------------------
# Filter State
# ---------------------------------------------------------------
metadata = get_metadata()

if metadata is None:
    st.warning("Unable to load metadata.")
    st.stop()

selected_city, caller_status, receiver_status, date_range = render_filters(
    metadata
)

params = build_filter_params(
    selected_city,
    caller_status,
    receiver_status,
    date_range,
)


# ---------------------------------------------------------------
# Dashboard Data
# ---------------------------------------------------------------
metrics = get_summary(params)
if metrics is None:
    st.error("Unable to retrieve dashboard metrics.")
    st.stop()


call_records = get_call_records(params)
if call_records is None:
    st.error("Unable to retrive Call Records.")
    st.stop()

hourly_data = get_calls_by_hour(params)
if hourly_data is None:
    st.error("Unable to retrive Call Records.")
    st.stop()

daily_data = get_calls_by_day(params)
if daily_data is None:
    st.error("Unable to retrive Call Records.")
    st.stop()

cost_data = get_cost_by_city(params)
if cost_data is None:
    st.error("Unable to retrive Call Records.")
    st.stop()

city_data = get_calls_by_city(params)
if city_data is None:
    st.error("Unable to retrive Call Records.")
    st.stop()


# ---------------------------------------------------------------
# Data Preparation
# ---------------------------------------------------------------
call_records_df = pd.DataFrame(call_records)

if call_records_df.empty:
    st.warning("No records match the selected filters.")
    st.stop()

call_records_df["callStartTime"] = pd.to_datetime(
    call_records_df["callStartTime"],
    format="mixed",
)


# ---------------------------------------------------------------
# Dashboard Rendering
# ---------------------------------------------------------------
render_overview(metrics)
render_activity(hourly_data, daily_data)
render_performance(call_records_df, metrics)
render_cost(metrics, cost_data, call_records_df)
render_regional(city_data)
render_recent_calls(params)
