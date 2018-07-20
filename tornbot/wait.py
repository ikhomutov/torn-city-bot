# coding: utf-8

import time

from selenium.webdriver.support.wait import WebDriverWait


class CustomWebDriverWait(WebDriverWait):
    def infinite_until(self, method, message=''):
        """Не завершается по прошествии времени, только по событию"""

        while True:
            try:
                value = method(self._driver)
                if value:
                    return value
            except self._ignored_exceptions as exc:
                pass
            time.sleep(self._poll)
