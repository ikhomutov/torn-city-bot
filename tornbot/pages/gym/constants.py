# coding: utf-8

from . import locators

STRENGTH = 'strength'
DEFENSE = 'defense'
SPEED = 'speed'
DEXTERITY = 'dexterity'

STAT_MAPPING = {
    STRENGTH: {
        'div': locators.STRENGTH_DIV,
        'input': locators.STRENGTH_INPUT,
        'button': locators.STRENGTH_TRAIN,
    },
    DEFENSE: {
        'div': locators.DEFENSE_DIV,
        'input': locators.DEFENSE_INPUT,
        'button': locators.DEFENSE_TRAIN,
    },
    SPEED: {
        'div': locators.SPEED_DIV,
        'input': locators.SPEED_INPUT,
        'button': locators.SPEED_TRAIN,
    },
    DEXTERITY: {
        'div': locators.DEXTERITY_DIV,
        'input': locators.DEXTERITY_INPUT,
        'button': locators.DEXTERITY_TRAIN,
    },
}

GYMS_MAPPING = {
    'light': {
        'tab': locators.GYMS_TAB_LIGHT,
        'div': locators.GYMS_LIST_LIGHT,
    },
    'middle': {
        'tab': locators.GYMS_TAB_MIDDLE,
        'div': locators.GYMS_LIST_MIDDLE,
    },
    'heavy': {
        'tab': locators.GYMS_TAB_HEAVY,
        'div': locators.GYMS_LIST_HEAVY,
    },
    'special': {
        'tab': locators.GYMS_TAB_SPECIAL,
        'div': locators.GYMS_LIST_SPECIAL,
    },
}
