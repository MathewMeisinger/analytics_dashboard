def build_filter_params(
    selected_city,
    caller_number,
    receiver_number,
    date_range,
):
    params = {}

    if selected_city != "All":
        params["city"] = selected_city

    if caller_number != "All":
        params["caller_number"] = caller_number

    if receiver_number != "All":
        params["receiver_number"] = receiver_number

    if len(date_range) == 2:
        params["start_date"] = date_range[0].isoformat()
        params["end_date"] = date_range[1].isoformat()

    return params
