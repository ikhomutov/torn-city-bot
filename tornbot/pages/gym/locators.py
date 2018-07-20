# coding: utf-8

from selenium.webdriver.common.by import By


TRAIN_COST = (By.XPATH, '//span[@class="energycost"]')

STRENGTH_DIV = (By.ID, 'divStrength')
STRENGTH_INPUT = (By.XPATH, '//input[@name="strength"]')
STRENGTH_TRAIN = (By.ID, '1')
DEFENSE_DIV = (By.ID, 'divDefence')
DEFENSE_INPUT = (By.XPATH, '//input[@name="defense"]')
DEFENSE_TRAIN = (By.ID, '2')
SPEED_DIV = (By.ID, 'divSpeed')
SPEED_INPUT = (By.XPATH, '//input[@name="speed"]')
SPEED_TRAIN = (By.ID, '3')
DEXTERITY_DIV = (By.ID, 'divDexterity')
DEXTERITY_INPUT = (By.XPATH, '//input[@name="dexterity"]')
DEXTERITY_TRAIN = (By.ID, '4')


GYMS_TAB_XPATH = '//li[@class="%s"][@role="tab"]'
GYMS_LIST_XPATH = '//div[@id="%s"][@role="tabpanel"]'
GYMS_JOIN_ROW_XPATH = '//li[starts-with(@class, "join")]'
GYMS_JOIN_LINK_XPATH = '//a[contains(@class, "join")]'

ACTIVATE_MEMBERSHIP = (By.XPATH, '//div[@class="activate-membership"]')
BUY_CONFIRM = (By.XPATH, '//div[@class="confirm-msg"]//a[text()="Yes"]')


GYMS_TAB_LIGHT = (By.XPATH, GYMS_TAB_XPATH % 'light')
GYMS_TAB_MIDDLE = (By.XPATH, GYMS_TAB_XPATH % 'middle')
GYMS_TAB_HEAVY = (By.XPATH, GYMS_TAB_XPATH % 'heavy')
GYMS_TAB_SPECIAL = (By.XPATH, GYMS_TAB_XPATH % 'special')

GYMS_LIST_LIGHT = (By.XPATH, GYMS_LIST_XPATH % 'light')
GYMS_LIST_MIDDLE = (By.XPATH, GYMS_LIST_XPATH % 'middle')
GYMS_LIST_HEAVY = (By.XPATH, GYMS_LIST_XPATH % 'heavy')
GYMS_LIST_SPECIAL = (By.XPATH, GYMS_LIST_XPATH % 'special')
