import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="class")
def browser_context(request):
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://selectorshub.com/xpath-practice-page/")
    page.set_viewport_size({"width": 1280, "height": 720})
    page.wait_for_load_state("domcontentloaded")

    request.cls.page = page
    yield
    browser.close()
    playwright.stop()

@pytest.mark.usefixtures("browser_context")
class TestShadowDOM:

    def test_shadow_dom_interaction(self):
        div = self.page.locator("xpath=//div[@class='jackPart']")
        div.scroll_into_view_if_needed()

        # Directly interact with shadow DOM elements
        link = self.page.locator("div.jackPart #app2 #pizza")
        print(link.input_value())
        link.fill("Farmhouse")

if __name__ == "__main__":
    pytest.main()
