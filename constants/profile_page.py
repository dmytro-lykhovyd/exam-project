from constants.base import BaseConstants


class ProfilePageConstants(BaseConstants):

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
    TERMS_CHECKBOX_XPATH = "/html/body/div[1]/main/div/div/div[2]/div[2]/div[2]/form/div[7]/div[1]" #.//input[@name='agreement.terms']"
    #  ".//p[text()='Погоджуюсь з ']"
    CONFIRM_ACCOUNT_CREATION_BUTTON_XPATH = ".//button[text()='Створити Акаунт']"

    #  user's profile
    # CLOSE_MAILING_POPUP_XPATH =
    LOGOUT_ICON_XPATH = "//*[@id='Icon/Logout']"
    REGISTERED_USER_PROFILE_XPATH = "//*[@id='user-(7)']"
