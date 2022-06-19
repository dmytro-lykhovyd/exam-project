from constants.base import BaseConstants


class HelpPageConstants(BaseConstants):

    FAQ_XPATH = ".//a[@href='/poshyreni-zapytannia']"
    PROMOCODES_XPATH = ".//p[text()='ПРОМОКОДИ / ANSWEARClub']"
    PROMOCODE_FAILURE_XPATH = ".//span[text()='ПРОМОКОД НЕ СПРАЦЬОВУЄ. ЩО МОЖЕ БУТИ НЕ ТАК?']"
    PROMOCODE_FAILURE_MESSAGE_XPATH = '//*[@id="root"]/main/div/div/div[1]/div[3]/div[2]/div[4]/div[2]/p'   # ".//p[text() = 'перевірте чи коректно Ви написали промокод']"
    PAYMENT_QUESTIONS_XPATH = ".//p[text()='ОПЛАТА']"
    PAYMENT_150_EURO_INFO_XPATH = ".//span[text()='ЩО МЕНІ ВАРТО ЗНАТИ, КУПУЮЧИ ТОВАР ДОРОЖЧЕ 150 ЄВРО?']"
    PAYMENT_150_EURO_INFO_LINK = ".//a[@href='/scho-potribno-znaty-kupuyuchy-tovar-dorozhche-150-ievro']"
    TAXES_CALCULATION_XPATH = ".//td[text()='Митний збір: (170-150) * 10% = 2,00€']"

