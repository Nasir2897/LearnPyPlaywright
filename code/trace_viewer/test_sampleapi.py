import pytest
import requests


@pytest.mark.token
def test_post_create_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    headers = {
        "Content-Type": "application/json",
    }
    response = requests.post("https://restful-booker.herokuapp.com/auth", headers=headers, json=payload)
    print(response.status_code)
    print(response.text)
