from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

def test_valid_login(page: Page):
    login = LoginPage(page)  # создаём объект страницы
    login.open()             # открываем страницу
    login.login("tomsmith", "SuperSecretPassword!")  # логинимся
    expect(page).to_have_url("https://the-internet.herokuapp.com/secure")

def test_invalid_login(page: Page):
    login = LoginPage(page)
    login.open()
    login.login("wronguser", "wrongpass")
    expect(page).to_have_url("https://the-internet.herokuapp.com/login")

def test_login_logout(page: Page):
    login = LoginPage(page)
    login.open()
    login.login("tomsmith", "SuperSecretPassword!")
    expect(page).to_have_url("https://the-internet.herokuapp.com/secure")
    login.logout()
    expect(page).to_have_url("https://the-internet.herokuapp.com/login")