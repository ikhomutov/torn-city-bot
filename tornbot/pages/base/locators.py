# coding: utf-8

from selenium.webdriver.common.by import By

USER_STATUS = (By.XPATH, '//div[@user-status]')

MONEY = (By.ID, 'user-money')
LEVEL = (By.XPATH,
         ('//div[starts-with(@class, "points")]/p[2]'
          '/span[starts-with(@class, "value")]'))
POINTS = (By.XPATH,
          ('//div[starts-with(@class, "points")]/p[3]'
           '/span[starts-with(@class, "value")]'))

ENEGRY_VALUE = (
    By.XPATH,
    ('//a[@id="barEnergy"]/div[starts-with(@class, "bar-stats")]'
     '/p[starts-with(@class, "bar-value")]'))
NERVE_VALUE = (
    By.XPATH,
    ('//a[@id="barNerve"]/div[starts-with(@class, "bar-stats")]'
     '/p[starts-with(@class, "bar-value")]'))
HAPPY_VALUE = (
    By.XPATH,
    ('//a[@id="barHappy"]/div[starts-with(@class, "bar-stats")]'
     '/p[starts-with(@class, "bar-value")]'))
LIFE_VALUE = (
    By.XPATH,
    ('//a[@id="barLife"]/div[starts-with(@class, "bar-stats")]'
     '/p[starts-with(@class, "bar-value")]'))


CAPTCHA = (
    By.XPATH, '//div[@id="tab-menu"][contains(@class, "captcha")]')
