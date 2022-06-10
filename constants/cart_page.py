from constants.base import BaseConstants
from constants.catalog_page import CatalogPageConstants


class CartPageConstants(CatalogPageConstants):
    # delivery type
    BUY_BUTTON_XPATH = ".//div[text()='Купити']"
    BUY_UNREGISTERED_BUTTON_XPATH = ".//div[text()='Покупка без реєстрації']"
    DELIVERY_TYPE_MEEST_XPATH = ".//label[@for='deliveryMethod_radio_05']"
    ADDRESS_INPUT_BUTTON_XPATH = ".//div[text()='Адресні дані']"

    # delivery address
    FIRSTNAME = ".//input[@id='firstName']"
    PATRONYMIC = ".//input[@id='patronymic']"
    SURNAME = ".//input[@id='surname']"
    STREET = ".//input[@id='street']"
    HOUSE_NUMBER = ".//input[@id='houseNumber']"
    POSTAL_CODE = ".//input[@id='postalCode']"
    REGION = ".//input[@id='region']"
    CITY = ".//input[@id='city']"
    PHONE = ".//input[@id='phone']"
    EMAIL = ".//input[@id='email']"
    PAY_BUTTON_XPATH = ".//div[text()='Оплата']"

    # paying process
    TOTAL_XPATH = ".//div[text()='Всього']"
    ORDER_PAY_XPATH = ".//div[text()='Замовляю/Сплачую']"  # for assertion only!

    