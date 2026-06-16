# imports
import streamlit as st
from helpers import (
    metric_card,
    chart_card,
    section_header,
    apply_chart_theme
)
from data.loader import (
    fetch_api_data,
    clean_data
)
from data.filters import (
    render_filters,
    apply_filters
)
from utils.metrics import calculate_metrics
from charts.activity import (
    build_daily_calls_chart,
    build_hourly_calls_chart
)
from charts.regional import build_city_volume_chart
from charts.performance import (
    build_duration_distribution,
    build_duration_vs_cost
)
from charts.cost import (
    build_avg_cost_city_chart,
    build_total_cost_city_chart,
    build_cost_duration_chart
)

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

# PAGE SETUP
st.set_page_config(
    page_title="Call Data Analysis Dashboard",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",
)
# TITLE SECTION
st.title("Call Data Analytics")
st.caption(
    "Monitor call volume, duration, cost, and regional performance."
)

st.title("Filters")

# load data and populate dataframe
json_data = fetch_api_data()

if json_data:
    df = clean_data(json_data)
else:
    st.warning("No data found or the API is offline")
    st.stop()

selected_city, selected_status, date_range = render_filters(df)

filtered_df = apply_filters(
    df,
    selected_city,
    selected_status,
    date_range
)

if filtered_df.empty:
    st.warning("No records match thye selected filters.")
    st.stop()

# Render metrics
metrics = calculate_metrics(filtered_df)


meta_col1, meta_col2, meta_col3 = st.columns(3)
with meta_col1:
    st.metric(
        "Records Loaded",
        len(filtered_df)
    )
with meta_col2:
    st.metric(
        "Filtered Records",
        len(filtered_df)
    )
with meta_col3:
    st.metric(
        "Cities",
        filtered_df["city"].nunique()
    )


# 1. KPI SUMMARY CARDS
section_header(
    "Overview",
    "High level performance metrics across all call activity."
)
cols = st.columns(5)
with cols[0]:
    metric_card(
        "Total Calls",
        metrics["total_calls"],
        "All recorded Calls.",
        "card1"
        )
with cols[1]:
    metric_card(
        "Total Cost",
        metrics["total_cost"],
        "Measured in Units.",
        "card2"
        )
with cols[2]:
    metric_card(
        "Avg Duration",
        f'{metrics["avg_duration"]}s',
        "Average per call.",
        "card3"
        )
with cols[3]:
    metric_card(
        "Success Rate of Calls",
        f"{metrics['success_rate']}%",
        "Ratio of completed calls.",
        "card4"
        )
with cols[4]:
    metric_card(
        "Active Cities",
        metrics['active_cities'],
        "Unique Locations",
        "card5"
    )


# 4. CALL ACTIVITY TIMELINE
section_header(
    "Activity Trends",
    "Monitor Call activity across Time."
)
fig_hourly_calls = (
    build_hourly_calls_chart(filtered_df)
)
fig_daily_calls = (
    build_daily_calls_chart(filtered_df)
)
apply_chart_theme(fig_daily_calls)
apply_chart_theme(fig_hourly_calls)

col1, col2 = st.columns(2)
with col1:
    chart_card(
        "Calls per Hour",
        "Distribution of calls per 24hrs.",
        fig_hourly_calls,
    )
with col2:
    chart_card(
        "Calls per Day",
        "Distribution of calls per day.",
        fig_daily_calls,
    )


# 2. CALL DURATION ANALYTICS
section_header(
    "Call Performance",
    "Analyse duration trends and call behaviour."
)
cols = st.columns(4)
with cols[0]:
    metric_card(
        "Longest Call",
        metrics["max_duration"],
        "Seconds",
        "call_card1"
    )
with cols[1]:
    metric_card(
        "Shortest Call",
        metrics["min_duration"],
        "Seconds",
        "call_card2"
    )
with cols[2]:
    metric_card(
        "Average Call Duration",
        metrics["avg_duration"],
        "Seconds",
        "call_card3"
    )
with cols[3]:
    metric_card(
        "Total Call Duration",
        metrics["total_duration"],
        "Seconds",
        "call_card4"
    )

# plots for call duration analytics
duration_histogram = build_duration_distribution(filtered_df)
duration_vs_cost = build_duration_vs_cost(filtered_df)
apply_chart_theme(duration_histogram)
apply_chart_theme(duration_vs_cost)

left, right = st.columns(2)
with left:
    chart_card(
            "Duration Distribution",
            "distribution of call durations.",
            duration_histogram,
        )
with right:
    chart_card(
        "Call Cost by Call Duration",
        "Distribution of call costs by call durations.",
        duration_vs_cost,
    )


# 3. CALL COST ANALYTICS
section_header(
    "Cost Performance",
    "Track call spending and cost efficiency."
)

cols = st.columns(3)
with cols[0]:
    metric_card(
        "Total Cost:",
        metrics["total_cost"],
        "Measured in Units.",
        "cost_card1"
        )
with cols[1]:
    metric_card(
        "Avg Cost / Call:",
        metrics["avg_cost"],
        "Measured in Units",
        "cost_card2"
        )
with cols[2]:
    metric_card(
        "Highest Call Cost:",
        metrics["max_cost"],
        "Measured in Units",
        "cost_card3"
        )

# build cost charts
fig_city_avg_cost = (
    build_avg_cost_city_chart(filtered_df)
)
fig_city_total_cost = (
    build_total_cost_city_chart(filtered_df)
)
fig_cost_duration = (
    build_cost_duration_chart(filtered_df)
)

apply_chart_theme(fig_city_avg_cost)
apply_chart_theme(fig_city_total_cost)
apply_chart_theme(fig_cost_duration)

# plot cost analytics
top_left, top_right = st.columns(2)
with top_left:
    chart_card(
        "Average Call cost by City",
        "Average of call cost per City.",
        fig_city_avg_cost,
    )
with top_right:
    chart_card(
        "Total Call cost by City",
        "Total cost of calls per city.",
        fig_city_total_cost,
    )
chart_card(
    "Call cost by Duration",
    "Cost of calls by the duration of the calls.",
    fig_cost_duration,
)


# 5. REGIONAL CALL DATA
section_header(
    "Regional Insights",
    "Compare call activity across locations."
)

fig_city_calls = build_city_volume_chart(filtered_df)

apply_chart_theme(fig_city_calls)

chart_card(
    "Call number by City",
    "Number of calls per City",
    fig_city_calls,
)

# 6. RECENT CALL LOG TABLE
section_header(
    "Most recent Calls",
    "Latest call records available from the system."
)
call_log_df = filtered_df[[
    "callerName",
    "callerNumber",
    "receiverNumber",
    "city",
    "callDuration",
    "callCost",
    "callStartTime"
    ]]
total_users = len(filtered_df)
st.dataframe(
    call_log_df,
    use_container_width=True,
    hide_index=True
    )
