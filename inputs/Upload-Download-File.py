import os

from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/upload")

    # Use the absolute path directly
    file_path = "D:/sf25_LH.png"

    page.set_input_files('#file-upload', file_path)

    page.locator("text=Upload").click()

    page.wait_for_timeout(10000)

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)