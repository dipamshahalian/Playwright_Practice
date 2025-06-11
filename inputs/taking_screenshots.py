from playwright.sync_api import sync_playwright
import os, time

def run():
    os.makedirs("screenshots", exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://books.toscrape.com")
        try:
            assert "Clothing" in page.title(), "Title check failed!"
        except AssertionError as e:
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            page.screenshot(path=f"screenshots/failure-{timestamp}.png", full_page=True)
            print("Screenshot taken due to failure.")
            raise e
        finally:
            browser.close()

if __name__ == "__main__":
    run()
