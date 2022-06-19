import random
import string

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from constants.base import BaseConstants


class BasePage:
    """Base Page Object"""
    def __init__(self, driver):
        self.driver: WebDriver = driver
        driver.maximize_window()
        self.waiter = WebDriverWait(driver=driver, timeout=5)
        self.constants = BaseConstants()

    @staticmethod
    def random_num() -> str:
        """Generate random number"""
        return str(random.randint(111111, 999999))

    @staticmethod
    def random_str(length=5):
        """Generate random string"""
        return "".join(random.choice(string.ascii_letters) for _ in range(length))

    def accept_all_cookies(self):
        """accepts all cookies"""
        self.wait_until_clickable(locator=self.constants.ACCEPT_ALL_COOKIES_XPATH).click()
        assert not self.is_element_exists(locator=self.constants.ACCEPT_ALL_COOKIES_XPATH)

    def wait_until_clickable(self, locator: str) -> WebElement:
        """waits until element becomes clickable"""
        return self.waiter.until(method=expected_conditions.element_to_be_clickable((By.XPATH, locator)))

    def wait_until_displayed(self, locator: str) -> WebElement:
        """waits until element becomes displayed"""
        return self.waiter.until(method=expected_conditions.visibility_of_element_located((By.XPATH, locator)))

    def is_element_exists(self, locator: str) -> bool:
        """Check if certain element exists"""
        try:
            self.driver.find_element(by=By.XPATH, value=locator)
            return True
        except (TimeoutError, NoSuchElementException):
            return False

    def fill_field(self, locator: str, value: str):
        """Send data into the field"""
        field = self.wait_until_clickable(locator)
        field.clear()
        field.send_keys(value)

    def click_on_button(self, locator: str):
        """Find and Click on button"""
        self.wait_until_clickable(locator).click()

    def retry(self, tries="", delay="", max_delay="", backoff=""):
        """Retry method"""


