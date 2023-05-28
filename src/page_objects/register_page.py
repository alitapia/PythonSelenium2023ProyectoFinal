import logging

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from src.page_objects.base_page import BasePage


class RegisterPage(BasePage):
    def __init__(self, driver: WebDriver, wait_driver: WebDriverWait):
        super(RegisterPage, self).__init__(driver, wait_driver)

    def register_user(self, name: str, lastname: str, email: str, telephone: str, password: str):
        logging.info(f"Register new user with name:{name} lastname:{lastname} email: {email} telephone:{telephone} password: {password}")
        self.element("name_input").wait_clickable().send_keys(name)
        self.element("lastname_input").wait_clickable().send_keys(lastname)
        self.element("email_input").wait_clickable().send_keys(email)
        self.element("telephone_input").wait_clickable().send_keys(telephone)
        self.element("password_input").wait_clickable().send_keys(password)
        self.element("password_confirm_input").wait_clickable().send_keys(password)
        self.element("privacy_policy_input").wait_clickable().click()
        self.element("continue_btn").wait_clickable().click()

    def get_success_message(self):
        return self.element("success_message").wait_visible().text
