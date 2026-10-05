from config.settings import BASE_URL
from playwright.sync_api import expect

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username = page.get_by_placeholder("Username")
        self.password = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")

    def open(self):
        self.page.goto(BASE_URL)

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()

    def verify_login_success(self):
        expect(self.page).to_have_url("https://www.saucedemo.com/inventory.html")
