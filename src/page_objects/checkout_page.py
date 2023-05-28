import logging

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from src.page_objects.base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self, driver: WebDriver, wait_driver: WebDriverWait):
        super(CheckoutPage, self).__init__(driver, wait_driver)

    def get_product_name_checkout(self):
        logging.info(f"Get product name on checkout")
        return self.element("get_product_name_checkout").wait_visible()

    def get_warning_message(self):
        return self.element("warning_message").wait_visible()
