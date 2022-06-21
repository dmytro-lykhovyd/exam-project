"""constants for profile page"""
from constants.base import BaseConstants


class ProfilePageConstants(BaseConstants):
    """constants for user account creation"""
    #  go to profile page
    USER_PROFILE_XPATH = ".//a[@href='/mii-akkaunt']"

    #  register new user
    CREATE_ACCOUNT_BUTTON_XPATH = ".//div[text()='Створити Акаунт']"
    SEX_MALE_RADIO_BUTTON_XPATH = ".//label[text()='Чоловік']"
    INPUT_FIRSTNAME_XPATH = ".//input[@id='firstName']"
    INPUT_SURNAME_XPATH = ".//input[@id='surname']"
    INPUT_PHONE_XPATH = ".//input[@id='phone']"
    INPUT_EMAIL_XPATH = ".//input[@maxlength='70']"
    INPUT_PASSWORD_XPATH = ".//input[@id='plaintextPassword.first']"
    INPUT_PASSWORD_REPEAT_XPATH = ".//input[@id='plaintextPassword.second']"
    TERMS_CHECKBOX_XPATH = "//p[text() = 'Погоджуюсь з ']"   """lead to shop's terms and conditions, unused, 
                                                                    unable to check checkbox due to pseudoelements"""
    ERROR_TEXT_XPATH = ".//span[text()='Будь ласка, ознайомтеся і погодьтеся з Правилами']"
    CONFIRM_ACCOUNT_CREATION_BUTTON_XPATH = ".//div[text()='Створити Акаунт']"

    #  user's profile
    LOGOUT_ICON_XPATH = "//*[@id='Icon/Logout']"
    REGISTERED_USER_PROFILE_XPATH = "//*[@id='user-(7)']"
