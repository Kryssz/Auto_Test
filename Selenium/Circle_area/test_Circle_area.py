from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://high-flyer.hu/zvkrs47p/feladat1_kor.html'


class TestCircleArea(object):
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
# Happy path.
    def test_happy_path(self):
        self.wait.until(EC.visibility_of_element_located((By.ID, 'r'))).send_keys('10')
        self.wait.until(EC.visibility_of_element_located((By.ID, 'submit'))).click()
        result = self.wait.until((EC.presence_of_element_located((By.ID, 'result'))))
        assert result.text == '314'

# Unhappy path with text.
    def test_text(self):
        self.wait.until(EC.visibility_of_element_located((By.ID, 'r'))).send_keys('kiscica')
        self.wait.until(EC.visibility_of_element_located((By.ID, 'submit'))).click()
        result = self.wait.until((EC.presence_of_element_located((By.ID, 'result'))))
        assert result.text == 'NaN'

# Unhappy path with empty field.
    def test_empty_field(self):
        self.wait.until(EC.visibility_of_element_located((By.ID, 'submit'))).click()
        result = self.wait.until((EC.presence_of_element_located((By.ID, 'result'))))
        assert result.text == 'NaN'