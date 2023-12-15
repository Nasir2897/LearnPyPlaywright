import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    print("beforeEach")
    page.goto("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
    yield
    print("afterEach")


def test_main_navigation(page: Page):
    # Assertions use the expect API.
    expect(page).to_have_url("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
    with page.expect_download() as d:
        page.locator("//tbody/tr[1]/td[5]/a[1]").click()
    d = d.value
    file_path = d.path()
    print(f"File downloaded to: {file_path}")


