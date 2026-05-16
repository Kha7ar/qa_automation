from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.dropdown_page import DropdownPage
from pages.checkboxes_page import CheckboxPage
from pages.Dynamical_page import DynamoLoad1

def test_one(page: Page):
    login = LoginPage(page)
    login.open()
    expect(page).to_have_title("The Internet")


def test_two(page: Page):
    login = LoginPage(page)
    login.open()
    login.login("tomsmith", "SuperSecretPassword!")
    expect(page).to_have_url("https://the-internet.herokuapp.com/secure")
    page.get_by_role("link", name="Logout").click()
    expect(page).to_have_url("https://the-internet.herokuapp.com/login")


def test_three(page: Page):
    dropdown = DropdownPage(page)
    dropdown.open()
    dropdown.select_option("Option 2")
    assert dropdown.get_value() == "2"



def test_five(page: Page):
    checkbox = CheckboxPage(page)
    checkbox.open()
    checkbox.check_first()
    checkbox.is_first_checked()
    checkbox.uncheck_last()
    checkbox.is_last_unchecked()


def test_six(page: Page):
    login = LoginPage(page)
    login.open()
    login.login("wrongname", "wrongpassword")
    expect(page).to_have_url("https://the-internet.herokuapp.com/login")


def test_seven(page: Page):
    login = LoginPage(page)
    login.open()
    login.login("tomsmith", "SuperSecretPassword!")
    expect(page).to_have_url("https://the-internet.herokuapp.com/secure")
    expect(page.get_by_text("Welcome to the Secure Area")).to_be_visible


def test_eight(page: Page):
    login = LoginPage(page)
    login.open()
    login.login("tomsmith", "SuperSecretPassword!")
    expect(page).to_have_url("https://the-internet.herokuapp.com/secure")
    page.get_by_role("link", name="Logout").click()
    expect(page).to_have_url("https://the-internet.herokuapp.com/login")


def test_nine(page: Page):
    dynamic = DynamoLoad1(page)
    dynamic.open()
    dynamic.button_action()
    dynamic.is_hidden()
    dynamic.is_loaded()



    
    
    

