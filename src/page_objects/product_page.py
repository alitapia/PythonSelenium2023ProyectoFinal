import logging

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from src.page_objects.base_page import BasePage


class ProductPage(BasePage):
    def __init__(self, driver: WebDriver, wait_driver: WebDriverWait):
        super(ProductPage, self).__init__(driver, wait_driver)


    def get_product_name(self):
        self.element("product_title").wait_visible()
        return self.element("product_title").wait_visible()
    def get_price(self):
        logging.info(f"Get price from product ")
        self.element("currency_menu").wait_clickable().click()
        self.element("dollar_option").wait_clickable().click()
        self.element("product_title").wait_clickable().click()
        return self.element("product_price").wait_visible().text





