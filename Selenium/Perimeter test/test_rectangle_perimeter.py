from TESTDATA import TESTDATA_RECTANGLE_HAPPY, TESTDATA_RECTANGLE_UNHAPPY_LETTER, TESTDATA_RECTANGLE_UNHAPPY_EMPTY
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://high-flyer.hu/hetihazi/feladat1_teglalap.html'


class TestRectanglePerimeter(object):
    def setup_method(self):
        options = Options()
        options.add_argument('--disable-search-engine-choice-screen')
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.get(URL)

    def teardown_method(self):
        self.driver.quit()

    def test_rectangle_happy_path(self):
        a = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, 'a')))
        a.send_keys(TESTDATA_RECTANGLE_HAPPY['a'])
        b = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, 'b')))
        b.send_keys(TESTDATA_RECTANGLE_HAPPY['b'])
        button_submit = self.driver.find_element(By.ID, 'submit')
        button_submit.click()
        result = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, 'result')))
        assert result.text == TESTDATA_RECTANGLE_HAPPY['result']

    def test_rectangle_unhappy_path_letter(self):
        a = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, 'a')))
        a.send_keys(TESTDATA_RECTANGLE_UNHAPPY_LETTER['a'])
        b = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, 'b')))
        b.send_keys(TESTDATA_RECTANGLE_UNHAPPY_LETTER['b'])
        button_submit = self.driver.find_element(By.ID, 'submit')
        button_submit.click()
        result = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, 'result')))
        assert result.text == TESTDATA_RECTANGLE_UNHAPPY_LETTER['result']

    def test_rectangle_unhappy_path_empty(self):
        a = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, 'a')))
        a.send_keys(TESTDATA_RECTANGLE_UNHAPPY_EMPTY['a'])
        b = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, 'b')))
        b.send_keys(TESTDATA_RECTANGLE_UNHAPPY_EMPTY['b'])
        button_submit = self.driver.find_element(By.ID, 'submit')
        button_submit.click()
        result = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, 'result')))
        assert result.text == TESTDATA_RECTANGLE_UNHAPPY_EMPTY['result']