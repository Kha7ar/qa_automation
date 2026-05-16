from playwright.sync_api import Page, expect

class DynamoLoad1:
    URL = "https://the-internet.herokuapp.com/dynamic_loading/1"

    def __init__(self, page: Page):
        self.page = page
        self.start_button = page.get_by_role("button", name="Start")
        self.result_name = page.locator("#finish")


    def open(self):
         self.page.goto(self.URL)

    def button_action(self):
        self.start_button.click()

    def is_loaded(self):
        expect(self.result_name).to_be_visible(timeout=10000)

    def is_hidden(self):
        expect(self.result_name).to_be_hidden()

    


