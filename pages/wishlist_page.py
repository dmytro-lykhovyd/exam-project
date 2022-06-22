import logging
from time import sleep

from constants.wishlist_page import WishlistPageConstants
from pages.catalog_page import CatalogPage
from pages.utils import log_wrapper, wait_until_ok


class WishlistPage(CatalogPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.log = logging.getLogger("[WishList]")
        self.constants = WishlistPageConstants()

    @log_wrapper
    def add_item_to_wishlist_from_cart(self):
        """moves item from cart to wishlist and check it"""
        self.wait_until_clickable(self.constants.ADD_TO_WISHLIST_FROM_CART_XPATH).click()
        self.wait_until_clickable(self.constants.WISHLIST_XPATH).click()

    @log_wrapper
    @wait_until_ok(timeout=5, period=0.5)
    def add_item_to_wishlist_from_catalog(self):
        """goes to catalog page, choose one item and place it to wishlist"""
        self.wait_until_clickable(self.constants.MAN_SHOES_XPATH).click()
        self.wait_until_clickable(self.constants.ITEM_ELEMENT_2_XPATH).click()
        self.wait_until_clickable(self.constants.CHOOSE_SIZE_DROPDOWN_XPATH).click()
        self.wait_until_clickable(self.constants.CHOOSE_SIZE_XPATH).click()
        self.wait_until_clickable(self.constants.ADD_TO_WISHLIST_FROM_CATALOG_XPATH).click()

    @log_wrapper
    @wait_until_ok(timeout=5, period=0.5)
    def verify_wishlist_functions(self):
        """verifies that items can be sorted and deleted from wishlist"""
        # go to wishlist
        self.wait_until_clickable(self.constants.WISHLIST_XPATH).click()
        self.wait_until_clickable(self.constants.SORTING_XPATH).click()
        self.wait_until_clickable(self.constants.SORTING_BY_LOWERING_PRICE_XPATH).click()
        assert self.wait_until_clickable(self.constants.SORTING_BY_LOWERING_PRICE_CONFIRMATION_XPATH).is_displayed(), \
            "sorting isn't set properly"
        self.wait_until_clickable(self.constants.SELECT_ALL_XPATH).click()
        self.wait_until_clickable(self.constants.DELETE_ALL_XPATH).click()
        assert self.wait_until_clickable(self.constants.WISHLIST_IS_EMPTY_TEXT).is_displayed(), "wishlist isn't cleared"
