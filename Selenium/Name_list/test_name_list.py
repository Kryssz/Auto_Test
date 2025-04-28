from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://high-flyer.hu/zvkrs47p/feladat3_nevek.html'


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

# Select the name with all uppercase.
    def test_tc1(self):
        namelist = self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//ul[@id="randomNames"]/li')))
        all_caps = [name.text for name in namelist if name.text.isupper()]
        name = all_caps[0].capitalize() # Need to use Name format, for the confirmation message.
        self.wait.until(EC.presence_of_element_located((By.ID, 'allcapsName'))).send_keys(name)
        self.wait.until(EC.presence_of_element_located((By.ID, 'submit'))).click()
        assert self.wait.until(EC.presence_of_element_located((By.ID, 'result'))).text == 'Eltaláltad.'



