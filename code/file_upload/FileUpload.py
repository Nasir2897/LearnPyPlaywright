import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    print("beforeEach")
    page.goto("https://awesomeqa.com/practice.html")
    yield
    print("afterEach")


def test_main_navigation(page: Page):
    # Assertions use the expect API.
    expect(page).to_have_url("https://awesomeqa.com/practice.html")
    with page.expect_file_chooser() as fc:
        page.locator("//input[@id='photo']").click()
    file_c =  fc.value
    file_c.set_files("/Users/pramod/PycharmProjects/LearnPyPlaywright/code/file_upload/Playwright_File_Upload_Guide.pdf")
    page.pause()

