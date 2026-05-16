from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.home_page import HomePage

def test_one(page: Page):
    pagehome = HomePage(page)
    pagehome.open()
    pagehome.action()
    pagehome.check()

def test_two(page: Page):
    login = LoginPage(page)
    login.open()
    login.login("tomsmith", "SuperSecretPassword!")
    expect(page).to_have_url("https://the-internet.herokuapp.com/secure")

def test_full_flow(page: Page):
    pagehome = HomePage(page)
    pagehome.open()
    pagehome.action()
    pagehome.check()
    login = LoginPage(page)
    login.open()
    login.login("tomsmith", "SuperSecretPassword!")
    expect(page).to_have_url("https://the-internet.herokuapp.com/secure")
    login.logout()
    expect(page).to_have_url("https://the-internet.herokuapp.com/login")


    

