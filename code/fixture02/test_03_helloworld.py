import allure
import pytest
from playwright.sync_api import expect, sync_playwright


@pytest.fixture()
def page_pw():
    browser = sync_playwright().start().chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(viewport={'width': 1920, 'height': 1080})
    page = context.new_page()
    page
    yield page
    page.close()


@allure.description("VWO Login")
@pytest.mark.positive
def test_vwo_login(page_pw):
    page = page_pw
    page.goto("https://app.vwo.com")
    page.wait_for_load_state("networkidle")
    page.get_by_role("textbox", name="Email address").fill("admin")
    page.get_by_role("textbox", name="Password").fill("admin")
    page.locator("#js-login-btn").click()
    allure.attach(page.screenshot(type="png", full_page=True),
                  name="random",
                  attachment_type=allure.attachment_type.PNG)
    expect(page.locator("#js-notification-box-msg")).to_have_text(
        "Your email, password, IP address or location did not match")
