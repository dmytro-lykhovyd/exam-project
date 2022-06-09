from time import sleep

from selenium.webdriver.common.by import By

from constants.catalog_page import CatalogPageConstants
from constants.profile_page import ProfilePageConstants
from pages.base_page import BasePage
from pages.utils import User, log_wrapper


class CatalogPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = CatalogPageConstants()

    @log_wrapper
    def go_to_shoe_catalog_page(self):
        """opens men's catalog page and opens catalog of new goods"""
        self.accept_all_cookies()
        self.wait_until_clickable(locator=self.constants.START_PAGE_MAN_XPATH).click()
        self.wait_until_clickable(locator=self.constants.MAN_NEW_GENERAL_XPATH).click()
        return CatalogPage

    @log_wrapper
    def select_filters(self):
        """select two filters from category and confirms"""
        new = self.wait_until_clickable(locator=self.constants.MAN_NEW_CATEGORY_XPATH)
        new.click()
        self.wait_until_clickable(locator=self.constants.MAN_NEW_CATEGORY_OUTDOOR_XPATH).click()
        sleep(3)
        assert self.wait_until_clickable(locator=self.constants.MAN_NEW_CATEGORY_OUTDOOR_XPATH).is_enabled()

        #self.wait_until_clickable(locator=self.constants.OK_BUTTON_XPATH).click()
        # check = self.wait_until_clickable(locator=self.constants.DENY_FILTERS_XPATH)
        # sleep(3)
        # assert check.is_displayed()
