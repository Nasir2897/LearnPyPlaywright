import time

import pytest
from playwright.sync_api import Page, expect, sync_playwright
import allure

@allure.description("VWO Login")
@pytest.mark.positive
def test_vwo_login(page: Page) -> None:
    page.goto("https://awesomeqa.com/pw/locators1.html")
    page.wait_for_load_state("networkidle")
    expect(page.get_by_role("listitem")).to_have_count(5)
    time.sleep(3)
    for row in page.get_by_role("listitem").all():
        print(row.text_content())
    page.close()



