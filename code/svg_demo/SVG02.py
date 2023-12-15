import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="function", autouse=True)
def page_setup(page: Page):
    page.goto("https://flipkart.com")
    page.set_viewport_size({"width": 1200, "height": 800})
    yield


def test_svg_demo(page: Page):
    # Interacting with the search input
    # search_input = page.locator("input[name='q']")
    # search_input.fill("AC")
    #
    # # Clicking on the SVG element
    # search_element = page.locator("xpath=//*[local-name()='svg']/*[local-name()='g' and @fill-rule='evenodd']")
    # search_element.click()

    # Navigating to a different URL
    page.goto("https://www.amcharts.com/svg-maps/?map=india")

    # Handling a list of SVG elements
    states_list = page.locator("xpath=//*[name()='svg']/*[name()='g'][7]/*[name()='g']/*[name()='g']/*[name()='path']")

    # Iterating over elements and performing an action
    for state in states_list.element_handles():
        aria_label = state.get_attribute("aria-label")
        print(aria_label)
        if aria_label.strip() == "Tripura":
            state.click()
            break


if __name__ == "__main__":
    pytest.main(["-v"])
