from TESTDATA import TESTDATA_UNHAPPY
from TESTDATA import TESTDATA
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://high-flyer.hu/selenium/simplevalidation.html'


class TestMegaTestForm(object):
    def setup_method(self):
        options = Options()
        options.add_argument('--disable-search-engine-choice-screen')
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.get(URL)

    def teardown_method(self):
        self.driver.quit()

    def test_form_validation_happy_path(self):
        test_email = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'test-email')))
        test_email.send_keys(TESTDATA['E-Mail'])
        test_password = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'test-password')))
        test_password.send_keys(TESTDATA['Password'])
        confirm_password = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'test-confirm-password')))
        confirm_password.send_keys(TESTDATA['Confirm'])
        customer_number = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'test-customer-number')))
        customer_number.send_keys(TESTDATA['Customer_number'])
        dealer_number = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'test-dealer-number')))
        dealer_number.send_keys(TESTDATA['Dealer_number'])
        date_field = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'test-date-field')))
        date_field.send_keys(TESTDATA['Date'])
        random_textarea = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'test-random-textarea')))
        random_textarea.send_keys(TESTDATA['Random_text'])
        card_type = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'test-card-type')))
        card_type.click()
        self.driver.find_element(By.XPATH, '//select/option[@value="VI"]').click()
        card_number = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'test-card-number')))
        card_number.send_keys(TESTDATA['Card_number'])
        card_cvv = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'test-card-cvv')))
        card_cvv.send_keys(TESTDATA['CVV'])
        card_month = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'test-card-month')))
        card_month.click()
        self.driver.find_element(By.XPATH, '//select/option[@value="2"]').click()
        card_year = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'test-card-year')))
        card_year.click()
        self.driver.find_element(By.XPATH, '//select/option[@value="2027"]').click()
        single_checkbox = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'test-single-checkbox')))
        single_checkbox.click()
        save_email_yes = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'test-save-email-yes')))
        save_email_yes.click()
        terms_service = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'test-terms-service')))
        terms_service.click()
        terms_service_more = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'test-terms-service-more')))
        terms_service_more.click()
        is_valid = self.driver.find_elements(By.CSS_SELECTOR, '[data-jsv-field-isvalid]')
        assert len(is_valid) == 17


    def test_form_validation_unhappy_path(self):
        test_email = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'test-email')))
        test_email.send_keys(TESTDATA_UNHAPPY['E-Mail'])
        test_password = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'test-password')))
        test_password.send_keys(TESTDATA_UNHAPPY['Password'])
        confirm_password = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'test-confirm-password')))
        confirm_password.send_keys(TESTDATA_UNHAPPY['Confirm'])
        customer_number = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'test-customer-number')))
        customer_number.send_keys(TESTDATA_UNHAPPY['Customer_number'])
        dealer_number = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'test-dealer-number')))
        dealer_number.send_keys(TESTDATA_UNHAPPY['Dealer_number'])
        date_field = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'test-date-field')))
        date_field.send_keys(TESTDATA_UNHAPPY['Date'])
        random_textarea = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'test-random-textarea')))
        random_textarea.send_keys(TESTDATA_UNHAPPY['Random_text'])
        card_type = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'test-card-type')))
        card_type.click()
        self.driver.find_element(By.XPATH, '//select/option[text()="Select Card Type"]').click()
        card_number = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'test-card-number')))
        card_number.send_keys(TESTDATA_UNHAPPY['Card_number'])
        card_cvv = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'test-card-cvv')))
        card_cvv.send_keys(TESTDATA_UNHAPPY['CVV'])
        card_month = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'test-card-month')))
        card_month.click()
        self.driver.find_element(By.XPATH, '//select/option[text()="Select Month"]').click()
        card_year = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'test-card-year')))
        card_year.click()
        self.driver.find_element(By.XPATH, '//select/option[text()="Select Year"]').click()
        single_checkbox = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'test-single-checkbox')))
        single_checkbox.click()
        single_checkbox.click()
        terms_service = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'test-terms-service')))
        terms_service.click()
        terms_service.click()
        terms_service_more = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'test-terms-service-more')))
        terms_service_more.click()
        terms_service_more.click()
        is_valid = self.driver.find_elements(By.CSS_SELECTOR, '[data-jsv-field-isvalid]')
        assert len(is_valid) == 2 # Break, because CVV box accept letters too.