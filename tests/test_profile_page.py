import logging
from time import sleep
import conftest

import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from constants.base import BaseConstants
from pages.profile_page import ProfilePage
from pages.utils import User
import conftest


class TestProfilePage:
    log = logging.getLogger('[StartPage]')

    @pytest.fixture(scope="function")
    def profile_page(self):
        driver = WebDriver(executable_path=BaseConstants.DRIVER_PATH)
        driver.implicitly_wait(2)
        driver.get(BaseConstants.BASE_URL)
        yield ProfilePage(driver)
        driver.close()

    @pytest.fixture(scope="function")
    def user(self):
        return User

    def test_sign_up(self, profile_page, user):
        """
        - Preconditions:
            - Create driver
            - Open start page
        - Steps:
            - Check radiobutton sex
            - Fill Firstname field
            - Fill Surname field
            - Fill Phone field
            - Fill Email field
            - Fill Password field
            - Fill Repeat password field
            - Press 'Create account' button
            - Verify successful registration
        """

        profile_page.go_to_profile_page()
        profile_page.verify_profile_page_is_open()
        profile_page.open_account_form()
        profile_page.create_account()
        # profile_page =
        #  profile_page.verify_account_is_created()
