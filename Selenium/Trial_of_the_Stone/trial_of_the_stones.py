from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

URL = 'https://techstepacademy.com/trial-of-the-stones'


class TestTC(object):
    def setup_method(self):
        options = Options()
        options.add_argument('--disable-search-engine-choice-screen')
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.get(URL)

    def teardown_method(self):
        self.driver.quit()

    def test_trial(self):
        #Solving the first riddle, with the "rock" string.
        stone = self.driver.find_element(By.XPATH, '//input[@id="r1Input"]')
        stone.send_keys('rock')
        answer1 = self.driver.find_element(By.XPATH, '//button[@id="r1Btn"]')
        answer1.click()

        #Solving the second riddle, use the revealed password on the site.
        secrets = self.driver.find_element(By.XPATH, '//input[@id="r2Input"]')
        key1 = self.driver.find_element(By.XPATH, '//div[@id="passwordBanner"]/h4')
        secrets.send_keys(key1.text)
        answer2 = self.driver.find_element(By.XPATH, '//button[@id="r2Butn"]')
        answer2.click()
        #Assert to solve the first and the second riddle.
        success1 = self.driver.find_element(By.ID, 'successBanner1')
        assert success1.text == 'Success!'

        #Compare the 2 merchant wealth, and use the name of the wealthiest merchant in the text field.
        merchant_blocks = self.driver.find_elements(By.XPATH, '//div[span/b]')
        merchant_data = []
        for block in merchant_blocks:
            name = block.find_element(By.TAG_NAME, 'b').text.strip()
            wealth = int(block.find_element(By.TAG_NAME, 'p').text.strip())
            merchant_data.append((name, wealth))

        richest = max(merchant_data, key=lambda x: x[1])
        name, wealth = richest

        riddle_input = self.driver.find_element(By.ID, 'r3Input')
        riddle_input.send_keys(name)

        #Assert to solv the third riddle.
        self.driver.find_element(By.ID, 'r3Butn').click()
        success2 = self.driver.find_element(By.ID, 'successBanner2')
        assert success2.is_displayed()

        #Assert to solve all of the riddles.
        self.driver.find_element(By.ID, 'checkButn').click()
        success_banner = self.driver.find_element(By.ID, 'trialCompleteBanner')
        assert success_banner.is_displayed()


