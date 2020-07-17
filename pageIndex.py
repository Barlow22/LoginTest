from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class PageIndex:

    def __init__(self, driver):
        self.driver = driver
        self.login_button = (By.CLASS_NAME, 'login')

    def sign_in(self):
        try:
            element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.login_button))
            element.click()
        except: 
            print('No se encuentra el elemento.')