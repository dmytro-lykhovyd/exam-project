from time import sleep

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

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
        self.wait_until_clickable(self.constants.PROMOCODE_FAILURE_XPATH).click()
        assert self.wait_until_displayed(self.constants.PROMOCODE_FAILURE_MESSAGE_XPATH).is_displayed(), \
        "Text is not visible"

    @log_wrapper
    @wait_until_ok(timeout=5, period=0.5)
    def open_order_page(self):
        """opens page with order questions"""
        self.wait_until_clickable(self.constants.PROMOCODE_FAILURE_XPATH).click()
        order_questions = self.wait_until_clickable(self.constants.ORDER_QUESTIONS_XPATH)
        ActionChains(self.driver).move_to_element(order_questions).perform()
        order_questions.click()
        assert self.wait_until_displayed(self.constants.CHANGE_ORDER_QUESTION_XPATH).is_enabled(), \
            "Order questions was not opened"

