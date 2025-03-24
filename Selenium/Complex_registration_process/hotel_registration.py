import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URLS = {
    'tempmail_url' : "https://mediapyro.com/mailbox",
    'hotel_v3_url' : "http://hotel-v3.progmasters.hu/",
    'reglink_url' : None
}

TESTDATA = {
    'Vezetéknév' : 'Kryssz',
    'Utónév' : 'Auto_test',
    'Cím' : 'Selenium, pytest u 3',
    'E-mail' : None,
    'Jelszó' : 'Auto_test',
}

class TestHotelRegistration(object):
    def setup_method(self):
        options = Options()
        options.add_argument('--disable-search-engine-choice-screen')
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

        # Main Test case.
    def test_temp_email(self):
        self.driver.get(URLS['tempmail_url'])
        e_mail_window = self.driver.window_handles[0]
        random_btn = self.driver.find_element(By.ID, 'random')
        random_btn.click()
        temp_email = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, 'email_id'))).text # Get the random generated temporary e-mail address.
        TESTDATA['E-mail'] = f'{temp_email}' # Push the temporary e-mail address as the value of the 'E-mail' key in TESTDATA dictionary.
        self.driver.switch_to.new_window() # Open a new tab in Chrome webdriver.
        self.do_hotel_v3_registration() # Start the 'hotel_v3_registration' steppes.
        self.driver.switch_to.window(e_mail_window) # Switch back to the e-mail tab, after the registration process done.
        WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, '//div[text()="hotel.team.five@gmail.com"]'))).click() # Wait, until the confirmation e-mail arrives.
        reg_link = self.driver.find_element(By.XPATH, '//iframe[@class="w-full flex flex-grow px-5"]')
        confirmation_message = reg_link.get_attribute('srcdoc')
        confirmation_link = confirmation_message.split('linkre: ')[1].split() # Get the confirmation link out from the e-mail text.
        URLS['reglink_url'] = f'{confirmation_link[0]}' # Push the confirmation link as the value of the 'reglink_url' key is URLS dictionary.
        self.driver.switch_to.new_window()
        registration_confirmation_window = self.driver.window_handles[2]
        self.driver.switch_to.window(registration_confirmation_window)
        time.sleep(.1)
        self.do_hotel_registration_confirmation() #Start the 'hotel_registration_confirmation' steppes.

        # The registration steppes.
    def do_hotel_v3_registration(self):
        self.driver.get(URLS['hotel_v3_url'])
        registration = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//div//a[@class="nav-link dropdown-toggle"]')))
        registration.click()
        user_reg = self.driver.find_element(By.XPATH, '//div/a[text()="Vendég"]')
        user_reg.click()
        time.sleep(.1) # Need to slow down the code, so that all data is in the right place.
        firstname_field = self.driver.find_element(By.ID, 'firstname')
        firstname_field.send_keys(TESTDATA['Vezetéknév'])
        time.sleep(.1)
        lastname_field = self.driver.find_element(By.ID, 'lastname')
        lastname_field.send_keys(TESTDATA['Utónév'])
        time.sleep(.1)
        address_field = self.driver.find_element(By.ID, 'address')
        address_field.send_keys(TESTDATA['Cím'])
        time.sleep(.1)
        email_filed = self.driver.find_element(By.ID, 'email')
        email_filed.send_keys(TESTDATA['E-mail'])
        time.sleep(.1)
        password_field = self.driver.find_element(By.ID, 'password')
        password_field.send_keys(TESTDATA['Jelszó'])
        time.sleep(.1)
        save_button = self.driver.find_element(By.XPATH, '//button[@class="btn btn-success ng-star-inserted"]')
        save_button.click()

        # The registration confirmation steppes.
    def do_hotel_registration_confirmation(self):
        self.driver.get(URLS['reglink_url']) # Use the confirmation link from the e-mail.
        email_field = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'email')))
        email_field.send_keys(TESTDATA['E-mail']) # Use the random generated e-mail from the website.
        password_field = self.driver.find_element(By.ID, 'password')
        password_field.send_keys(TESTDATA['Jelszó'])
        enter_btn = self.driver.find_element(By.XPATH, '//button[@class="btn btn-success "]')
        enter_btn.click()
        registration_success_txt = self.driver.find_element(By.XPATH, '//p/strong')
        assert registration_success_txt.text == 'Sikeres regisztráció! Kérjük jelentkezz be!' # Checking if the confirmation link worked correctly.
        profile_btn = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'profile')))
        profile_btn.click()
        WebDriverWait(self.driver, 5).until(EC.text_to_be_present_in_element_attribute((By.XPATH, '//form/div/input'), 'placeholder', f'{TESTDATA['E-mail']}')) # Need to wait to load all the attributes, before start to checking them.
        data_form = self.driver.find_elements(By.XPATH, '//form/div/input[@placeholder]')
        profile_email_field = data_form[0].get_attribute('placeholder')
        profile_firstname_field = data_form[1].get_attribute('placeholder')
        profile_second_name_field = data_form[2].get_attribute('placeholder')
        profile_address_field = data_form[3].get_attribute('placeholder')
        assert profile_email_field == TESTDATA['E-mail']
        assert profile_firstname_field == TESTDATA['Vezetéknév']
        assert profile_second_name_field == TESTDATA['Utónév']
        assert profile_address_field == f' {TESTDATA['Cím']}'






