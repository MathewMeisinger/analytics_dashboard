import pandas as pd
import plotly.express as px


def build_hourly_calls_chart(hourly_data):

    hourly_df = pd.DataFrame(hourly_data)

    fig = px.line(
        hourly_df,
        x="hour",
        y="totalCalls",
        markers=True,
    )

    fig.update_layout(
        xaxis_title="Hour of Day",
        yaxis_title="Number of Calls",
    )

    return fig


def build_daily_calls_chart(daily_data):

    daily_df = pd.DataFrame(daily_data)

    fig = px.line(
        daily_df,
        x="day",
        y="totalCalls",
        markers=True,
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Number of Calls",
    )

    return fig
