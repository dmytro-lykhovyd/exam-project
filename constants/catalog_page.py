"""constants for catalog page"""
from constants.base import BaseConstants


class CatalogPageConstants(BaseConstants):
    """constants for searching and adding item to a cart process"""
    # man's new
    START_PAGE_MAN_XPATH = ".//a[@href='/c/vin']"
    MAN_SHOES_XPATH = ".//a[@href='/k/vin/vzuttya']"
    MAN_SHOES_OUTDOOR_XPATH = "//*[@id='root]/div[3]/div/div/div[2]/div/div[2]/ul/li[3]/div/div/div"
    MAN_NEW_GENERAL_XPATH = ".//a[@href='/new/vin']"
    MAN_NEW_CATEGORY_XPATH = ".//span[text()='Категорія']"
    MAN_NEW_CATEGORY_OUTDOOR_XPATH = ".//span[text()='Outdoor']"
    MAN_NEW_SIZE_XPATH = ".//span[text()='Розмір']"
    MAN_NEW_SIZE_41_XPATH = ".//span[text()='41']"
    OK_BUTTON_XPATH = ".//button[@class='btn col-xs-12 col-md-6 col-md-offset-3 col-lg-12 col-lg-offset-0  btn--fluid btn--filtersSubmit btn--spaced-bottom']"
    DENY_FILTERS_XPATH = ".//span[text()='Усунути фільтри']"

    # add item to cart
    ITEM_ELEMENT_XPATH = ".//img[@src='https://img2.ans-media.com/i/314x471/SS22-OBM2KL_59X_F1.jpg?v=1654497179']"
    ITEM_ELEMENT_2_XPATH = ".//img[@src='https://img2.ans-media.com/i/314x471/AW21-OBM2F7_55X_F1.jpg?v=1654064660']"
    ADD_TO_CART_XPATH = ".//button[text()='Додати у Кошик']"
    CHOOSE_SIZE_DROPDOWN_XPATH = ".//span[text()='Вибрати розмір']"
    CHOOSE_SIZE_XPATH = ".//span[text()='42']"
    CART_XPATH = ".//a[@href='/cart']"

    # for closing mailing pop-up
    POP_UP_MAILING_IMG_XPATH = ".//img[@src='https://cdn.ans-media.com/assets/front/ans/9.26.2-ans/static/media/newsletter-popup.jpg']"
    POP_UP_MAILING_CLOSE_ICON_XPATH = ".//div[@class='Modal__close__3azF3']"

    # cart
    BUY_BUTTON_XPATH = ".//div[text()='Купити']"
