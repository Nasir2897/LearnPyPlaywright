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
    page.get_by_role("button", name="Click for JS Alert").click()
    result = page.locator("#result").text_content()
    assert result == "You successfully clicked an alert"


