# coding: utf-8

import time

from . import elements
from . import locators


class BasePage(object):
    """Базовый класс для страниц.

    Включает элементы, доступные в любой момент времени
    """
    energy_element = elements.EnergyElement()
    nerve_element = elements.NerveElement()

    base_url = 'https://www.torn.com/'
    url = ''

    def __init__(self, driver):
        self.driver = driver

    @property
    def page_url(self):
        return self.base_url + self.url

    def open(self):
        self.driver.get(self.page_url)

    @property
    def curr_energy(self):
        energy = self.energy_element.text
        return int(energy.split('/')[0])

    @property
    def curr_nerve(self):
        nerve = self.nerve_element.text
        return int(nerve.split('/')[0])

    def send_keys(self, locator, keys):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(keys)
        # Пауза для достоверности поведения
        time.sleep(0.5)

    def find_element(self, locator):
        return self.driver.find_element(*locator)
