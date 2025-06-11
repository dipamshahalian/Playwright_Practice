class BooksPage:
    def __init__(self, page):
        self.page = page
        self.first_book = page.locator("article.product_pod:nth-child(1) h3 a")

    def navigate(self):
        self.page.goto("https://books.toscrape.com")

    def get_first_book_title(self):
        # Update the locator to select only the first element
        return self.page.locator("article.product_pod h3 a").first.text_content()

    def click_first_book(self):
        self.first_book.click()