import plotly.express as px


def build_city_volume_chart(df):
    city_calls = (
        df["city"]
        .value_counts()
        .head(10)
        .reset_index()
    )
    city_calls.columns = ["city", "calls"]

    fig = px.bar(
        city_calls,
        x="calls",
        y="city",
        orientation="h",
    )

    return fig
