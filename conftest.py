import datetime
import os

import pytest

from constants.base import BaseConstants


def pytest_sessionstart(session):
    os.environ["PATH"] = os.environ["PATH"] + f":{os.path.abspath(BaseConstants.DRIVER_PATH)}"


# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_make_report(item, call):
#     """makes screenshot when test fails"""
#     outcome = yield
#     result = outcome.get_result()
#     if result.failed:
#         driver = [item.funkargs[arg] for arg in item.funkargs if arg.endswith("_page")][0].driver
#         file_name = f"{item.name}_{datetime.datetime.today().strftime('%Y-%m-%d_%H:%M:%S')}.png"
#         file_path = os.path.curdir
#         driver.save_screenshot(os.path.join(file_path, file_name))
