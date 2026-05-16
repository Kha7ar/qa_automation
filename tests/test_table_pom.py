from playwright.sync_api import Page, expect
from pages.tables_page import TablePage

def test_table(page: Page):
    tables = TablePage(page)
    tables.open()
    tables.is_header_visible
    tables.is_table_visible


