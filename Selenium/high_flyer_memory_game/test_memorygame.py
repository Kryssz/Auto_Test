from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from collections import defaultdict

URL = 'https://high-flyer.hu/selenium/memory-game.html'


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

    def test_game_pass(self):
        cards = self.driver.find_elements(By.XPATH, "//div[@class='card']")
        card_dict = defaultdict(list)
        for card in cards:
            data_id = card.get_attribute("data-id")
            card_dict[data_id].append(card)

        for data_id, card_list in card_dict.items():
            if len(card_list) == 2:
                self.driver.execute_script("arguments[0].scrollIntoView(true);", card_list[0])
                card_list[0].click()

                self.driver.execute_script("arguments[0].scrollIntoView(true);", card_list[1])
                card_list[1].click()

        winner_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "winner")))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", winner_element)
        assert "You Rock!" in winner_element.text