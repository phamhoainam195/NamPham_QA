from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto('https://demo.nopcommerce.com/login')

    def login(self, email, password):
        self.page.fill('#Email', email)
        self.page.fill('#Password', password)
        self.page.click('button.login-button')
