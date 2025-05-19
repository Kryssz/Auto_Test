from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Automated_tests.GeneralPage import GeneralPage

class LoginPage(GeneralPage):
    def __init__(self, driver=None):
        self.url = 'http://localhost:4200/'
        super().__init__(self.url, driver)
        self.role_dropdown = (By.ID, "role")

    def bar_button_login(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//button/a[text()="Login"]')))

    def input_username(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, 'username')))

    def input_password(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, 'password')))

    def button_login_page(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//form/button[text()="Login"]')))

    def bar_button_logout(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//button/a[text()="Logout"]')))

    def bar_button_my_profile(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//button/a[text()="My Profile"]')))

    def bar_button_beehive_list(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//button/a[text()="Beehive list"]')))

    def bar_button_main_page(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//button/a[text()="Main Page"]')))

    def bar_button_register(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//button/a[text()="Register"]')))

    def input_first_name(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, 'firstName')))

    def input_last_name(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, 'lastName')))

    def input_phone_number(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, 'phoneNumber')))

    def input_email(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, 'email')))

    def input_zipcode(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, 'zipcode')))

    def input_city(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, 'city')))

    def input_address(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, 'address')))

    def role_user(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//select/option[@value="ROLE_BEEFAMILY"]')))

    def role_owner(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//select/option[@value="ROLE_BEEKEEPER"]')))

    #Image upload not yet available!

    def button_submit(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//form/button[text()="Submit"]')))
