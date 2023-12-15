import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    print("beforeEach")
    page.goto("https://the-internet.herokuapp.com/windows")
    yield
    print("afterEach")


def test_main_navigation(page: Page):
    # Assertions use the expect API.
    expect(page).to_have_title("The Internet")
    # Use expect_popup() to capture the new tab when performing the action that opens it.

    with page.expect_popup() as popup_info:
        page.get_by_role("link", name="Click Here").click()
    page1 = popup_info.value
    page1.get_by_role("heading", name="New Window").click()

    # Switch Back to the Original Page:
    page.bring_to_front()
    page.pause()



