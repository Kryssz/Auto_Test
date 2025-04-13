from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def generate_chrome_driver():
    options = Options()
    options.add_argument('--disable-search-engine-choice-screen')
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    return driver