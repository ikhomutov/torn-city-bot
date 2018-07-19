# coding: utf-8

import re

from selenium.common.exceptions import NoSuchElementException

from ..base.decorators import ensure_on_page
from ..base.page import BasePage
from . import constants
from . import locators


class CrimePage(BasePage):
    url = 'crimes.php'

    @ensure_on_page
    def commit_crime(self, code):
        if code not in constants.CRIMES:
            print('Wrong crime code!')
            return
        crime1, crime2 = constants.CRIMES_PATH.get(code)
        # TODO: Отрефакторить, чтобы не проходить полный путь заново
        try:
            self.driver.find_element_by_xpath(locators.MAIN_CRIME_FORM_XPATH)
        except NoSuchElementException:
            self.driver.get(self.url)
        crime_row = self.driver.find_element(*crime1)
        nerve_cost_text = crime_row.find_element_by_xpath(
            locators.NERVE_COST_XPATH).text
        nerve_cost = int(re.match(r'-(\d+) Nerve', nerve_cost_text).group(1))
        if nerve_cost > self.curr_nerve:
            print('Not enough nerve!')
            return
        crime_row.click()
        self.driver.find_element(*crime2).click()
