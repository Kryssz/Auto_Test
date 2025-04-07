from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://high-flyer.hu/hetihazi/feladat3_penzfeldobas.html'


class TestFlipCoin(object):
    def setup_method(self):
        options = Options()
        options.add_argument('--disable-search-engine-choice-screen')
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.get(URL)

    def teardown_method(self):
        self.driver.quit()

    def test_hundred_flips(self):
        head = 0
        tail = 0
        for i in range(100):
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'submit'))).click()
            result = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'lastResult')))
            if result.text == 'fej':
                head += 1
            else:
                tail += 1
        assert head >= 30 # The test has passed only, if we got heads at least 30 times from 100 flips.