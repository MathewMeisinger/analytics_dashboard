import plotly.express as px


def build_duration_distribution(df):
    fig = px.histogram(
        df,
        x="callDuration",
        nbins=10,
        labels={"callDuration": "Duration (Seconds)"}
    )
    fig.update_layout(bargap=0.1)

    return fig


def build_duration_vs_cost(df):
    fig = px.scatter(
        df,
        x="callDuration",
        y="callCost",
        hover_data=["callerName"]
    )
    fig.update_layout(
        xaxis_title="Call Duration",
        yaxis_title="Cost per Call"
    )

    return fig
