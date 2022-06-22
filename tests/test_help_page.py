import logging

import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from constants.base import BaseConstants
from pages.help_page import HelpPage


class TestHelpPage:
    log = logging.getLogger('[HelpPage]')

    @pytest.fixture(scope="function")
    def help_page(self):
        driver = WebDriver(executable_path=BaseConstants.DRIVER_PATH)
        driver.implicitly_wait(3)
        driver.get(BaseConstants.BASE_URL)
        yield HelpPage(driver)
        driver.close()

    def test_help_center(self, help_page):

        """
        - Preconditions:
            - Create driver
            - Open start page
        - Steps:
            - Click on a FAQ menu in a site footer
            - Go to Promocodes questions
            - Verify information
            - Go to Order questions
            - Verifies text in order question section is visible
        """
        help_page.open_promocode_page()
        help_page.open_order_page()

