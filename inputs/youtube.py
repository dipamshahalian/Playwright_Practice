# This script uses Playwright to automate a web browser to search for a specific song on YouTube and play it.

import asyncio
from playwright.async_api import async_playwright

async def search_youtube():
    async with async_playwright() as p:
        # Launch a browser (Chromium)
        browser = await p.chromium.launch(headless=False)  # Set headless=True to run without UI
        context = await browser.new_context()
        page = await context.new_page()

        # Go to YouTube
        await page.goto("https://www.youtube.com")

        # Wait for the search box to be visible using the class
        search_box = page.locator('.yt-searchbox-input')
        await search_box.wait_for(state="visible")

        # Search for "Justin Bieber"
        await search_box.fill("Justin Bieber")
        await search_box.press("Enter")

        # Wait for the results to load
        await asyncio.sleep(3)

        # Locate the specific song using a refined locator and click on it
        song = page.locator('//a[@title="DJ Snake - Let Me Love You ft. Justin Bieber"]')
        await song.wait_for(state="visible")
        await song.click()

        # Wait for 30 seconds while the song plays
        await asyncio.sleep(30)

        # Close the browser
        await browser.close()

# Run the function

asyncio.run(search_youtube())