import pytest
from playwright.sync_api import Page,expect, sync_playwright
@pytest.fixture()
def page_pw():
    browser = sync_playwright().start().chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(
    record_video_dir="videos/",
    record_video_size={"width": 1920, "height": 1080},
    viewport={'width': 1920, 'height': 1080}
    )
    page = context.new_page()
    yield page
    context.close()
    page.close()


@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    print("beforeEach")
    page.goto("https://sdet.live")
    yield
    print("afterEach")

def test_trace_viewer(page: Page):
    # Assertions use the expect API.
    expect(page).to_have_url("https://courses.thetestingacademy.com/")