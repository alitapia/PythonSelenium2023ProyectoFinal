import logging

import logging

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from src.page_objects.base_page import BasePage


class SearchPage(BasePage):
    def __init__(self, driver: WebDriver, wait_driver: WebDriverWait):
        super(SearchPage, self).__init__(driver, wait_driver)

    def get_product_name(self):
        logging.info(f"Get product name")
        return self.element("product_title").wait_visible()

    def add_to_cart(self):
        logging.info("Add to cart product")
        self.element("add_cart_button").wait_clickable().click()

    def go_to_checkout(self):
        logging.info("Go to checkout from search page")
        self.element("checkout_button").wait_clickable().click()
