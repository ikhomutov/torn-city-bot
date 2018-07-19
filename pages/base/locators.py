# coding: utf-8

from selenium.webdriver.common.by import By


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
