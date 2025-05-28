import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width":1920,"height":1028})
    page = context.new_page()
    page.goto("http://localhost:4000/#/login?redirect_url=/67b448c342af43e63b38fda6/project/6834207579b2ebd7f9a2ba06/p?tab=ProjectListView")
    page.get_by_role("textbox", name="Email ID*").click()
    page.get_by_role("textbox", name="Email ID*").fill("riap1330+999@gmail.com")
    page.get_by_role("textbox", name="Password*").click()
    page.get_by_role("textbox", name="Password*").fill("VimalSir@223133")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="No").click()
    page.get_by_role("list").locator("div").nth(2).click()
    page.locator("div").filter(has_text=re.compile(r"^Delete$")).first.click()
    page.get_by_role("textbox", name="delete").click()
    page.get_by_role("textbox", name="delete").fill("delete")
    page.get_by_role("button", name="Delete").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
