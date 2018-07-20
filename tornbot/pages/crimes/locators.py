# coding: utf-8

from selenium.webdriver.common.by import By


BASE_CRIME_XPATH = ('//input[@name="crime"][@value="{}"]'
                    '//ancestor::ul[contains(@class, "item")]')
NERVE_COST_XPATH = '//li[starts-with(@class, "points")]'

CRIME_FORM = (By.XPATH, '//form[@name="crimes"]')
BACK_TO_CRIMES = (By.ID, 'back')

SEARCH_CASH_CRIME = (By.XPATH, BASE_CRIME_XPATH.format('search-for-cash'))
SEARCH_THE_TRAIN_STATION = (
    By.XPATH, BASE_CRIME_XPATH.format('search-the-train-station'))
SEARCH_UNDER_THE_OLD_BRIDGE = (
    By.XPATH, BASE_CRIME_XPATH.format('search-under-the-old-bridge'))
SEARCH_THE_BINS = (
    By.XPATH, BASE_CRIME_XPATH.format('search-the-bins'))
SEARCH_THE_WATER_FOUNTAIN = (
    By.XPATH, BASE_CRIME_XPATH.format('search-the-water-fountain'))
SEARCH_THE_DUMPSTERS = (
    By.XPATH, BASE_CRIME_XPATH.format('search-the-dumpsters'))
SEARCH_MOVIE_THEATER = (
    By.XPATH, BASE_CRIME_XPATH.format('search-movie-theater'))

SELL_MEDIA_CRIME = (By.XPATH, BASE_CRIME_XPATH.format('sell-copied-media'))

SHOP_LIFT_CRIME = (By.XPATH, BASE_CRIME_XPATH.format('shoplift'))
LIFT_SWEET_SHOP = (By.XPATH, BASE_CRIME_XPATH.format('sweetshop'))
CHOCOLATEBARS = (By.XPATH, BASE_CRIME_XPATH.format('chocolatebars'))

LIFT_MARKET_STALL = (By.XPATH, BASE_CRIME_XPATH.format('marketstall'))
LIFT_CLOTHES_SHOP = (By.XPATH, BASE_CRIME_XPATH.format('clothesshop'))
LIFT_JEWELLERY_SHOP = (By.XPATH, BASE_CRIME_XPATH.format('jewelleryshop'))

PICKPOCKET_CRIME = (By.XPATH, BASE_CRIME_XPATH.format('pickpocket-someone'))
LARCENY_CRIME = (By.XPATH, BASE_CRIME_XPATH.format('larceny'))
ARMED_ROBBERIES_CRIME = (By.XPATH, BASE_CRIME_XPATH.format('armed-robberies'))
TRANSPORT_DRUGS_CRIME = (By.XPATH, BASE_CRIME_XPATH.format('transport-drugs'))
VIRUS_CRIME = (By.XPATH, BASE_CRIME_XPATH.format('plant-a-computer-virus'))
ASSASINATION_CRIME = (By.XPATH, BASE_CRIME_XPATH.format('assassination'))
ARSON_CRIME = (By.XPATH, BASE_CRIME_XPATH.format('arson'))
GTA_CRIME = (By.XPATH, BASE_CRIME_XPATH.format('grand-theft-auto'))
PAWN_SHOP_CRIME = (By.XPATH, BASE_CRIME_XPATH.format('pawn-shop'))
COUNTERFEITING_CRIME = (By.XPATH, BASE_CRIME_XPATH.format('counterfeiting'))
KIDNAPPING_CRIME = (By.XPATH, BASE_CRIME_XPATH.format('kidnapping'))
ARMS_TRAFFIC_CRIME = (By.XPATH, BASE_CRIME_XPATH.format('arms-trafficking'))
BOMBINGS_CRIME = (By.XPATH, BASE_CRIME_XPATH.format('bombings'))
HACKING_CRIME = (By.XPATH, BASE_CRIME_XPATH.format('hacking'))
