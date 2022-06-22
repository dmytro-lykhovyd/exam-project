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

    def test_buy_non_registered(self, cart_page):
        """
        - Preconditions:
            - Item added to the cart
        - Steps:
            - Click on Buy button
            - Choose 'buying without registration'
            - Choose delivery company and go to the Payment
            - Fill all oblige fields
            - Go to the payment page
            - Fill Purchase Note field
            - Fill Password field to registrate new user during payment process (optional feature)
            - Verify Order/Buy button is enabled
        """
        # adding item to cart
        cart_page.go_to_new_catalog_page()
        cart_page.select_filters()
        cart_page.add_to_cart()

        # purchasing process
        cart_page.buy_without_registration()
        cart_page.choose_delivery_company()
        cart_page.input_delivery_info()
        cart_page.payment()

        cart_page.verify_payment_is_staged()

