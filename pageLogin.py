from selenium.webdriver.common.by import By

class PageLogin:


    def __init__(self, driver):
        self.driver = driver
        self.email_box = (By.ID, 'email')
        self.passwd_box = (By.ID, 'passwd')
        self.submit_login = (By.ID, 'SubmitLogin')
        

    def email_login(self, mail):
        self.driver.find_element(*self.email_box).send_keys(mail)

    def passwd_login(self, passwd):
        self.driver.find_element(*self.passwd_box).send_keys(passwd)

    def button_login(self):
        self.driver.find_element(*self.submit_login).click()