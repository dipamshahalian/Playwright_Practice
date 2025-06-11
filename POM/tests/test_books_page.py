import pytest
from POM.pages.books_page import BooksPage
from POM.utils.helpers import take_screenshot

def test_first_book_title(page):
    books = BooksPage(page)
    books.navigate()
    
    title = books.get_first_book_title()
    assert "A Light" in title  # This might fail intentionally

    take_screenshot(page, "first_book_title")