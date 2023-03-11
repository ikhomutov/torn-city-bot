# coding: utf-8

import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from . import elements
from . import locators


class BasePage(object):
    """Базовый класс для страниц.

    Включает элементы, доступные в любой момент времени
    """
    energy_element = elements.EnergyElement()
    nerve_element = elements.NerveElement()
    happy_element = elements.HappyElement()
    life_element = elements.LifeElement()

    base_url = 'https://www.torn.com/'
    url = ''

    def __init__(self, driver, captcha_solver):
        self.driver = driver
        self.captcha_solver = captcha_solver

    @property
    def page_url(self):
        return self.base_url + self.url

    @property
    def status(self):
        status_element = self.get_element(locators.USER_STATUS)
        if status_element:
            return status_element.get_attribute("user-status")
        return status_element

    @property
    def curr_energy(self):
        return int(self.energy_element.text.split('/')[0])

    @property
    def max_energy(self):
        return int(self.energy_element.text.split('/')[1])

    @property
    def energy_is_full(self):
        return self.curr_energy == self.max_energy

    @property
    def curr_nerve(self):
        return int(self.nerve_element.text.split('/')[0])

    @property
    def max_nerve(self):
        return int(self.nerve_element.text.split('/')[1])

    @property
    def nerve_is_full(self):
        return self.curr_nerve == self.max_nerve

    @property
    def curr_happy(self):
        return int(self.happy_element.text.split('/')[0])

    @property
    def max_happy(self):
        return int(self.happy_element.text.split('/')[1])

    @property
    def curr_life(self):
        return int(self.life_element.text.split('/')[0])

    @property
    def max_life(self):
        return int(self.life_element.text.split('/')[1])

    @property
    def money(self):
        money_element = self.find_element(locators.MONEY)
        return money_element.get_attribute('data-money')

    @property
    def level(self):
        level_element = self.find_element(locators.LEVEL)
        return level_element.text

    @property
    def points(self):
        points_element = self.find_element(locators.POINTS)
        return points_element.text

    def handle_captcha(self):
        if self.get_element(locators.CAPTCHA):
            self.captcha_solver.solve()

    def send_keys(self, locator, keys):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(keys)
        # Пауза для достоверности поведения
        time.sleep(0.5)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def get_element(self, locator, default=None):
        try:
            element = WebDriverWait(self.driver, 5).until(
                ec.presence_of_element_located(locator))
            return element
        except TimeoutException:
            return default

    def open(self):
        self.driver.get(self.page_url)
