from playwright.sync_api import Page, expect


class DropdownPage:
    URL = "https://the-internet.herokuapp.com/dropdown"

    def __init__(self, page: Page):
        self.page = page
        self.dropdown = page.locator("#dropdown")

    def open(self):
        self.page.goto(self.URL)

    def select_option(self, option: str):
        self.dropdown.select_option(option)

    def get_value(self) -> str:
        return self.dropdown.input_value() 