import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    print("beforeEach")
    page.goto("https://selectorshub.com/xpath-practice-page/")
    page.wait_for_load_state("domcontentloaded")
    yield
    print("afterEach")


def test_svg_demo(page: Page):
    # Assertions use the expect API.
    expect(page).to_have_url("https://selectorshub.com/xpath-practice-page/")
    # Maximize window
    page.set_viewport_size({"width": 1200, "height": 800})

    # Select the div element
    div = page.locator("xpath=//div[@class='jackPart']")

    # Scroll to view the div
    div.scroll_into_view_if_needed()

    # Get shadow DOM elements using JavaScript
    # Playwright can directly interact with elements inside shadow DOM
    input_pizza = page.locator("div.jackPart #app2 #pizza")

    # Perform actions on the shadow DOM element
    input_pizza.fill("FarmHouse")
    input_pizza.press("Enter")
    page.pause()


if __name__ == "__main__":
    pytest.main(["-v"])
