from Selenium.BeeRelaxed.Automated_tests.generate_browers import generate_chrome_driver
from Selenium.BeeRelaxed.Automated_tests.BeeRelaxed.page_model_user import LoginPage


class TestPassword(object):
    def __init__(self):
        self.login_page = None

    def setup_method(self):
        driver = generate_chrome_driver()
        self.login_page = LoginPage(driver)
        self.login_page.get()

    def teardown_method(self):
        self.login_page.quit()


    def test_user_registration(self):
        pass