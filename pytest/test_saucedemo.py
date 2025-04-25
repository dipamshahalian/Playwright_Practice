from playwright.sync_api import Page
import pytest

# @pytest.mark.skip_browser("chromium") # Skip the test for Chromium browser
# @pytest.mark.only_browser("firefox") # Run the test only for Firefox browser
def test_title(page: Page):
    page.goto("/") # Dynamic URL for that I've to mention it in the command i.e. pytest --base-url=https://www.saucedemo.com/
    assert page.title() == "Swag Labs"

def test_inventory_site(page: Page):
    page.goto("/inventory.html")
    assert page.inner_text('h3') == "Epic sadface: You can only access '/inventory.html' when you are logged in."