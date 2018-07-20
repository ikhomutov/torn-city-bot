# coding: utf-8

from selenium.webdriver.support.ui import WebDriverWait

from . import locators


class BaseElement(object):
    locator = None

    def __get__(self, obj, owner):
        driver = obj.driver
        return driver.find_element(*self.locator)


class EnergyElement(BaseElement):
    locator = locators.ENEGRY_VALUE


class NerveElement(BaseElement):
    locator = locators.NERVE_VALUE


class HappyElement(BaseElement):
    locator = locators.HAPPY_VALUE


class LifeElement(BaseElement):
    locator = locators.LIFE_VALUE
