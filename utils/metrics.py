def calculate_metrics(filtered_df):
    return {
        "total_calls": int(len(filtered_df)),
        "successful_calls": int(filtered_df["callStatus"].sum()),
        "total_cost": round(float(filtered_df["callCost"].sum()), 2),
        "avg_duration": round(float(filtered_df["callDuration"].mean()), 2),
        "max_duration": int(filtered_df['callDuration'].max()),
        "min_duration": int(filtered_df['callDuration'].min()),
        "total_duration": int(filtered_df['callDuration'].sum()),
        "success_rate": round((filtered_df["callStatus"].sum() / len(filtered_df)) * 100, 1),
        "active_cities": int(filtered_df["city"].nunique()),
        "avg_cost": round(filtered_df["callCost"].mean(), 2),
        "max_cost": filtered_df["callCost"].max()
    }