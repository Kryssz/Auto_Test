import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument('--disable-search-engine-choice-screen')
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()

URL = 'http://hotel-v3.progmasters.hu/'
driver.get(URL)

hotels_list = driver.find_element(By.XPATH, '//button[text()=" Megnézem a teljes listát "]')
hotels_list.click()
wait = WebDriverWait(driver, 10)
checkboxes = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='form-group']//input[@type='checkbox']")))

for checkbox in checkboxes:
    if not checkbox.is_selected():
        checkbox.click()

if len(checkboxes) == 10:
    print('All of the checkboxes are checked.')
else:
    print('One or more checkbox is not selected.')
    raise AssertionError('Checkbox error')

filter_reset = driver.find_element(By.XPATH, '//span[@id="redstar"]')
filter_reset.click()
time.sleep(1)

all_selected = all(checkbox.is_selected() for checkbox in checkboxes)

if all_selected:
    print('The filter reset is not working properly.')
    raise AssertionError('Filter reset error')
else:
    print('The filter reset is working properly.')

rss_hotel = driver.find_element(By.XPATH, '//div/h4[text()="Rainbow Six Siege - Hotel - nyaraló"]')
rss_hotel.click()
rss_hotel_desc = driver.find_element(By.XPATH, '//p[@class="card-text"][2]')
long_desc = rss_hotel_desc.text
print(long_desc)
if len(long_desc) > 500:
    print('The description is longer than 500 character.')
else:
    print('The description is shorter than 500 character.')

login = driver.find_element(By.XPATH, '//li/a[@class="nav-link"]')
login.click()

email = driver.find_element(By.XPATH, '//input[@id="email"]')
email.send_keys('fse23850@jioso.com')
password = driver.find_element(By.XPATH, '//input[@id="password"]')
password.send_keys('AutoTest')

login_btn = driver.find_element(By.XPATH, '//button[text()="Belépés "]')
login_btn.click()

try:

    logout = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//a[text()="Kilépés"]'))
    )
    print('The log in was successful.')
except:
    print('Somethings went wrong during the log in.')
    raise AssertionError('Log in error')

driver.quit()