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

        # Find the h1 element and get its text content
        h1_text = self.page.locator("(//a[normalize-space()='Download the ROADMAPs'])[2]").text_content()

        # JavaScript function to scroll the h1 element with matching text content into view
        script = """
            (h1Text) => {
                const h1 = Array.from(document.querySelectorAll('h1')).find(element => element.textContent === h1Text);
                if (h1) {
                    h1.scrollIntoView();
                }
            }
            """

        # Execute the script with the h1 text content as an argument
        self.page.evaluate(script, h1_text)


if __name__ == "__main__":
    pytest.main()
