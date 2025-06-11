import pytest
from pages.login_page import LoginPage

def test_valid_login(page):
    login = LoginPage(page)
    login.navigate()
    login.login("student", "Password123")

    assert page.url == "https://practicetestautomation.com/logged-in-successfully/"
