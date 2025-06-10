from playwright.sync_api import sync_playwright
def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://books.toscrape.com/")
        
        # Page title using JavaScript execution
        titile = page.evaluate("() => document.title")
        print(f"Page title: {titile}")

        print("Scrolling to bottom of the page...")
        page.evaluate("() => window.scrollTo(0, document.body.scrollHeight)")

        book_count = page.evaluate("() => document.querySelectorAll('article.product_pod').length")
        print("Number of books on this page:", book_count)

        first_price = page.evaluate("""
            () => {
                const priceEl = document.querySelector('article.product_pod .price_color');
                return priceEl ? priceEl.textContent : 'Not found';
            }
        """)
        print("First book price:", first_price)

        page.locator("article.product_pod h3 a").first.click()

        description = page.evaluate("""
            () => {
                const para = document.querySelector('#product_description + p');
                return para ? para.innerText : 'No description found';
            }
        """)
        print("Description:", description)


        input("Press Enter to continue...")
        browser.close()
if __name__ == "__main__":
    run()