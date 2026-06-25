import streamlit as st

from helpers import (
    metric_card,
    section_header,
)


def render_overview(metrics):

    section_header(
        "Overview",
        "High level performance metrics across all call activity."
    )

    cols = st.columns(5)

    with cols[0]:
        metric_card(
            "Total Calls",
            metrics["totalCalls"],
            "All recorded Calls.",
            "card1"
        )

    with cols[1]:
        metric_card(
            "Total Cost",
            metrics["totalCost"],
            "Measured in Units.",
            "card2"
        )

    with cols[2]:
        metric_card(
            "Avg Duration",
            f"{metrics['averageDuration']}s",
            "Average per call.",
            "card3"
        )

    with cols[3]:
        metric_card(
            "Success Rate of Calls",
            f"{metrics['successRate']}%",
            "Ratio of completed calls.",
            "card4"
        )

    with cols[4]:
        metric_card(
            "Active Cities",
            metrics["activeCities"],
            "Unique Locations",
            "card5"
        )
