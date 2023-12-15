import pytest
from playwright.sync_api import Page, expect

#Checkboxes and radio buttons

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    print("beforeEach")
    page.goto("https://katalon-demo-cura.herokuapp.com/")
    yield
    print("afterEach")
    page.close()


def test_checkbox_radio(page: Page):
    # Assertions use the expect API.
    page.locator("#btn-make-appointment").click()
    page.get_by_label("Username").click()
    page.get_by_label("Password").click()
    page.get_by_role("button", name="Login").click()
    expect(page.locator(".lead.text-danger")).to_have_text("Login failed! Please ensure the username and password are valid.")

