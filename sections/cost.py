import streamlit as st
from helpers import (
    metric_card,
    chart_card,
    section_header,
    apply_chart_theme,
)
from charts.cost import (
    build_avg_cost_city_chart,
    build_total_cost_city_chart,
    build_cost_duration_chart,
)


def render_cost(metrics, cost_data, filtered_df):

    section_header(
        "Cost Performance",
        "Track call spending and cost efficiency."
    )

    cols = st.columns(3)

    with cols[0]:
        metric_card(
            "Total Cost",
            metrics["totalCost"],
            "Measured in Units.",
            "cost_card1",
        )

    with cols[1]:
        metric_card(
            "Avg Cost / Call",
            metrics["averageCost"],
            "Measured in Units",
            "cost_card2",
        )

    with cols[2]:
        metric_card(
            "Highest Call Cost",
            metrics["maxCost"],
            "Measured in Units",
            "cost_card3",
        )

    fig_city_avg_cost = build_avg_cost_city_chart(cost_data)

    fig_city_total_cost = build_total_cost_city_chart(cost_data)

    fig_cost_duration = build_cost_duration_chart(filtered_df)

    apply_chart_theme(fig_city_avg_cost)
    apply_chart_theme(fig_city_total_cost)
    apply_chart_theme(fig_cost_duration)

    left, right = st.columns(2)

    with left:
        chart_card(
            "Average Call Cost by City",
            "Average call cost per city.",
            fig_city_avg_cost,
        )

    with right:
        chart_card(
            "Total Call Cost by City",
            "Total call cost per city.",
            fig_city_total_cost,
        )

    chart_card(
        "Call Cost by Duration",
        "Relationship between call duration and cost.",
        fig_cost_duration,
    )
