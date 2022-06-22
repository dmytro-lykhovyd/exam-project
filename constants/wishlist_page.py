"""constants for wishlist page"""
from constants.catalog_page import CatalogPageConstants


class WishlistPageConstants(CatalogPageConstants):
    """wishlist page features constants"""
    ADD_TO_WISHLIST_FROM_CART_XPATH = ".//span[text()='Додати до закладки Мій Вибір']"
    WISHLIST_XPATH = ".//a[@href='/mii-vybir']"
    SORTING_XPATH = ".//span[text()='найновіше']"
    SORTING_BY_LOWERING_PRICE_XPATH = ".//span[text()='ціна за спаданням']"
    SORTING_BY_LOWERING_PRICE_CONFIRMATION_XPATH = ".//span[text()='ціна за спаданням']"
    SELECT_ALL_XPATH = ".//div[@class='flex-block xs-flex-block--left']"
    DELETE_ALL_XPATH = ".//div[text()='Усунути зазначене']"
    WISHLIST_IS_EMPTY_TEXT = ".//p[text()='Товари відсутні']"  # for assertion
    ADD_TO_WISHLIST_FROM_CATALOG_XPATH = ".//div[@class='ProductActive__cartConfirmationAddToFavsWrapper__1Wmxe']"
