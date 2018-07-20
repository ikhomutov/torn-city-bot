# coding: utf-8

from ..base.page import BasePage
from ...decorators import ensure_on_page
from . import locators


class LoginPage(BasePage):

    @ensure_on_page
    def login(self, login, password):
        if self.status == 'logged-out':
            self.send_keys(locators.EMAIL_INPUT, login)
            self.send_keys(locators.PASSWORD_INPUT, password)
            self.driver.find_element(*locators.SUBMIT_INPUT).click()
