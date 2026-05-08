from playwright.sync_api import Page, expect

def test_title(page: Page):
    page.goto("https://playwright.dev")
    expect(page).to_have_title("Fast and reliable end-to-end testing for modern web apps | Playwright")

def test_get_started(page: Page):
    page.goto("https://playwright.dev")
    page.get_by_role("link", name="Get started").click()
    expect(page).to_have_url("https://playwright.dev/docs/intro")

def test_login(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.get_by_role("button", name="Login").click()
    expect(page.locator(".flash.success")).to_be_visible()

def test_invalid_login(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("#username").fill("wronguser")
    page.locator("#password").fill("wrongpassword")
    page.get_by_role("button", name="Login").click()
    expect(page.locator(".flash.error")).to_be_visible()


