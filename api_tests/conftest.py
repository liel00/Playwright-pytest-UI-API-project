import os
from dotenv import load_dotenv
import requests
import pytest

load_dotenv()
BASE_URL = os.getenv("BASE_URL_API")
USERNAME = os.getenv("API_USERNAME")
PASSWORD = os.getenv("API_PASSWORD")


@pytest.fixture(scope="session", autouse=True)
def check_server_alive():
    try:
        response = requests.get(BASE_URL, timeout=5)
        if response.status_code != 200:
            pytest.fail(f"Server is reachable but returned unexpected status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Could not connect to server at {BASE_URL}: {e}")


@pytest.fixture(scope="session")
def get_token():
    url = f"{BASE_URL}/auth"
    credentials = {
        "username": USERNAME,
        "password": PASSWORD
    }
    response = requests.post(url, json=credentials)

    if response.status_code == 200:
        print(response.json()["token"])
        return response.json()["token"]
    else:
        print(f"{response.status_code} - {response.text}")
        return None
