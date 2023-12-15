import json

import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def context():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        yield context
        browser.close()


def test_crud_operations(context):
    # Base URL of the API
    base_url = "https://restful-booker.herokuapp.com/auth"

    # CREATE: POST request to create a new resource
    payload = {
        "username": "admin",
        "password": "password123"
    }
    create_response = context.request.post(base_url, data=payload)
    print("Token",create_response.json()["token"])
    print(create_response.status_text)


    # # UPDATE: PUT request to update the resource
    # update_response = context.request.put(f"{base_url}/{new_resource['id']}", data={"name": "Updated Resource"})
    # assert update_response.ok()
    #
    # # DELETE: DELETE request to remove the resource
    # delete_response = context.request.delete(f"{base_url}/{new_resource['id']}")
    # assert delete_response.ok()
    #
    # # Verify deletion
    # verify_delete_response = context.request.get(f"{base_url}/{new_resource['id']}")
    # assert verify_delete_response.status() == 404  # Assuming API returns 404 for not found
