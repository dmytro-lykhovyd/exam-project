from constants.cart_page import CartPageConstants
from pages.catalog_page import CatalogPage
from pages.utils import log_wrapper


class CartPage(CatalogPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = CartPageConstants()

    @log_wrapper
    def buy_without_registration(self):
        """buy item with unregistered user"""
        self.wait_until_clickable(self.constants.BUY_BUTTON_XPATH).click()
        self.wait_until_clickable(self.constants.BUY_UNREGISTERED_BUTTON_XPATH).click()

    @log_wrapper
    def choose_delivery_company(self):
        """chooses delivery company"""
        self.wait_until_clickable(self.constants.DELIVERY_TYPE_MEEST_XPATH).click()
        self.wait_until_clickable(self.constants.ADDRESS_INPUT_BUTTON_XPATH).click()

    @log_wrapper
    def input_delivery_info(self):
        """inputs user credentials for purchase delivery and payment"""
        self.fill_field(self.constants.FIRSTNAME, f"{self.random_str()}")
        self.fill_field(self.constants.PATRONYMIC, f"{self.random_str()}")
        self.fill_field(self.constants.SURNAME, f"{self.random_str()}")
        self.fill_field(self.constants.STREET, f"{self.random_str()}")
        self.fill_field(self.constants.HOUSE_NUMBER, f"{self.random_num()}")
        self.fill_field(self.constants.POSTAL_CODE, f"{self.random_num()}")
        self.fill_field(self.constants.REGION, f"{self.random_str()}")
        self.fill_field(self.constants.CITY, f"{self.random_str()}")
        self.fill_field(self.constants.PHONE, f"0123{self.random_num()}")
        self.fill_field(self.constants.EMAIL, f"{self.random_str()}@random.mail")
        self.wait_until_clickable(self.constants.PAYMENT_BUTTON_XPATH).click()
        self.wait_until_displayed(self.constants.TOTAL_XPATH).click()

    @log_wrapper
    def payment(self):
        """fills purchase remark and inputs password for creating an account during purchasing"""
        self.fill_field(self.constants.PURCHASE_REMARK_XPATH, self.constants.PURCHASE_REMARK_TEXT)
        self.fill_field(self.constants.CREATE_ACC_OPTIONAL_XPATH, f"{self.random_str()}{self.random_num()}")

    @log_wrapper
    def verify_payment_is_staged(self):
        """verifies that payment can be performed with previously given credentials"""
        assert self.wait_until_displayed(self.constants.ORDER_PAY_XPATH).is_enabled()
