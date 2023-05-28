import logging

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from src.page_objects.base_page import BasePage


class ForgotPasswordPage(BasePage):
    def __init__(self, driver: WebDriver, wait_driver: WebDriverWait):
        super(ForgotPasswordPage, self).__init__(driver, wait_driver)

    def recover_password(self, email: str):
        logging.info(f"Recover password for {email} ")
        self.element("email_input").wait_clickable().send_keys(email)
        self.element("continue_btn").wait_clickable().click()

    def get_warning_message(self):
        return self.element("warning_message").wait_visible().text
