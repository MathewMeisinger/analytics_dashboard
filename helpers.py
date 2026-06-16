import streamlit as st
import streamlit_shadcn_ui as ui


# function for all metric card UI
def metric_card(title, value, description, key):
    ui.metric_card(
        title=title,
        content=value,
        description=description,
        key=key
    )


# function for all charts to be in a card
def chart_card(title, description, fig):
    config = {
        "displaylogo": False
    }

    with st.container(border=True):
        st.markdown(f"#### {title}")
        st.caption(description)

        st.plotly_chart(
            fig,
            use_container_width=True,
            key=f"chart_{title.lower().replace(' ', '_')}",
            config=config
        )


# section header helpers
def section_header(title, description):
    st.divider()
    st.subheader(title)
    st.caption(description)


# chart them helper
def apply_chart_theme(fig):
    fig.update_layout(
        template="plotly_white",
        height=350,
        margin=dict(
            l=20,
            r=20,
            t=20,
            b=20
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )
    return fig
