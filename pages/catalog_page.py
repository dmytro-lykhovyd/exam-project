"""catalog page object"""
from time import sleep

from constants.catalog_page import CatalogPageConstants
from pages.base_page import BasePage
from pages.utils import log_wrapper, wait_until_ok


class CatalogPage(BasePage):
    """methods for catalog paje object"""
    def __init__(self, driver):
        super().__init__(driver)
        self.constants = CatalogPageConstants()

    @log_wrapper
    def go_to_new_catalog_page(self):
        """opens men's catalog page -> opens catalog of new goods"""
        self.accept_all_cookies()
        self.wait_until_clickable(self.constants.START_PAGE_MAN_XPATH).click()
        self.wait_until_clickable(self.constants.MAN_NEW_GENERAL_XPATH).click()

    @log_wrapper
    @wait_until_ok(timeout=5, period=0.5)
    def select_filters(self):
        """selects filters Outdoor from 'category' and 'size' filter and confirms"""
        #  selects new -> category -> outdoor -> confirm
        self.wait_until_clickable(self.constants.MAN_NEW_CATEGORY_XPATH).click()
        self.wait_until_clickable(self.constants.MAN_NEW_CATEGORY_OUTDOOR_XPATH).click()
        assert self.wait_until_clickable(self.constants.MAN_NEW_CATEGORY_OUTDOOR_XPATH).is_enabled(), \
            "Filter is not enabled"
        self.wait_until_clickable(self.constants.OK_BUTTON_XPATH).click()

        #  selects new -> size -> 41 -> confirm
        self.wait_until_clickable(self.constants.MAN_NEW_SIZE_XPATH).click()
        self.wait_until_clickable(self.constants.MAN_NEW_SIZE_41_XPATH).click()
        assert self.wait_until_clickable(self.constants.MAN_NEW_SIZE_41_XPATH).is_enabled(), \
            "Filter is not enabled"
        self.wait_until_clickable(self.constants.OK_BUTTON_XPATH).click()

    @log_wrapper
    def add_to_cart(self):
        """adds selected item to cart"""
        self.wait_until_clickable(self.constants.ITEM_ELEMENT_XPATH).click()
        self.wait_until_displayed(self.constants.POP_UP_MAILING_IMG_XPATH)
        self.wait_until_clickable(self.constants.POP_UP_MAILING_CLOSE_ICON_XPATH).click()
        self.wait_until_clickable(self.constants.CHOOSE_SIZE_DROPDOWN_XPATH).click()
        self.wait_until_clickable(self.constants.CHOOSE_SIZE_XPATH).click()
        self.wait_until_clickable(self.constants.ADD_TO_CART_XPATH).click()
        sleep(1)  # doesn't work without sleep; trying to check cart before item appears in it, return empty cart state.
        self.wait_until_clickable(self.constants.CART_XPATH).click()

    @log_wrapper
    def verify_item_added_to_cart(self):
        """verifies the chosen item successfully added to the cart by """
        assert self.wait_until_clickable(self.constants.BUY_BUTTON_XPATH).is_displayed(), "Item is not in cart"

