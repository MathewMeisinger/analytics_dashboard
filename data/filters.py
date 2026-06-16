import streamlit as st


def render_filters(df):
    # FILTER LOGIC
    filter_col1, filter_col2, filter_col3 = st.columns(3)

    with filter_col1:
        # city filter
        selected_city = st.selectbox(
            "City",
            ["All"] + sorted(df["city"].unique().tolist()),
            key="city_filter"
        )
    with filter_col2:
        # call status filter
        selected_status = st.selectbox(
            "Call status",
            ["All", "Successful", "Failed"],
            key="status_filter"
        )
    with filter_col3:
        # date filter
        date_range = st.date_input(
            "Date Range",
            value=(
                df["callStartTime"].min().date(),
                df["callStartTime"].max().date()
            ),
            key="date_filter"
        )

    return (
        selected_city,
        selected_status,
        date_range
        )


def apply_filters(
    df,
    selected_city,
    selected_status,
    date_range
):
    # filter application logic
    filtered_df = df.copy()

    # city filter
    if selected_city != "All":
        filtered_df = filtered_df[
            filtered_df["city"] == selected_city
        ]

    # call status filter
    if selected_status == "Successful":
        filtered_df = filtered_df[
            filtered_df["callStatus"] == True
        ]
    elif selected_status == "Failed":
        filtered_df = filtered_df[
            filtered_df["callStatus"] == False
        ]

    # date range filter
    start_date, end_date = date_range

    filtered_df = filtered_df[
        (
            filtered_df["callStartTime"].dt.date >= start_date
        )
        &
        (
            filtered_df["callStartTime"].dt.date <= end_date
        )
    ]
    return filtered_df
