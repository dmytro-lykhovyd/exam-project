import logging

import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from constants.base import BaseConstants
from pages.catalog_page import CatalogPage


class TestCatalogPage:
    log = logging.getLogger('[CatalogPage]')

    @pytest.fixture(scope="function")
    def catalog_page(self):
        driver = WebDriver(executable_path=BaseConstants.DRIVER_PATH)
        driver.implicitly_wait(3)
        driver.get(BaseConstants.BASE_URL)
        yield CatalogPage(driver)
        driver.close()

    def test_add_item_to_cart(self, catalog_page):  # unstable test due to bad locators?
        """
        - Preconditions:
            - Create driver
            - Open start page
        - Steps:
            - Click on Man's catalog section
            - Click on New goods section
            - Click on Category section -> Outdoor in Category -> confirm
            - Click on Size section -> 41 in Size -> confirm
            - Add first item from the list of results to cart
            - Verify item is in the cart
        """

        catalog_page.go_to_new_catalog_page()
        catalog_page.select_filters()
        catalog_page.verify_filters_setting()
        catalog_page.add_to_cart()
        catalog_page.verify_item_added_to_cart()



