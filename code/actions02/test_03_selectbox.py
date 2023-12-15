import time

import pytest
from playwright.sync_api import Page


@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    print("beforeEach")
    page.goto("https://the-internet.herokuapp.com/dropdown")
    yield
    print("afterEach")
    page.close()


def test_main_navigation(page: Page):
    # Assertions use the expect API.
    # page.locator("#dropdown").click()

    page.locator("#dropdown").select_option("2")
    page.reload()
    time.sleep(2)
    page.locator("#dropdown").select_option("Option 1")
    time.sleep(5)
