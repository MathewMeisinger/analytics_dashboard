import requests
import streamlit as st
from config import API_URL

BASE_URL = API_URL


def get_headers():
    """
    Return the authorization headers for authenticated requests.
    """

    token = st.session_state.get("access_token")

    if not token:
        return {}

    return {
        "Authorization": f"Bearer {token}"
    }


def api_get(endpoint, params=None):
    """
    Generic GET request helper.
    """
    try:
        response = requests.get(
            f"{BASE_URL}{endpoint}",
            params=params,
            headers=get_headers(),
            timeout=10,
        )

        # Authentication has expired
        if response.status_code == 401:
            st.session_state["access_token"] = None
            st.session_state["user"] = None
            st.rerun()

        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        st.error(f"API Error: {e}")
        return None


def api_post(
    endpoint,
    data=None,
    json=None,
):
    """
    Generic authenticated POST request.
    """
    try:
        response = requests.post(
            f"{BASE_URL}{endpoint}",
            data=data,
            json=json,
            headers=get_headers(),
            timeout=10,
        )

        # Authentication has expired
        if response.status_code == 401:
            st.session_state["access_token"] = None
            st.session_state["user"] = None
            st.rerun()

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as e:
        st.error(f"API Error: {e}")
        return None


def get_summary(params=None):
    return api_get("/analytics/summary", params)


def get_metadata():
    return api_get("/metadata")


def get_cdr(params=None):
    return api_get("/cdr", params)


def get_call_type_distribution(params=None):
    return api_get("/analytics/call-type-distribution", params)


def get_top_callers(params=None):
    return api_get("/analytics/top-callers", params)


def get_calls_by_city(params=None):
    return api_get("/analytics/calls-by-city", params)


def get_cost_by_city(params=None):
    return api_get("/analytics/cost-by-city", params)


def get_calls_by_hour(params=None):
    return api_get("/analytics/calls-by-hour", params)


def get_calls_by_day(params=None):
    return api_get("/analytics/calls-by-day", params)


def get_call_records(params=None):
    return api_get("/analytics/call-records", params)
