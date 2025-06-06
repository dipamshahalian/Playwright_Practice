from playwright.sync_api import sync_playwright
import os

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = context.new_page()
        page.goto("https://www.formula1.com/")
        page.set_viewport_size({"width": 1800, "height": 1200})
        input("Press Enter to close the browser...")
        # Ensure logs directory exists
        os.makedirs("logs", exist_ok=True)
        context.tracing.stop(path="logs/trace.zip")
        browser.close()

if __name__ == "__main__":
    main()