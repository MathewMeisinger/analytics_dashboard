import plotly.express as px


def build_avg_cost_city_chart(df):
    city_avg_cost = (
        df.groupby("city")["callCost"]
        .mean()
        .sort_values(ascending=False)
        .reset_index()
    )

    fig = px.bar(
        city_avg_cost,
        x="city",
        y="callCost",
    )

    return fig


def build_total_cost_city_chart(df):
    # total cost per city
    city_total_cost = (
        df.groupby("city")["callCost"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )
    fig = px.bar(
        city_total_cost,
        x="city",
        y="callCost",
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
