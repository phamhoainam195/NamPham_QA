from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto('https://demo.nopcommerce.com/')

    def is_loaded(self):
        return self.page.locator('.header-logo')
