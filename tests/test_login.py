import re

from playwright.sync_api import expect

from pages.login_page import LoginPage
from utils.config import BASE_URL, HUDL_EMAIL, HUDL_PASSWORD


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

    expect(page).to_have_url(re.compile(r"https://www\.hudl\.com/home"))


def test_uppercase_email_format(page):
    login_page = LoginPage(page)
    login_page.navigate_to_login_page()

    login_page.enter_email(HUDL_EMAIL.upper())
    login_page.click_continue()
    login_page.enter_password(HUDL_PASSWORD)
    login_page.click_continue()

    expect(page).to_have_url(re.compile(r"https://www\.hudl\.com/home"))


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

    login_page.enter_email("fakeemail4@example.com")
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


def test_forgot_password_link(page):
    login_page = LoginPage(page)
    login_page.navigate_to_login_page()

    login_page.enter_email(HUDL_EMAIL)
    login_page.click_continue()

    login_page.click_forgot_password()

    expect(page).to_have_url(
        re.compile(r"https://identity\.hudl\.com/u/reset-password/request")
    )
    expect(page.get_by_role("heading", name="Reset Password")).to_be_visible()


def test_forgot_password_submission(page):
    login_page = LoginPage(page)
    login_page.navigate_to_login_page()

    login_page.enter_email(HUDL_EMAIL)
    login_page.click_continue()

    login_page.click_forgot_password()
    login_page.click_continue()

    expect(page.get_by_role("heading", name="Check your email")).to_be_visible()


def test_password_visibility_toggle(page):
    login_page = LoginPage(page)
    login_page.navigate_to_login_page()

    login_page.enter_email(HUDL_EMAIL)
    login_page.click_continue()

    password_input = page.locator('[data-qa-id="password-input-input"]')
    toggle_button = page.locator('[data-qa-id="toggle-password-visibility"]')

    password_input.fill(HUDL_PASSWORD)
    expect(password_input).to_have_attribute("type", "password")

    toggle_button.click()
    expect(password_input).to_have_attribute("type", "text")

    toggle_button.click()
    expect(password_input).to_have_attribute("type", "password")

    expect(password_input).to_have_value(HUDL_PASSWORD)


def test_navigate_back_to_email_input(page):
    login_page = LoginPage(page)
    login_page.navigate_to_login_page()

    login_page.enter_email(HUDL_EMAIL)
    login_page.click_continue()

    back_button = page.locator('[data-qa-id="edit-identifier"]')
    back_button.click()

    expect(page).to_have_url(
        re.compile(r"https://identity\.hudl\.com/u/login/identifier")
    )


def test_navigate_back_to_email_input_and_change_email(page):
    login_page = LoginPage(page)
    login_page.navigate_to_login_page()

    login_page.enter_email(HUDL_EMAIL)
    login_page.click_continue()

    back_button = page.locator('[data-qa-id="edit-identifier"]')
    back_button.click()

    new_email = "newemail@example.com"
    login_page.enter_email(new_email)
    login_page.click_continue()

    expect(page).to_have_url(
        re.compile(r"https://identity\.hudl\.com/u/login/password")
    )
