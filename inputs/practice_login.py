# Login of alianhub.com using Playwright

# import re
# from playwright.sync_api import Playwright, sync_playwright, expect


# def run(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context(viewport={"width":1900,"height":1000})
#     page = context.new_page()
#     page.goto("https://alian.alianhub.com/#/login?redirect_url=/")
#     page.get_by_role("textbox", name="Email ID*").click()
#     page.get_by_role("textbox", name="Email ID*").fill("dipam.shah@aliansoftware.com")
#     page.get_by_role("textbox", name="Email ID*").press("Tab")
#     page.get_by_role("textbox", name="Password*").fill("#DipamShah10#")
#     page.get_by_role("button", name="Login").click()
#     page.get_by_role("button", name="No").click()

#     input("Press Enter to close the browser...")

#     # ---------------------
#     context.close()
#     browser.close()


# with sync_playwright() as playwright:
#     run(playwright)


# Now Login of COSEC to check the Daily Attendance

import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width":1900,"height":1000})
    page = context.new_page()
    page.goto("http://192.168.0.1/COSEC/Login/Login")
    page.get_by_role("textbox", name="User ID, Email or Mobile").fill("819")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("Dipam@223133")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name="Time Attendance ").click()
    page.get_by_role("link", name="Daily Attendance").click()

    input("Press Enter to close the browser...")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
