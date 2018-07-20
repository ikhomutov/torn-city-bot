# coding: utf-8

from selenium.common.exceptions import NoSuchElementException

from . import constants
from . import locators
from ..base.page import BasePage
from ...decorators import detect_captcha
from ...decorators import ensure_on_page


class GymPage(BasePage):
    url = 'gym.php'

    @ensure_on_page
    @detect_captcha
    def train(self, stat, points=None):
        stat_locators = constants.STAT_MAPPING.get(stat)
        stat_container = self.find_element(stat_locators.get('div'))
        train_cost = stat_container.find_element(*locators.TRAIN_COST).text
        points_required = int(train_cost) * (points or 1)
        if int(self.curr_energy) < points_required:
            print('Not enough energy to train %s' % stat)
            return False
        if points:
            self.send_keys(stat_locators.get('input'), points)
        stat_container.find_element(*stat_locators.get('button')).click()
        return True

    def train_strength(self, points=None):
        return self.train('strength', points)

    def train_defense(self, points=None):
        return self.train('defense', points)

    def train_speed(self, points=None):
        return self.train('speed', points)

    def train_dexterity(self, points=None):
        return self.train('dexterity', points)

    def activate_gym(self):
        pass

    def upgrade_gym(self):
        for gyms_map in constants.GYMS_MAPPING.values():
            gyms_list = self.find_element(gyms_map.get('div'))
            try:
                join_row = gyms_list.find_element_by_xpath(
                    locators.GYMS_JOIN_ROW_XPATH)
                self.find_element(gyms_map.get('tab')).click()
                join_row.find_element_by_xpath(
                    locators.GYMS_JOIN_LINK_XPATH).click()
                self.find_element(locators.ACTIVATE_MEMBERSHIP).click()
                self.find_element(locators.BUY_CONFIRM).click()
                return
            except NoSuchElementException:
                continue
