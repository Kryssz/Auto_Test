from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

URL = 'http://localhost:4200/register'


class TestTC(object):
    def setup_method(self):
        options = Options()
        options.add_argument('--disable-search-engine-choice-screen')
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        # self.driver.maximize_window()
        self.driver.get(URL)
        self.wait = WebDriverWait(self.driver, 5)

    def teardown_method(self):
        pass #self.driver.quit()

    def test_tc1(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//button/a[text()="Register"]'))).click()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//select/option[@value="ROLE_BEEFAMILY"]'))).click()