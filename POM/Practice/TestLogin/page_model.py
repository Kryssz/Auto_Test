from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from POM.Practice.GeneralPage import GeneralPage

class LoginPage(GeneralPage):
    def __init__(self, driver=None):
        self.url = 'https://practicetestautomation.com/practice-test-login/'
        super().__init__(self.url, driver)

    def input_username(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, 'username')))

    def input_password(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, 'password')))

    def button_submit(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, 'submit')))

    def button_log_out(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//a[text()="Log out"]')))

    def message_success(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//h1[@class="post-title"]')))

    def message_error(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, 'error')))

    def login(self, username, password):
        self.input_username().send_keys(username)
        self.input_password().send_keys(password)
        self.button_submit().click()





