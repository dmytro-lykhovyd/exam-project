import datetime
import logging
from time import sleep


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
