import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    print("beforeEach")
    page.goto("https://the-internet.herokuapp.com/iframe")
    yield
    print("afterEach")


def test_main_navigation(page: Page):
    # Assertions use the expect API.
    expect(page).to_have_title("The Internet")
    page.get_by_role("button", name="Formats").click()
    page.get_by_text("Inline").click()
    page.get_by_role("menuitemcheckbox", name="Italic").get_by_text("Italic").click()
    page.frame_locator("#mce_0_ifr").locator("#tinymce").clear()
    page.frame_locator("#mce_0_ifr").locator("#tinymce").click
    page.frame_locator("#mce_0_ifr").locator("#tinymce").type("Hello Pramod")

