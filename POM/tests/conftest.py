import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"]) # Launch browser in non-headless mode and maximized (for maximizing there are other options too) 
        context = browser.new_context(no_viewport=True)  # No viewport to maximize the window
        page = context.new_page()
        yield page
        browser.close()