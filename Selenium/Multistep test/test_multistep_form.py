from io import BytesIO

from TESTDATA import TESTDATA_MULTISTEP
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

URL = 'https://high-flyer.hu/selenium/multistepform.html'


class TestMultiStep(object):
    def setup_method(self):
        options = Options()
        options.add_argument('--disable-search-engine-choice-screen')
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        # self.driver.maximize_window()
        self.driver.get(URL)

    def teardown_method(self):
        pass #self.driver.quit()

    def test_multistep(self):
        first_name = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, 'first_name')))
        first_name.send_keys(TESTDATA_MULTISTEP['First_name'])
        last_name = self.driver.find_element(By.ID, 'last_name')
        last_name.send_keys(TESTDATA_MULTISTEP['Last_name'])
        button_next = self.driver.find_element(By.XPATH, '//button[text()="Next"]')
        button_next.click()
        email = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, 'email')))
        email.send_keys(TESTDATA_MULTISTEP['Email'])
        phone = self.driver.find_element(By.ID, 'phone')
        phone.send_keys(TESTDATA_MULTISTEP['Phone'])
        button_next = self.driver.find_element(By.XPATH, '//button[text()="Next"]')
        button_next.click()
        dob = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, 'dob')))
        dob.send_keys(TESTDATA_MULTISTEP['Date_of_birth'])
        button_next = self.driver.find_element(By.XPATH, '//button[text()="Next"]')
        button_next.click()
        username = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, 'username')))
        username.send_keys(TESTDATA_MULTISTEP['Username'])
        password = self.driver.find_element(By.ID, 'password')
        password.send_keys(TESTDATA_MULTISTEP['Password'])
        button_submit = self.driver.find_element(By.XPATH, '//button[text()="Submit"]')
        button_submit.click()
        alert = self.driver.switch_to.alert
        assert alert.text == TESTDATA_MULTISTEP['alert']
        alert.accept()
        button_submit = self.driver.find_element(By.XPATH, '//button[text()="Submit"]')
        assert button_submit.is_enabled() # Az alert sikeresen elfogadva.
