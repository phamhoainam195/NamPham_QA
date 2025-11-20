from pages.register_page import RegisterPage

def test_signup(page):
    reg = RegisterPage(page)
    reg.open()
    email, _ = reg.register()
    assert 'completed' in page.locator('.result').inner_text().lower()
