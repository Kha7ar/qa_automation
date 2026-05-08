from playwright.sync_api import Page, expect
from pages.dropdown_page import DropdownPage

def test_select_option1(page: Page):
    dropdown = DropdownPage(page)
    dropdown.open()
    dropdown.select_option("Option 1")
    assert dropdown.get_value() == "1"

def test_select_option2(page: Page):
    dropdown = DropdownPage(page)
    dropdown.open()
    dropdown.select_option("Option 2")
    assert dropdown.get_value() == "2"

def test_both_options(page: Page):
    dropdown = DropdownPage(page)
    dropdown.open()
    dropdown.select_option("Option 1")
    assert dropdown.get_value() == "1"
    dropdown.select_option("Option 2")
    assert dropdown.get_value() == "2"