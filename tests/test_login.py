import re
from utils.config import HUDL_EMAIL, HUDL_PASSWORD, BASE_URL
from pages.login_page import LoginPage
from playwright.sync_api import expect

def test_ui_loads(page):
    login_page = LoginPage(page)
    login_page.load_ui()

    expect(page).to_have_url(f"{BASE_URL}/")


def test_login_page_loads(page):
    login_page = LoginPage(page)
    login_page.navigate_to_login_page()

    expect(page).to_have_url(
        re.compile(r"https://identity\.hudl\.com/u/login/identifier")
    )

def test_valid_login(page):
    login_page = LoginPage(page)
    login_page.navigate_to_login_page()

    login_page.enter_email(HUDL_EMAIL)
    login_page.click_continue()
    login_page.enter_password(HUDL_PASSWORD)
    login_page.click_continue()

    expect(page).to_have_url(
        re.compile(r"https://www\.hudl\.com/home")
    )

def test_invalid_email_format(page):
    login_page = LoginPage(page)
    login_page.navigate_to_login_page()

    login_page.enter_email("fakeemail")
    login_page.click_continue()

    expect(page.locator('[data-qa-id="email-input-help-text"]')).to_have_text(
        "Enter a valid email."
    )

def test_login_with_invalid_credentials(page):
    login_page = LoginPage(page)
    login_page.navigate_to_login_page()

    login_page.enter_email("fakeemail@example.com")
    login_page.click_continue()
    login_page.enter_password("password")
    login_page.click_continue()

    expect(page.locator('[data-qa-id="password-input-help-text"]')).to_have_text(
        "Incorrect username or password."
    )

def test_login_with_empty_email(page):
    login_page = LoginPage(page)
    login_page.navigate_to_login_page()

    login_page.enter_email("")
    login_page.click_continue()

    expect(page.locator('[data-qa-id="email-input-help-text"]')).to_have_text(
        "Please enter your email address"
    )

def test_login_with_empty_password(page):
    login_page = LoginPage(page)
    login_page.navigate_to_login_page()

    login_page.enter_email(HUDL_EMAIL)
    login_page.click_continue()

    login_page.enter_password("")
    login_page.click_continue()

    expect(page.locator('[data-qa-id="password-input-help-text"]')).to_have_text(
        "Please enter your password"
    )


    