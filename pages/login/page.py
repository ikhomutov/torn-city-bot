# coding: utf-8

from ..base.page import BasePage
from ..base.decorators import ensure_on_page
from . import locators


class LoginPage(BasePage):

    @ensure_on_page
    def login(self, login, password):
        # TODO: Добавить проверку авторизованности
        self.send_keys(locators.EMAIL_INPUT, login)
        self.send_keys(locators.PASSWORD_INPUT, password)
        self.driver.find_element(*locators.SUBMIT_INPUT).click()
