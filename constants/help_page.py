"""help page constants"""
from constants.base import BaseConstants


class HelpPageConstants(BaseConstants):
    """constants for testing help center"""

    FAQ_XPATH = ".//a[@href='/poshyreni-zapytannia']"
    PROMOCODES_XPATH = ".//p[text()='ПРОМОКОДИ / ANSWEARClub']"
    PROMOCODE_FAILURE_XPATH = ".//span[text()='ПРОМОКОД НЕ СПРАЦЬОВУЄ. ЩО МОЖЕ БУТИ НЕ ТАК?']"
    PROMOCODE_FAILURE_MESSAGE_XPATH = '//*[@id="root"]/main/div/div/div[1]/div[3]/div[2]/div[4]/div[2]/p'
    ORDER_QUESTIONS_XPATH = ".//img[@src='https://img2.ans-media.com/ua/cms/faq/section/7-6204e92af36ea1.26540671']"
    CHANGE_ORDER_QUESTION_XPATH = ".//span[text()='ЧИ МОЖУ Я ЗМІНИТИ ЗАМОВЛЕННЯ?']"

