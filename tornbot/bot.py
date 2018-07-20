# coding: utf-8

import time

from selenium import webdriver

from .pages.crimes.page import CrimePage
from .pages.crimes import constants as crime_constants
from .pages.gym.page import GymPage
from .pages.gym import constants as gym_constants
from .pages.login.page import LoginPage
from .pages.usersearch.page import UserSearchPage


class Bot(object):
    def __init__(self, torn_email, torn_password):
        self.torn_email = torn_email
        self.torn_password = torn_password

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

        # список возможных действий
        self.posible_actions = {}

        self.login_page = LoginPage(self.driver)
        self.gym_page = GymPage(self.driver)
        self.crime_page = CrimePage(self.driver)
        self.usersearch_page = UserSearchPage(self.driver)

    def login(self):
        self.login_page.login(self.torn_email, self.torn_password)

    def quit(self):
        self.driver.quit()

    def make_decision(self):
        if self.gym_page.energy_is_full:
            self.posible_actions['11'] = 'train'
        if self.crime_page.nerve_is_full:
            self.posible_actions['21'] = 'crime'

    def crime(self):
        default_crime = crime_constants.CHOCOLATEBARS
        result = True
        while result:
            if self.crime_page.status == 'ok':
                result = self.crime_page.commit_crime(default_crime)
            else:
                result = False
        self.posible_actions.pop('21')

    def train(self):
        train_map = {
            gym_constants.STRENGTH: 3,
            gym_constants.DEFENSE: 5,
            gym_constants.SPEED: 5,
            gym_constants.DEXTERITY: 7
        }
        for stat, value in train_map.items():
            self.gym_page.train(stat, value)
        self.posible_actions.pop('11')

    def alive(self):
        """Запуск автономного бота.

        В цикле сначала ищет возможные действия, затем выполняет их"""
        # TODO: обеспечить возможность прерывания метода
        while True:
            self.make_decision()
            for action_key in sorted(self.posible_actions.keys()):
                getattr(self, self.posible_actions.pop(action_key))()
            time.sleep(30)
