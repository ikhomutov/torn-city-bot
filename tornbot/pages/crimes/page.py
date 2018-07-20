# coding: utf-8

import re
import time

from selenium.common.exceptions import NoSuchElementException

from . import constants
from . import locators
from ...decorators import detect_captcha
from ...decorators import ensure_on_page
from ..base.page import BasePage


class CrimePage(BasePage):
    url = 'crimes.php'

    @ensure_on_page
    @detect_captcha
    def commit_crime(self, code):
        if code not in constants.CRIMES:
            print('Wrong crime code!')
            return False
        crime_list = list(constants.CRIMES_PATH.get(code))
        crime_main = crime_list[0]

        crime_form = self.find_element(locators.CRIME_FORM)
        # Определяем на какой форме в данный момент находимся
        crime_step = crime_form.get_attribute('action').split('step=')[1]
        if not crime_step == 'docrime':
            self.open()
        crime_row = self.find_element(crime_main)
        nerve_cost_text = crime_row.find_element_by_xpath(
            locators.NERVE_COST_XPATH).text
        nerve_cost = int(re.match(r'-(\d+) Nerve', nerve_cost_text).group(1))
        if nerve_cost > self.curr_nerve:
            print('Not enough nerve!')
            return False
        for crime in crime_list:
            self.find_element(crime).click()
            time.sleep(2)
        return True
