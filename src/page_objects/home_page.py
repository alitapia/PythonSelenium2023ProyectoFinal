import logging

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from src.page_objects.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver: WebDriver, wait_driver: WebDriverWait):
        super(HomePage, self).__init__(driver, wait_driver)

    def search(self, value: str):
        logging.info(f"Search {value}")
        self.element("search_input").wait_clickable().send_keys(value)
        self.element("search_btn").wait_clickable().click()

    def get_top_menu_options(self) -> list[str]:
        logging.info("Get home top menu options")
        self.element("top_menu_options").wait_visible()
        return [element.text for element in self.element("top_menu_options").find_elements()]
