import streamlit as st
from helpers import (
    metric_card,
    chart_card,
    section_header,
    apply_chart_theme,
)
from charts.performance import (
    build_duration_distribution,
    build_duration_vs_cost,
)


def render_performance(filtered_df, metrics):

    section_header(
        "Call Performance",
        "Analyse duration trends and call behaviour."
    )

    cols = st.columns(4)

    with cols[0]:
        metric_card(
            "Longest Call",
            metrics["maxDuration"],
            "Seconds",
            "call_card1",
        )

    with cols[1]:
        metric_card(
            "Shortest Call",
            metrics["minDuration"],
            "Seconds",
            "call_card2",
        )

    with cols[2]:
        metric_card(
            "Average Call Duration",
            metrics["averageDuration"],
            "Seconds",
            "call_card3",
        )

    with cols[3]:
        metric_card(
            "Total Call Duration",
            metrics["totalDuration"],
            "Seconds",
            "call_card4",
        )

    duration_histogram = build_duration_distribution(filtered_df)
    duration_vs_cost = build_duration_vs_cost(filtered_df)

    apply_chart_theme(duration_histogram)
    apply_chart_theme(duration_vs_cost)

    left, right = st.columns(2)

    with left:
        chart_card(
            "Duration Distribution",
            "Distribution of call durations.",
            duration_histogram,
        )

    with right:
        chart_card(
            "Call Cost by Call Duration",
            "Distribution of call costs by call durations.",
            duration_vs_cost,
        )
