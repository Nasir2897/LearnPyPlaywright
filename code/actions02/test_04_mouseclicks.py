import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    print("beforeEach")
    page.goto(
        "https://app.vwo.com/#/test/ab/13/heatmaps/1?token=eyJhY2NvdW50X2lkIjo2NjY0MDAsImV4cGVyaW1lbnRfaWQiOjEzLCJjcmVhdGVkX29uIjoxNjcxMjA1MDUwLCJ0eXBlIjoiY2FtcGFpZ24iLCJ2ZXJzaW9uIjoxLCJoYXNoIjoiY2IwNzBiYTc5MDM1MDI2N2QxNTM5MTBhZDE1MGU1YTUiLCJzY29wZSI6IiIsImZybiI6ZmFsc2V9&isHttpsOnly=1")
    page.wait_for_load_state("domcontentloaded", timeout=15)
    yield
    print("afterEach")


def test_click(page: Page):
    page.wait_for_load_state("networkidle", timeout=10)
    page.locator('li#js-heatmap-thumbnail').nth(1).hover()
    page.get_by_text("View Heatmap").nth(1).click()
    page.wait_for_load_state("networkidle", timeout=10)
    expect(page.title()).to_have_text("Campaign 13 - Heatmaps & Clickmaps")


def test_keyboard_click(page: Page):
    page.goto("https://playwright.dev/python/docs/input#select-options")
    page.locator("#select-options").click(modifiers=["Shift"])
    expect(page.title()).to_have_text("Campaign 13 - Heatmaps & Clickmaps")


def test_hover(page: Page):
    page.wait_for_load_state("networkidle", timeout=10)
    page.locator('li#js-heatmap-thumbnail').nth(1).hover()
    page.get_by_text("View Heatmap").nth(1).click()
    page.wait_for_load_state("networkidle", timeout=10)
    expect(page.title()).to_have_text("Campaign 13 - Heatmaps & Clickmaps")
