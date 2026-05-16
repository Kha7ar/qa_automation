from playwright.sync_api import Page, expect
from pages.elements_page import Elements

def test_first(page: Page):
    element = Elements(page)
    element.opens()
    element.add_elemnt()
    element.delete_element()


def test_two(page: Page):
    element = Elements(page)
    element.opens()
    element.add_elemnt()
    element.click_delete()
    element.delete_removed()