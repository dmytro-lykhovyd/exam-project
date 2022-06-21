"""Profile page object contains methods for registration new user"""
from constants.profile_page import ProfilePageConstants
from pages.base_page import BasePage
from pages.utils import log_wrapper


class ProfilePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = ProfilePageConstants()

    @log_wrapper
    def go_to_profile_page(self):
        """goes to the registration/autentification page"""
        self.accept_all_cookies()
        self.wait_until_clickable(self.constants.USER_PROFILE_XPATH).click()

    @log_wrapper
    def verify_profile_page_is_open(self):
        """verifies that profile page open"""
        create_account_button = self.wait_until_displayed(self.constants.CREATE_ACCOUNT_BUTTON_XPATH)
        assert create_account_button.is_enabled(), "Profile page is not opened"

    @log_wrapper
    def open_account_form(self):
        """opens fillable form for creating an account"""
        btn = self.wait_until_clickable(self.constants.CREATE_ACCOUNT_BUTTON_XPATH)
        btn.click()
        radio_btn = self.wait_until_clickable(self.constants.SEX_MALE_RADIO_BUTTON_XPATH)
        radio_btn.click()

    @log_wrapper
    def create_account(self):
        """creates an account with random valid credentials"""
        self.fill_field(self.constants.INPUT_FIRSTNAME_XPATH, f"{self.random_str()}")
        self.fill_field(self.constants.INPUT_SURNAME_XPATH, f"{self.random_str()}")
        self.fill_field(self.constants.INPUT_PHONE_XPATH, f"0123{self.random_num()}")
        self.fill_field(self.constants.INPUT_EMAIL_XPATH, f"{self.random_str()}@random.mail")
        self.fill_field(self.constants.INPUT_PASSWORD_XPATH, "123456AA")
        self.fill_field(self.constants.INPUT_PASSWORD_REPEAT_XPATH, "123456AA")
        #  self.wait_until_clickable(self.constants.TERMS_CHECKBOX_XPATH).click() - redirect to the shop rules,
        #  cannot check the checkbox

    @log_wrapper
    def verify_error_message(self):
        """verifies that error message is shown after clicking on
        Create account button without checking Terms checkbox"""
        self.wait_until_clickable(self.constants.CONFIRM_ACCOUNT_CREATION_BUTTON_XPATH).click()
        assert self.wait_until_clickable(self.constants.ERROR_TEXT_XPATH).is_displayed(), "Error message is not shown"



