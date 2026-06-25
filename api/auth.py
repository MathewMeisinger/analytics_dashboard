from api.client import api_post, api_get
from config import API_URL

BASE_URL = API_URL


def login(username, password):
    return api_post(
        "/auth/login",
        data={
            "username": username,
            "password": password,
        },
    )


def get_current_user():
    """
    Retrieve the currently authenticated user.
    """

    return api_get("/auth/me")
