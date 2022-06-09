import logging
from time import sleep
import conftest

import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from constants.base import BaseConstants
from pages.base_page import BasePage
from pages.catalog_page import CatalogPage
from pages.utils import User, log_wrapper
import conftest


class TestCatalogPage:
    log = logging.getLogger('[CatalogPage]')

    @pytest.fixture(scope="function")
    def catalog_page(self):
        driver = WebDriver(executable_path=BaseConstants.DRIVER_PATH)
        driver.implicitly_wait(2)
        driver.get(BaseConstants.BASE_URL)
        yield CatalogPage(driver)
        driver.close()

    # @pytest.fixture(scope="function")
    # def accept_cookies(self):
    #     """accepts all cookies"""
    #     self.wait_until_clickable(locator=self.constants.ACCEPT_ALL_COOKIES_XPATH).click()
    #     assert not self.is_element_exists(locator=self.constants.ACCEPT_ALL_COOKIES_XPATH)

    def test_add_man_shoes_to_cart(self, catalog_page):
        """
        - Preconditions:
            - Create driver
            - Open start page
        - Steps:
            - Click on Man's catalog section
            - Click on Shues section
            - Click on
            - Fill Firstname field
            - Fill Surname field
            - Fill Phone field
            - Fill Email field
            - Fill Password field
            - Fill Repeat password field
            - Press 'Create account' button
            - Verify successful registration
        """

        catalog_page.go_to_shoe_catalog_page()
        catalog_page.select_filters()

