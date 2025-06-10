from playwright.sync_api import sync_playwright
def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://books.toscrape.com")
        assert "Books" in page.title(), "Page title does not contain 'Books'"

        price_text = page.locator(".price_color").first.text_content()
        assert price_text.startswith("£"), f"Unexpected price format: {price_text}"

        assert page.locator("h1").is_visible(), "Heading is not visible"
        
        # assert page.locator("button[type='submit']").is_enabled(), "Submit button is disabled"
        
        heading = page.locator("h1").text_content()
        assert heading == "All products", f"Expected heading 'All products' but got '{heading}'"

        books = page.locator("article.product_pod")
        assert books.count() == 20, f"Expected 20 books, found {books.count()}"

        first_book = page.locator("article.product_pod h3 a").first
        first_book.click()

        # Verify description exists
        description = page.locator("#product_description ~ p").text_content()
        assert "We don’t" not in description, "Unexpected text in product description"




        browser.close()
if __name__ == "__main__":
    run()