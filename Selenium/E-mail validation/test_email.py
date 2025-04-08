from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://high-flyer.hu/hetihazi/feladat2_email.html'


class TestEmail(object):
    def setup_method(self):
        options = Options()
        options.add_argument('--disable-search-engine-choice-screen')
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.get(URL)

    def teardown_method(self):
        self.driver.quit()

    def test_invalid_email(self):
        test_data = 'teszt@'
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'email'))).send_keys(test_data)
        self.driver.find_element(By.ID, 'submit').click()
        error_msg = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//div[@class="validation-error"]')))
        assert error_msg.text == f"Please enter a part following '@'. '{test_data}' is incomplete."

    def test_empty_email(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'submit'))).click()
        error_msg = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//div[@class="validation-error"]')))
        assert error_msg.text == f'Please fill out this field.'

    def test_valid_email(self):
        test_data = 'teszt@elek.hu'
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'email'))).send_keys(test_data)
        self.driver.find_element(By.ID, 'submit').click()

        elements = self.driver.find_elements(By.XPATH, '//div[@class="validation-error"]')
        assert len(elements) == 0, "Validation error appeared when it shouldn't have."
