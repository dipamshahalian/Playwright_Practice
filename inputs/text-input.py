import asyncio
from playwright.async_api import async_playwright, expect

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        await context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = await context.new_page()
        await page.set_viewport_size({"width": 1800, "height": 1200})
        await page.goto("https://demoqa.com/text-box")
        #-Filling text-inputs
        await page.fill('#userName', 'Dipam')
        await page.fill('#userEmail', 'dipam@alian.com')
        await page.fill('#currentAddress', 'Moon')
        await page.fill('#permanentAddress', 'yourHeart')
        #-Actions
        await page.click('#submit')
        await page.screenshot(path="screenshots/text-boxes.png")
        #-Assertions
        await expect(page.locator("p#name")).to_have_text("Name:Dipam")
        await expect(page.locator("p#email")).to_have_text("Email:dipam@alian.com")
        await expect(page.locator("p#currentAddress")).to_have_text("Current Address :Moon")
        await expect(page.locator("p#permanentAddress")).to_have_text("Permananet Address :yourHeart")
        #-Stoping Tracing
        await context.tracing.stop(path = "logs/trace.zip")
        #-Closing browser
        await browser.close()


asyncio.run(main())