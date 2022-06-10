import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from constants.base import BaseConstants
from pages.cart_page import CartPage


class TestCartPage:

    @pytest.fixture(scope="function")
    def cart_page(self):
        driver = WebDriver(executable_path=BaseConstants.DRIVER_PATH)
        driver.implicitly_wait(2)
        driver.get(BaseConstants.BASE_URL)
        yield CartPage(driver)
        driver.close()

    def test_buy_without_registration(self, cart_page):
        """
        - Preconditions:
            - Item added to the cart
        - Steps:
            -

        """
        cart_page.go_to_new_catalog_page()
        cart_page.select_filters()
        cart_page.add_to_cart()
        cart_page.buy_without_registration()
