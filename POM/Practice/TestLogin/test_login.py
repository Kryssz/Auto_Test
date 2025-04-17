'''
Test case 1: Positive LogIn test
Open page
Type username student into Username field
Type password Password123 into Password field
Push Submit button
Verify new page URL contains practicetestautomation.com/logged-in-successfully/
Verify new page contains expected text ('Congratulations' or 'successfully logged in')
Verify button Log out is displayed on the new page

Test case 2: Negative username test
Open page
Type username incorrectUser into Username field
Type password Password123 into Password field
Push Submit button
Verify error message is displayed
Verify error message text is Your username is invalid!

Test case 3: Negative password testtest_form_validation.py
Open page
Type username student into Username field
Type password incorrectPassword into Password field
Push Submit button
Verify error message is displayed
Verify error message text is Your password is invalid!
'''

from POM.Practice.generate_browser import generate_chrome_driver
from page_model import LoginPage

class TestLogin(object):
    def setup_method(self):
        driver = generate_chrome_driver()
        self.login_page = LoginPage(driver)
        self.login_page.get()

    def teardown_method(self):
        self.login_page.quit()


    def test_positive_login(self):
        self.login_page.login('student', 'Password123')
        assert self.login_page.get_url() == 'https://practicetestautomation.com/logged-in-successfully/'
        assert self.login_page.message_success().text == 'Logged In Successfully'
        try:
            self.login_page.button_log_out().click()
        except Exception as e:
            assert False, f"Button could not be clicked: {e}"


    def test_negative_username(self):
        self.login_page.login('incorrectUser', 'Password123')
        assert self.login_page.message_error().is_displayed()
        assert self.login_page.message_error().text == 'Your username is invalid!'

    def test_negative_password(self):
        self.login_page.login('student', 'incorrectPassword')
        assert self.login_page.message_error().is_displayed()
        assert self.login_page.message_error().text == 'Your password is invalid!'

