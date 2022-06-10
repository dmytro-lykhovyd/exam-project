from time import sleep

from constants.cart_page import CartPageConstants
from pages.base_page import BasePage
from pages.catalog_page import CatalogPage
from pages.utils import User, log_wrapper
from pages import catalog_page


class CartPage(CatalogPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = CartPageConstants()

    def buy_without_registration(self):
        """buy item with unregistered user"""
        self.wait_until_clickable(self.constants.BUY_BUTTON_XPATH).click()
        self.wait_until_clickable(self.constants.BUY_UNREGISTERED_BUTTON_XPATH).click()
        assert self.wait_until_clickable(self.constants.ADDRESS_INPUT_BUTTON_XPATH).is_enabled()

    # TODO: register user during buying
