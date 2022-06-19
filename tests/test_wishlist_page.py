import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from constants.base import BaseConstants
from pages.wishlist_page import WishlistPage


class TestWishlistPage:

    @pytest.fixture(scope="function")
    def wishlist_page(self):
        driver = WebDriver(executable_path=BaseConstants.DRIVER_PATH)
        driver.implicitly_wait(2)
        driver.get(BaseConstants.BASE_URL)
        yield WishlistPage(driver)
        driver.close()

    def test_add_items_to_wishlist(self, wishlist_page):
        """
        - Preconditions:
            - Item is already added to cart
            - User is in the cart
        - Steps:
            - Click on 'Add to wishlist' icon
            - Go to wishlist
            - Verify item is in the wishlist (assert BUY_BUTTON_XPATH is displayed)
            - Go to the Shoes catalog section
            - Select another item -> select size -> add it to the wishlist
            - Go to the wishlist
            - Sort wishlist by lowering price
            - verify sorting is by lowering price
            - select all items in wishlist
            - delete all from wishlist
            - verify wishlist is empty
        """

        # adding item to cart
        wishlist_page.go_to_new_catalog_page()
        wishlist_page.select_filters()
        wishlist_page.add_to_cart()

        # adding item to the wishlist from cart
        wishlist_page.add_item_to_wishlist_from_cart()

        # adding item to the wishlist from catalog
        wishlist_page.add_item_to_wishlist_from_catalog()

        # verify wishlist functions
        wishlist_page.verify_wishlist_functions()



