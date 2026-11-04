from playwright.sync_api import Page
from utils.config import BASE_URL

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def load_ui(self):
        self.page.goto(BASE_URL)

    def navigate_to_login_page(self):
        self.load_ui()
        self.page.get_by_role("link", name="Log In").click()
        self.page.locator('[data-qa-id="login-hudl"]').click()

    def enter_email(self, email: str):
        self.page.locator('[data-qa-id="email-input-input"]').fill(email)

    def enter_password(self, password: str):
        self.page.locator('[data-qa-id="password-input-input"]').fill(password)

    def click_continue(self):
        self.page.get_by_role("button", name="Continue", exact=True).click()

    def click_forgot_password(self):
        self.page.get_by_role("link", name="Forgot password?").click()