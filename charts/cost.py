import pandas as pd
import plotly.express as px


def build_avg_cost_city_chart(cost_data):

    cost_df = pd.DataFrame(cost_data)

    fig = px.bar(
        cost_df,
        x="city",
        y="averageCost",
    )

    fig.update_layout(
        xaxis_title="City",
        yaxis_title="Average Cost",
    )

    return fig


def build_total_cost_city_chart(cost_data):

    cost_df = pd.DataFrame(cost_data)

    fig = px.bar(
        cost_df,
        x="city",
        y="totalCost",
    )

    fig.update_layout(
        xaxis_title="City",
        yaxis_title="Total Cost",
    )

    return fig


def build_cost_duration_chart(df):
    # cost by duration
    fig = px.scatter(
        df,
        x="callDuration",
        y="callCost",
        hover_data=["city"]
    )

    return fig
