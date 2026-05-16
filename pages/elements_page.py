from playwright.sync_api import Page, expect


class Elements:
    URL = "https://the-internet.herokuapp.com/add_remove_elements/"

    def __init__(self, page: Page):
        self.page = page
        self.push_add = page.get_by_role("button", name="Add Element")
        self.delete = page.get_by_role("button", name="Delete")

    def opens(self):
        self.page.goto(self.URL)

    def add_elemnt(self):
        self.push_add.click()

    def click_delete(self):
        self.delete.click()

    def delete_element(self):
        expect(self.delete).to_be_visible()

    def delete_removed(self):
        expect(self.delete).not_to_be_visible()
