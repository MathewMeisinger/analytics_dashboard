import streamlit as st
from helpers import (
    chart_card,
    section_header,
    apply_chart_theme,
)
from charts.activity import (
    build_hourly_calls_chart,
    build_daily_calls_chart,
)


def render_activity(hourly_data, daily_data):

    section_header(
        "Activity Trends",
        "Monitor Call activity across Time."
    )

    fig_hourly_calls = build_hourly_calls_chart(hourly_data)
    fig_daily_calls = build_daily_calls_chart(daily_data)

    apply_chart_theme(fig_hourly_calls)
    apply_chart_theme(fig_daily_calls)

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
