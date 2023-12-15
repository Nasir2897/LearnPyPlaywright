import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        yield page
        browser.close()

def test_example_com_title_and_content(page):
    # Navigate to the website
    page.goto("https://www.thetestingacademy.com/")

    # Assertions
    # Check if the title of the page is correct
    assert page.title() == "TheTestingAcademy | Learn Software Testing and Automation Testing", "Title does not match expected value"

    # Check if the page contains specific text
    assert "Learn the Art of Software Testing & Upskill Yourself" in page.content(), "Expected text not found in page content"

# Run the test
if __name__ == "__main__":
    pytest.main()
