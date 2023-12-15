import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="class")
def browser_context(request):
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    request.cls.page = page
    yield
    browser.close()
    playwright.stop()

@pytest.mark.usefixtures("browser_context")
class TestJavaScriptExecution:

    def test_execute_javascript(self):
        self.page.goto('https://thetestingacademy.com/')

        # Example of executing JavaScript to get the document's title
        title = self.page.evaluate("() => document.title")
        assert title == "TheTestingAcademy | Learn Software Testing and Automation Testing", "Title does not match"

        # Execute a more complex script
        script = """
        (message) => {
            return message;
        }
        """
        result = self.page.evaluate(script, "Hello, Playwright!")
        assert result == "Hello, Playwright!", "Script result does not match"

if __name__ == "__main__":
    pytest.main()
