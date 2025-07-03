from gui_tests.utils.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_input = page.locator('#username')
        self.password_input = page.locator('#password')
        self.login_button = page.locator('#doLogin')

    def login(self, username="admin", password="password"):
        self.safe_fill(self.username_input, username)
        self.safe_fill(self.password_input, password)
        self.safe_click(self.login_button)
