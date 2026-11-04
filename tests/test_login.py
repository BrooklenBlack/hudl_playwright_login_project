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

    expect(page).to_have_url(re.compile(r"https://identity\.hudl\.com/u/login/identifier"))

def test_valid_login(page):
    login_page = LoginPage(page)
    login_page.navigate_to_login_page()

    login_page.enter_email(HUDL_EMAIL)
    login_page.click_continue()
    login_page.enter_password(HUDL_PASSWORD)
    login_page.click_continue()

    expect(page).to_have_url(re.compile(r"https://www\.hudl\.com/home"))