from constants.catalog_page import CatalogPageConstants


class WishlistPageConstants(CatalogPageConstants):

    ADD_TO_WISHLIST_FROM_CART_XPATH = ".//span[text()='Додати до закладки Мій Вибір']"
    WISHLIST_XPATH = ".//a[@href='/mii-vybir']"
    SORTING_XPATH = ".//span[@class='FavouritesHeader__favoritesSelectLabel__1KWt4 BaseSelectDropdown__selectLabel__3eGHX BaseSelectDropdown__selectPrefix__VNEqY']"
    SORTING_BY_LOWERING_PRICE_XPATH = ".//span[@class='BaseSelectItem__selectItemLabelSelected__1XQwE']"
    SORTING_BY_LOWERING_PRICE_CONFIRMATION_XPATH = ".//span[text()='ціна за спаданням']" #".//span[@class='BaseSelectDropdown__selectContainerHasAFilter__4yFQ9']"
    SELECT_ALL_XPATH = ".//label[@for='check-all-favourites']"
    DELETE_ALL_XPATH = ".//label[text()='Зняти всі відмітки']"
    WISHLIST_IS_EMPTY_TEXT = ".//p[text()='Товари відсутні']"  # for assertion
    ADD_TO_WISHLIST_FROM_CATALOG_XPATH = ".//div[@class='ProductActive__cartConfirmationAddToFavsWrapper__1Wmxe']"
