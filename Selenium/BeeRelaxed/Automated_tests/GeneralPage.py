from Selenium.BeeRelaxed.Automated_tests.generate_browers import generate_chrome_driver

class GeneralPage(object):
    def __init__(self, url, driver=None):
        self.url = url
        if driver is None:
            self.driver = generate_chrome_driver()
        else:
            self.driver = driver

    def get(self):
        self.driver.get(self.url)

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()

    def refresh(self):
        self.driver.refresh()

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url