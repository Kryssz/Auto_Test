import pytest
from Selenium.BeeRelaxed.Automated_tests.generate_browers import generate_chrome_driver
from Selenium.BeeRelaxed.Automated_tests.BeeRelaxed.page_model_registration import LoginPage


class TestLoginFlow:
    def setup_method(self, method):
        self.driver = generate_chrome_driver()
        self.page = LoginPage(self.driver)
        self.page.get()

    def teardown_method(self, method):
        self.driver.quit()

    def test_login_button_clickable(self):
        btn = self.page.bar_button_login()
        assert btn.is_enabled()
        btn.click()
        assert self.page.button_login_page().is_displayed()