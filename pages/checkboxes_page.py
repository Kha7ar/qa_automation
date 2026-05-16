from playwright.sync_api import Page, expect

class CheckboxPage:
    URL = "https://the-internet.herokuapp.com/checkboxes"
    
    def __init__(self, page: Page):
        self.page = page
        self.first_checkbox = page.locator("input[type='checkbox']").first
        self.last_checkbox = page.locator("input[type='checkbox']").last
        
    
    def open(self):
        self.page.goto(self.URL)
    
    def check_first(self):
        self.first_checkbox.click()
    
    def uncheck_last(self):
        self.last_checkbox.click()
    
    def is_first_checked(self):
        expect(self.first_checkbox).to_be_checked()
    
    def is_last_unchecked(self):
        expect(self.last_checkbox).not_to_be_checked()