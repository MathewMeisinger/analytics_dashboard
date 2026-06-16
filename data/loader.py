import requests
import streamlit as st
import pandas as pd


@st.cache_data(ttl=600)
def fetch_api_data():
    url = "https://69b30b45e224ec066bdb55a0.mockapi.io/api/v1/cdr"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")
        return None


def clean_data(json_data):
    df = pd.DataFrame(json_data)

    # Numeric fields
    df["id"] = pd.to_numeric(df["id"])
    df["callCost"] = pd.to_numeric(df["callCost"])
    df["callDuration"] = pd.to_numeric(df["callDuration"])

    # Datetime fields
    df["callStartTime"] = pd.to_datetime(df["callStartTime"], utc=True)
    df["callEndTime"] = pd.to_datetime(df["callEndTime"], utc=True)

    # Phone numbers
    df["callerNumber"] = (
        df["callerNumber"]
        .str.replace(r"\s+x\d+", "", regex=True)  # remove extensions
        .str.replace(r"\D", "", regex=True)       # keep digits only
    )

    df["receiverNumber"] = (
        df["receiverNumber"]
        .str.replace(r"\s+x\d+", "", regex=True)
        .str.replace(r"\D", "", regex=True)
    )

    return df
