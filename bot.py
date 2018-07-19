# coding: utf-8

import os

from dotenv import load_dotenv
from selenium import webdriver

from pages.crimes.page import CrimePage
from pages.gym.page import GymPage
from pages.login.page import LoginPage
from pages.usersearch.page import UserSearchPage

load_dotenv(dotenv_path='.env')

TORN_EMAIL = os.getenv('TORN_EMAIL')
TORN_PASSWORD = os.getenv('TORN_PASSWORD')


class Bot(object):
    def __init__(self, torn_email, torn_password):
        self.torn_email = torn_email
        self.torn_password = torn_password

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

        self.login_page = LoginPage(self.driver)
        self.gym_page = GymPage(self.driver)
        self.crime_page = CrimePage(self.driver)
        self.usersearch_page = UserSearchPage(self.driver)

    def login(self):
        self.login_page.login(self.torn_email, self.torn_password)

    def quit(self):
        self.driver.quit()
