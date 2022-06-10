from time import sleep

from selenium.webdriver.chrome.webdriver import WebDriver
import logging
import pytest
from selenium.webdriver.common.by import By
from constants import base

class TestBasic:
    log = logging.getLogger('[Basic]')

    def test_basic(self):
        driver = WebDriver(executable_path="/Users/dmytrolykhovyd/PycharmProjects/exam-project/chromedriver")
        driver.maximize_window()
        driver.get("https://answear.ua")
        self.log.info("Opened")
        accept_cookies = driver.find_element(by=By.XPATH, value=".//button[@Class='btn btn--primary CookiesInfo__cookiesInfoBtnWrapperAccept__2r6s4']")
        sleep(3)
        accept_cookies.click()
        sleep(3)
        self.log.info("All cookies accepted")
        vin = driver.find_element(by=By.XPATH, value=".//a[@href='/mii-akkaunt']")
        sleep(5)
        vin.click()
        sleep(1)
        self.log.info("Profile icon is displayed")
        driver.close()
