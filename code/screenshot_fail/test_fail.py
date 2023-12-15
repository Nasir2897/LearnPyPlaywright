import pytest
from playwright.sync_api import sync_playwright
import os
# Fixture for the Playwright browser
@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        yield browser
        browser.close()

# Fixture for the Playwright page


# Example test case
def test_example_com(page):
    page.goto("https://example.com")
    assert page.title() == "Nonexistent Title", "Title does not match expected value"
