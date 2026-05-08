from playwright.sync_api import Page, expect


class LoginPage:
    # ДАННЫЕ — локаторы страницы
    URL = "https://the-internet.herokuapp.com/login"

    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator("#username")
        self.password = page.locator("#password")
        self.login_button = page.get_by_role("button", name="Login")
        self.logout_button = page.get_by_role("link", name="Logout")

    # ДЕЙСТВИЯ — что можно делать на странице
    def open(self):
        self.page.goto(self.URL)

    def login(self, username: str, password: str):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()

    def logout(self):
        self.logout_button.click()