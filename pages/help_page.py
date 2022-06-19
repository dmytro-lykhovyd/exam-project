from time import sleep

from constants.help_page import HelpPageConstants
from pages.base_page import BasePage
from pages.utils import log_wrapper, wait_until_ok


class HelpPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = HelpPageConstants()

    @log_wrapper
    def open_promocode_page(self):
        """opens page with frequently asked questions"""
        self.accept_all_cookies()
        self.wait_until_clickable(self.constants.FAQ_XPATH).click()
        self.wait_until_clickable(self.constants.PROMOCODES_XPATH).click()
        sleep(5)
        self.wait_until_clickable(self.constants.PROMOCODE_FAILURE_XPATH).click()
        assert self.wait_until_displayed(self.constants.PROMOCODE_FAILURE_MESSAGE_XPATH).is_displayed(), \
        "Text is not visible"

    @log_wrapper
    @wait_until_ok(timeout=5, period=0.5)
    def open_payment_page(self):
        """opens page with payment FAQ and verifies the link to special rules for 150+ euro payment"""
        self.wait_until_clickable(self.constants.PROMOCODE_FAILURE_XPATH).click()
        sleep(5)
        self.wait_until_clickable(self.constants.PAYMENT_QUESTIONS_XPATH).click()
        sleep(4)
        self.wait_until_clickable(self.constants.PAYMENT_150_EURO_INFO_XPATH).click()
        sleep(4)
        self.wait_until_clickable(self.constants.PAYMENT_150_EURO_INFO_LINK).click()
        sleep(4)
        assert self.wait_until_clickable(self.constants.TAXES_CALCULATION_XPATH).is_displayed(), "Page don't open"

