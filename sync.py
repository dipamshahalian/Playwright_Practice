# Headless Mode

# from playwright.sync_api import sync_playwright

# with sync_playwright() as p:
#     browser = p.chromium.launch()
#     page = browser.new_page()
#     page.goto("https://whatismyuseragent.com/")
#     page.screenshot(path = "demo.png")
#     browser.close()

# Now with the Head mode

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # Set headless to False to run in head mode
    page = browser.new_page()
    page.goto("https://aliansoftware.com/")
    page.screenshot(path = "demo1.png")
    browser.close()
