from playwright.sync_api import Page, expect


def test_checkboxes(page: Page):
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    page.locator("input[type='checkbox']").first.click()
    expect(page.locator("input[type='checkbox']").first).to_be_checked()


def test_login_logout(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.get_by_role("button", name="Login").click()
    expect(page).to_have_url("https://the-internet.herokuapp.com/secure")
    page.get_by_role("link", name="Logout").click()
    expect(page).to_have_url("https://the-internet.herokuapp.com/login")


def test_checkboxes(page: Page):
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    page.locator("input[type='checkbox']").first.click()
    expect(page.locator("input[type='checkbox']").first).to_be_checked()


def test_page_text(page: Page):
    page.goto("https://the-internet.herokuapp.com/")
    expect(page).to_have_title("The Internet")
    expect(page.get_by_text("Available Examples")).to_be_visible()


def test_dropdown(page: Page):
    page.goto("https://the-internet.herokuapp.com/dropdown")
    page.locator("#dropdown").select_option("Option 1")
    expect(page.locator("#dropdown")).to_have_value("1")


def test_dynamic_text(page: Page):
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/1")
    page.get_by_role("button", name="Start").click()
    expect(page.locator("#finish")).to_be_visible(timeout=10000)


def test_full_flow(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    expect(page).to_have_title("The Internet")
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.get_by_role("button", name="Login").click()
    expect(page).to_have_url("https://the-internet.herokuapp.com/secure")
    expect(page.get_by_role("heading", name="Secure Area", exact=True)).to_be_visible()
    page.get_by_role("link", name="Logout").click()
    expect(page).to_have_url("https://the-internet.herokuapp.com/login")


def test_dropdown_all_options(page: Page):
    page.goto("https://the-internet.herokuapp.com/dropdown")
    page.locator("#dropdown").select_option("Option 1")
    expect(page.locator("#dropdown")).to_have_value("1")
    page.locator("#dropdown").select_option("Option 2")
    expect(page.locator("#dropdown")).to_have_value("2")


def test_both_checkboxes(page: Page):
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    #page.locator("button", name="checkbox").click()
    page.locator("input[type='checkbox']").first.click()
    expect(page.locator("input[type='checkbox']").first).to_be_checked()
    page.locator("input[type='checkbox']").last.click()
    expect(page.locator("input[type='checkbox']").last).not_to_be_checked()


def test_forgot_password(page: Page):
    page.goto("https://the-internet.herokuapp.com/forgot_password")
    page.locator("#email").fill("tesr@mail.com")
    page.get_by_role("button", name="Retrieve password").click()
    expect(page.get_by_text("Internal Server Error")).to_be_visible(timeout=10000)


def test_check_uncheck(page: Page):
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    page.locator("input[type='checkbox']").first.click()
    expect(page.locator("input[type='checkbox']").first).to_be_checked()
    page.locator("input[type='checkbox']").first.click()
    expect(page.locator("input[type='checkbox']").first).not_to_be_checked()
    page.locator("input[type='checkbox']").last.click()
    expect(page.locator("input[type='checkbox']").last).not_to_be_checked()


def test_navigation(page: Page):
    page.goto("https://the-internet.herokuapp.com/")
    expect(page).to_have_title("The Internet")
    page.get_by_role("link", name="Form Authentication").click(timeout=10000)
    expect(page).to_have_url("https://the-internet.herokuapp.com/login")
    expect(page.get_by_text("Login Page")).to_be_visible()


def test_secure_area(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.get_by_role("button", name="Login").click()
    expect(page).to_have_url("https://the-internet.herokuapp.com/secure")
    expect(page.get_by_text("You logged into a secure area!")).to_be_visible()
    page.get_by_role("link", name="Logout").click()
    expect(page).to_have_url("https://the-internet.herokuapp.com/login")


def test_dropdown_title(page: Page):
    page.goto("https://the-internet.herokuapp.com/dropdown")
    expect(page).to_have_title("The Internet")
    page.locator("#dropdown").select_option("Option 1")
    expect(page.locator("#dropdown")).to_have_value("1")
    page.locator("#dropdown").select_option("Option 2")
    expect(page.locator("#dropdown")).to_have_value("2")
    expect(page.get_by_text("Dropdown List")).to_be_visible()


def test_dynamic(page: Page):
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/2")
    page.get_by_role("button", name="Start").click()
    expect(page.get_by_text("Hello World!")).to_be_visible(timeout=10000)


def test_multi_navigation(page: Page):
    page.goto("https://the-internet.herokuapp.com")
    page.get_by_role("link", name="Checkboxes").click()
    expect(page).to_have_url("https://the-internet.herokuapp.com/checkboxes")
    page.locator("input[type='checkbox']").first.click()
    expect(page.locator("input[type='checkbox']").first).to_be_checked()
    page.locator("input[type='checkbox']").last.click()
    expect(page.locator("input[type='checkbox']").last).not_to_be_checked()


def test_invalid_login(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("#username").fill("wronguser")
    page.locator("#password").fill("wrongpass")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text("Your username is invalid!")).to_be_visible()
    expect(page).to_have_url("https://the-internet.herokuapp.com/login")


def test_full(page: Page):
    page.goto("https://the-internet.herokuapp.com")
    expect(page).to_have_title("The Internet")
    page.get_by_role("link", name="Dropdown").click()
    page.locator("#dropdown").select_option("Option 2")
    expect(page.locator("#dropdown")).to_have_value("2")
    page.go_back()
    expect(page).to_have_url("https://the-internet.herokuapp.com/")

