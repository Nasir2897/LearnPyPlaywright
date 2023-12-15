import pytest
from playwright.sync_api import Page, expect, sync_playwright
import allure

@allure.description("VWO Login")
@pytest.mark.positive
def test_vwo_login(page: Page) -> None:
    page.goto("https://awesomeqa.com/pw/locators1.html")
    page.wait_for_load_state("networkidle")
    page.get_by_label("Subscribe").check()
    page.get_by_role("button", name="Submit").click()
    page.close()



