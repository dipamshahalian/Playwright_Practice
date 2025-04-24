import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.firefox.launch(headless=False)  # Set headless to False to run in head mode
        page = await browser.new_page()
        await page.goto("https://whatismyuseragent.com/")
        print(await page.title())
        await browser.close()

    # print("test")

asyncio.run(main())