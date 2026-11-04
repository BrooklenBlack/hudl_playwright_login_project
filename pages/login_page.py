from playwright.sync_api import Page
from utils.config import BASE_URL

class LoginPage:
    def __init__(self, page: Page):
        self.page = page