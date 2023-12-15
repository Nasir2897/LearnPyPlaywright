import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        yield browser
        browser.close()

def test_webtables(browser):
    page = browser.new_page()
    URL = "https://awesomeqa.com/webtable.html"
    page.goto(URL)

    # Number of Rows and Columns in the table
    row_elements = page.locator("//table[@id='customers']/tbody/tr")
    col_elements = page.locator("//table[@id='customers']/tbody/tr[2]/td")

    row_count = row_elements.count()
    col_count = col_elements.count()

    print(row_count)
    print(col_count)

    # Loop through rows and columns to print data
    for i in range(2, row_count + 1):
        for j in range(1, col_count + 1):
            data = page.locator(f"//table[@id='customers']/tbody/tr[{i}]/td[{j}]").text_content()
            print(data, end=" ")
        print()

    # Find Helen Bennett's country
    for i in range(2, row_count + 1):
        name = page.locator(f"//table[@id='customers']/tbody/tr[{i}]/td[1]").text_content()
        if "Helen Bennett" in name:
            country = page.locator(f"//table[@id='customers']/tbody/tr[{i}]/td[3]").text_content()
            print("------")
            print(f"Helen Bennett is in - {country}")

    print(" ||||||||||||||||||||||| \n")

    # Navigate to another URL
    page.goto("https://awesomeqa.com/webtable1.html")

    # Get the table
    rows_table = page.locator("//table[@summary='Sample Table']/tbody/tr")

    # Loop through rows and columns to print data
    row_count = rows_table.count()
    for i in range(row_count):
        columns_table = rows_table.nth(i).locator("td")
        col_count = columns_table.count()
        for j in range(col_count):
            print(columns_table.nth(j).text_content())

    # Close the page
    page.close()
