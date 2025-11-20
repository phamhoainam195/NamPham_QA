from pages.login_page import LoginPage
import json

def test_signin(page):
    data = json.load(open('data/user.json'))
    login = LoginPage(page)
    login.open()
    login.login(data['email'], data['password'])
    assert page.locator('.ico-account').is_visible()
