import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    print("beforeEach")
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    yield
    print("afterEach")


def test_main_navigation(page: Page):
    # Assertions use the expect API.
    expect(page).to_have_title("The Internet")

    page.on('dialog', lambda dialog:  dialog.accept())
    page.locator("//button[@onclick='jsConfirm()']").click()
    result = page.locator("#result").text_content()
    assert result == "You clicked: Ok"


