from helpers import (
    chart_card,
    section_header,
    apply_chart_theme,
)
from charts.regional import (
    build_city_volume_chart,
)


def render_regional(city_data):

    section_header(
        "Regional Insights",
        "Compare call activity across locations."
    )

    fig_city_calls = build_city_volume_chart(city_data)

    apply_chart_theme(fig_city_calls)

    chart_card(
        "Call Number by City",
        "Number of calls per city.",
        fig_city_calls,
    )
