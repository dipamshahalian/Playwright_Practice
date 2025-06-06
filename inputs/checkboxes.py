import asyncio
from playwright.async_api import async_playwright, expect

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # Set headless to False to run in head mode
        context = await browser.new_context()
        await context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = await context.new_page()
        await page.set_viewport_size({"width": 1800, "height": 1200})
        await page.goto("https://demoqa.com/checkbox")

        # Actions
        await page.check('label[for="tree-node-home"]')
        await page.screenshot(path="checkbox.png")

        # Assertions
        assert await page.is_checked('label[for="tree-node-home"]') is True

        # Normalize text by removing line breaks
        result_text = await page.locator('#result').inner_text()
        normalized_text = result_text.replace('\n', '').replace(' ', '')
        expected_text = 'Youhaveselected:homedesktopnotescommandsdocumentsworkspacereactangularveuofficepublicprivateclassifiedgeneraldownloadswordFileexcelFile'
        assert normalized_text == expected_text, f"Expected: {expected_text}, but got: {normalized_text}"

        # Stop tracing
        await context.tracing.stop(path="checkbox.zip")

        # Close the browser
        await browser.close()
        input("Press Enter to close the browser...")

asyncio.run(main())
