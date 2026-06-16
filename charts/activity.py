import plotly.express as px


def build_hourly_calls_chart(df):
    activity_df = df.copy()
    activity_df["hour"] = activity_df["callStartTime"].dt.hour

    hourly_calls = (
        activity_df.groupby("hour")
        .size()
        .reset_index(name="calls")
    )

    fig = px.line(
        hourly_calls,
        x="hour",
        y="calls",
        markers=True,
    )
    fig.update_layout(
        xaxis_title="Hour of the day",
        yaxis_title="Number of Calls"
    )

    return fig


def build_daily_calls_chart(df):
    activity_df = df.copy()
    activity_df["callDate"] = activity_df["callStartTime"].dt.date

    daily_calls = (
        activity_df.groupby("callDate")
        .size()
        .reset_index(name="calls")
    )

    fig = px.line(
        daily_calls,
        x="callDate",
        y="calls",
        markers=True,
    )
    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Number of Calls"
    )

    return fig
