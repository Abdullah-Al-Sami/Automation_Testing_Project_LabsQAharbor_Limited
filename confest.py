import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="function")
def browser(playwright):
    # Launch Chromium browser in non-headless mode
    browser = playwright.chromium.launch(headless=False)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def page(browser):
    # Create a new page in the browser
    page = browser.new_page()
    yield page
    page.close()

