import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    print("beforeEach")
    page.goto("https://the-internet.herokuapp.com/nested_frames")
    yield
    print("afterEach")


def test_main_navigation(page: Page):
    # Assertions use the expect API.
    expect(page).to_have_title("The Internet")
    page.frame_locator("frame[name=\"frame-top\"]").frame_locator("frame[name=\"frame-left\"]").get_by_text(
        "LEFT").click()
    page.frame_locator("frame[name=\"frame-top\"]").frame_locator("frame[name=\"frame-middle\"]").locator(
        "body").click()
    page.frame_locator("frame[name=\"frame-top\"]").frame_locator("frame[name=\"frame-right\"]").get_by_text(
        "RIGHT").click()
    page.frame_locator("frame[name=\"frame-bottom\"]").get_by_text("BOTTOM").click()
