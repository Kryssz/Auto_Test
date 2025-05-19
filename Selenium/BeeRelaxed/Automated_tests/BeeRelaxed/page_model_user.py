from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Automated_tests.GeneralPage import GeneralPage

class LoginPage(GeneralPage):
    def __init__(self, driver=None):
        self.url = 'http://localhost:4200/'
        super().__init__(self.url, driver)

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

    def bar_button_logo(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//div/a/img[@class="logo"]')))

    def button_carousel_left(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//button/span[@class="carousel-control-next-icon"]')))

    def button_carousel_right(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//button/span[@class="carousel-control-prev-icon"]')))
