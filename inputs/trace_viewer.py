from playwright.sync_api import sync_playwright
def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()

        context.tracing.start(
            screenshots=True,
            snapshots=True,
            sources=True,
        )

        page = context.new_page()
        page.goto("https://books.toscrape.com/")
        page.locator("article.product_pod h3 a").first.click()

        context.tracing.stop(path="trace.zip")
        
        browser.close()

if __name__ == "__main__":
    run()