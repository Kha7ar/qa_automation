from playwright.sync_api import Page, expect

class HomePage:
    URL = "https://the-internet.herokuapp.com"


    def __init__(self, page: Page):
        self.page = page
        self.perexod = page.get_by_role("link", name="Form Authentication")
        

    def open(self):
        self.page.goto(self.URL)    

    def action(self):
        self.perexod.click()

    def check(self):
        expect(self.show_title)

    def check(self):
        expect(self.page).to_have_title("The Internet")
        