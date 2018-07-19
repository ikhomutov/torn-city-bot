# coding: utf-8

from . import locators

STAT_MAPPING = {
    'strength': {
        'div': locators.STRENGTH_DIV,
        'input': locators.STRENGTH_INPUT,
        'button': locators.STRENGTH_TRAIN,
    },
    'defense': {
        'div': locators.DEFENSE_DIV,
        'input': locators.DEFENSE_INPUT,
        'button': locators.DEFENSE_TRAIN,
    },
    'speed': {
        'div': locators.SPEED_DIV,
        'input': locators.SPEED_INPUT,
        'button': locators.SPEED_TRAIN,
    },
    'dexterity': {
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
