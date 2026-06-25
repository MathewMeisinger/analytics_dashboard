import pandas as pd
import plotly.express as px


def build_city_volume_chart(city_data):
    city_df = pd.DataFrame(city_data)

    fig = px.bar(
        city_df,
        x="city",
        y="totalCalls",
    )

    fig.update_layout(
        xaxis_title="City",
        yaxis_title="Number of Calls",
    )

    return fig
