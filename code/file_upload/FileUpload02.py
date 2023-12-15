import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    print("beforeEach")
    page.goto("https://the-internet.herokuapp.com/upload")
    yield
    print("afterEach")


def test_main_navigation(page: Page):
    # Assertions use the expect API.
    expect(page).to_have_url("https://the-internet.herokuapp.com/upload")
    with page.expect_file_chooser() as fc:
        page.locator("//input[@id='file-upload']").click()
    file_c =  fc.value
    file_c.set_files("/Users/pramod/PycharmProjects/LearnPyPlaywright/code/file_upload/Playwright_File_Upload_Guide.pdf")
    page.locator("//input[@id='file-submit']").click()
    page.wait_for_load_state()
    # uploaded_file = page.locator("//div[@id='uploadeds-files']").text_content()
    # assert  uploaded_file == "Playwright_File_Upload_Guide.pdf"

