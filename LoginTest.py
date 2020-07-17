import unittest
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from pageIndex import PageIndex
from pageLogin import PageLogin


class LoginCases(unittest.TestCase):

    def setUp(self):
        option = Options()
        option.add_argument('start-maximized')
        self.driver =  webdriver.Chrome('chromedriver.exe', options=option)
        self.driver.get('http://automationpractice.com/index.php')
        self.driver.implicitly_wait(5)
        self.index_page = PageIndex(self.driver)
        self.login_page = PageLogin(self.driver)

    def test_invalid_mail(self):
        self.index_page.sign_in()
        self.login_page.email_login('PepeElMasCapo')
        self.login_page.passwd_login('123456')
        self.login_page.button_login()
        time.sleep(5)



if __name__ == "__main__":
    unittest.main()