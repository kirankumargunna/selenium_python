from selenium.webdriver.common.by import By
from pages.basepage import base_page

class LoginPage(base_page):
    username_field = (By.ID, "username")
    password_field = (By.ID, "password")
    login_button = (By.ID, "submit")

    def login(self, username, password):
        self.driver.find_element(*self.username_field).click()
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).click()
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()
