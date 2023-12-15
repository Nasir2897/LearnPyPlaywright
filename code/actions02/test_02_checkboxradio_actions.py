import time

import pytest
from playwright.sync_api import Page


@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    print("beforeEach")
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    yield
    print("afterEach")
    page.close()


def test_main_navigation(page: Page):
    # Assertions use the expect API.
    # page.locator("#dropdown").click()

    page.get_by_role("checkbox").first.check()
    #page.get_by_role("checkbox").last.check()
    page.get_by_role("checkbox").nth(1).uncheck()
