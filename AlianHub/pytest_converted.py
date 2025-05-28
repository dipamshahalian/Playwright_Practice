import pytest
from playwright.sync_api import sync_playwright, expect

@pytest.fixture(scope="session")
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(viewport={"width":1920, "height":1000})
        yield context
        context.close()
        browser.close()

def test_create_project(browser_context):
    page = browser_context.new_page()
    page.goto("http://localhost:4000/#/login?redirect_url=/")
    
    # your interactions here
    page.get_by_role("textbox", name="Email ID*").fill("riap1330+999@gmail.com")
    page.get_by_role("textbox", name="Password*").fill("VimalSir@223133")
    page.get_by_role("button", name="Login").click()
    
    # Add assertions
    expect(page.get_by_role("link", name="Projects")).to_be_visible()

    input("Press Enter to continue...")

    # Continue the rest of your steps
