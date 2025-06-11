def test_home_page_title(page):
    page.goto("https://books.toscrape.com")
    assert "Books" in page.title()
    print(f"Page title: ", page.title())
