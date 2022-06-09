import datetime
import logging
import random
import string
from time import sleep

from selenium.webdriver.chrome.webdriver import WebDriver

from constants.base import BaseConstants


def random_num():
    """Generate random number"""
    return str(random.randint(100000, 999999))


def random_str(length=6):
    """Generate random string"""
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))


class User:

    def __init__(self, firstname="", surname="", phone="", email="", password=""):
        self.firstname = firstname if firstname else f"{random_str()}{random_num()}"
        self.surname = surname if surname else f"{random_str()}{random_num()}"
        self.phone = phone if phone else f"{1}{random_num()}"
        self.email = email if email else f"{surname}@random.mail"
        self.password = password if password else f"{random_str(6)}{random_num()}"

    # def __str__(self):
    #     return self


def wait_until_ok(timeout: int, period: float):
    """Retries function until ok"""
    logger = logging.getLogger("[WaitUntilOk]")

    def decorator(original_function):

        def wrapper(*args, **kwargs):
            end_time = datetime.datetime.now() + datetime.timedelta(seconds=timeout)
            while True:
                try:
                    return original_function(*args, **kwargs)
                except Exception as err:
                    if datetime.datetime.now() > end_time:
                        logger.warning(f"Catch: {err}")
                        raise err
                    sleep(period)

        return wrapper

    return decorator


def log_wrapper(func):
    """add logs for method using docstring"""

    def wrapper(*args, **kwargs):
        log = logging.getLogger("[LogDecorator]")
        result = func(*args, **kwargs)
        if len(args) > 1 and isinstance(args[1], User):
            log.info(f"Using profile: {args[1].username}")
        log.info(f"{func.__doc__}")
        return result

    return wrapper
