import pytest
from playwright.sync_api import sync_playwright

def test_handle_alerts():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to site
        page.goto("https://the-internet.herokuapp.com/javascript_alerts")

        # ----------- Handle Alert Popup -----------
        def handle_alert(dialog):
            dialog.accept()
            print("Alert handled.")
        page.once("dialog", handle_alert)
        page.click("text=Click for JS Alert")

        # ----------- Handle Confirm Popup -----------
        page.once("dialog", lambda dialog: dialog.dismiss())
        page.click("text=Click for JS Confirm")
        print("Confirm popup dismissed.")

        # ----------- Handle Prompt Popup -----------
        def handle_prompt(dialog):
            print(f"Prompt Message: {dialog.message}")
            dialog.accept("Hello from Playwright!")
        page.once("dialog", handle_prompt)
        page.click("text=Click for JS Prompt")

        # Check result
        result = page.text_content("#result")
        print(f"Result Text: {result}")
        assert "Hello from Playwright!" in result

        browser.close()

if __name__ == "__main__":
    test_handle_alerts()
