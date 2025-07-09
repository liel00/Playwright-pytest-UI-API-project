from gui_tests.utils.BasePage import BasePage


class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.admin_button = page.locator('a.nav-link[href="/admin"]')

    # This method clicks the admin button on the home page
    def click_admin_button(self):
        self.safe_click(self.admin_button)
