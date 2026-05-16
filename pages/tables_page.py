from playwright.sync_api import Page, expect

class TablePage:
    URL = "https://the-internet.herokuapp.com/tables"


    def __init__(self, page: Page):
        self.page = page
        self.table = page.locator("#table1")
        self.table_name = page.locator("#table1 th")

    def open(self):
        self.page.goto(self.URL)

    def is_table_visible(self):
        expect(self.table).to_be_visible()

    def is_header_visible(self):
        expect(self.table_name.nth(0)).to_have_text("Last Name")
        expect(self.table_name.nth(1)).to_have_text("First Name")
        expect(self.table_name.nth(2)).to_have_text("Email")