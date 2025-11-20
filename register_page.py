from playwright.sync_api import Page
from faker import Faker

fake = Faker()

class RegisterPage:
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto('https://demo.nopcommerce.com/register')

    def register(self):
        email = fake.email()
        password = 'Test1234!'
        self.page.check('#gender-male')
        self.page.fill('#FirstName', fake.first_name())
        self.page.fill('#LastName', fake.last_name())
        self.page.fill('#Email', email)
        self.page.fill('#Password', password)
        self.page.fill('#ConfirmPassword', password)
        self.page.click('#register-button')
        return email, password
