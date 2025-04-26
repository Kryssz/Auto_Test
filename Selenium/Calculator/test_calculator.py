from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL = 'https://high-flyer.hu/zvkrs47p/feladat2_calculator.html'


class TestTC(object):
    def setup_method(self):
        options = Options()
        options.add_argument('--disable-search-engine-choice-screen')
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.get(URL)
        self.wait = WebDriverWait(self.driver, 5)

    def teardown_method(self):
        self.driver.quit()

    # Testing the operation of the calculator.
    def test_result_check(self):
        num1 = self.wait.until(EC.presence_of_element_located((By.ID, 'num1'))).text
        num2 = self.wait.until(EC.presence_of_element_located((By.ID, 'num2'))).text
        op1 = self.wait.until(EC.presence_of_element_located((By.ID, 'op1'))).text
        result = 0
        if op1 == '+':
            result = int(num1) + int(num2)
        elif op1 == '-':
            result = int(num1) - int(num2)
        elif op1 == '*':
            result = int(num1) * int(num2)
        elif op1 == '/':
            result = int(num1) / int(num2)

        self.wait.until(EC.element_to_be_clickable((By.ID, 'submit'))).click()
        webresult = self.wait.until(EC.presence_of_element_located((By.ID, 'result')))
        assert webresult.text == f'{result}'  # Comparison of the two final results.
