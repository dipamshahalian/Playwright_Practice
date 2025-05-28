import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width":1920,"height":1000})
    page = context.new_page()
    page.goto("http://localhost:4000/#/login?redirect_url=/")
    page.get_by_role("textbox", name="Email ID*").click()
    page.get_by_role("textbox", name="Email ID*").fill("riap1330+999@gmail.com")
    page.get_by_role("textbox", name="Password*").click()
    page.get_by_role("textbox", name="Password*").click()
    page.get_by_role("textbox", name="Password*").fill("VimalSir@223133")
    page.locator("form").get_by_role("img").click()
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="No").click()
    page.get_by_role("link", name="Projects").click()
    page.get_by_role("button", name="+ New Project").click()
    page.locator("#createblankproject_driver").get_by_role("button").click()
    page.get_by_role("textbox", name="Enter Project Name").click()
    page.get_by_role("textbox", name="Enter Project Name").fill("ALIAN SOFTWARE")
    page.get_by_role("textbox", name="Enter Key Name").click()
    page.get_by_role("textbox", name="Enter Key Name").fill("AGC")
    page.get_by_role("textbox", name="Enter Key Name").press("Tab")
    page.get_by_role("textbox", name="Select Category").click()
    page.locator("#item2").click()
    page.locator("[data-test-id=\"dp-input\"]").click()
    page.locator("[data-test-id=\"Sat May 31 2025 00\\:00\\:00 GMT\\+0530 \\(India Standard Time\\)\"]").get_by_text("31").click()
    page.get_by_role("img", name="add user").click()
    page.locator("#item0").get_by_text("Dipam Shah").click()

    page.get_by_role("img", name="closeButton").click()
    page.get_by_role("button", name="Next").click()
    # page.get_by_text("Upload").click()
    # page.locator("body").set_input_files("sf25_LH.jpg")
    page.get_by_role("button", name="Next").click()
    page.locator("div").filter(has_text=re.compile(r"^Alian's Workspace$")).click()
    page.get_by_role("button", name="Next").click()
    page.get_by_role("button", name="Next").click()
    page.get_by_role("button", name="Next").click()
    page.get_by_role("button", name="Next").click()
    page.get_by_role("button", name="Next").click()
    page.get_by_role("button", name="Next").click()
    page.get_by_role("button", name="Next").click()
    page.get_by_role("button", name="Create Project").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
