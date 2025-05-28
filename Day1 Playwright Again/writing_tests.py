# import pytest
# from playwright.sync_api import Page, Browser, BrowserContext, sync_playwright, expect

# @pytest.fixture(scope="session")
# def browser_context_args(browser_context_args):
#     return {**browser_context_args, "viewport": {"width": 1280, "height": 720}}

# @pytest.fixture(scope="session")
# def browser_type_launch_args(browser_type_launch_args):
#     return {**browser_type_launch_args, "headless": False}

# @pytest.fixture(scope="function", autouse=True)
# def before_each_after_each(page: Page):
#     print("before the test runs")
#     # Go to the starting url before each test.
#     page.goto("https://playwright.dev/")
#     yield
#     print("after the test runs")

# def test_main_navigation(page: Page):
#     # Assertions use the expect API.
#     expect(page).to_have_url("https://playwright.dev/")


from playwright.sync_api import sync_playwright

def test_actual_h1():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://fornula1.com")
        heading = page.locator("h1")
        print(heading.text_content())
        browser.close()
