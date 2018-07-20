# coding: utf-8

from . import locators

SEARCHTRAINSTATION = 'searchtrainstation'
SEARCHBRIDGE = 'searchbridge'
SEARCHBINS = 'searchbins'
SEARCHFOUNTAIN = 'searchfountain'
SEARCHDUMPSTER = 'searchdumpster'
SEARCHMOVIE = 'searchmovie'

CHOCOLATEBARS = 'chocolatebars'


CRIMES = [
    SEARCHTRAINSTATION,
    SEARCHBRIDGE,
    SEARCHBINS,
    SEARCHFOUNTAIN,
    SEARCHDUMPSTER,
    SEARCHMOVIE,
    CHOCOLATEBARS
]

CRIMES_PATH = {
    SEARCHTRAINSTATION: (
        locators.SEARCH_CASH_CRIME, locators.SEARCH_THE_TRAIN_STATION),
    SEARCHBRIDGE: (
        locators.SEARCH_CASH_CRIME, locators.SEARCH_UNDER_THE_OLD_BRIDGE),
    SEARCHBINS: (locators.SEARCH_CASH_CRIME, locators.SEARCH_THE_BINS),
    SEARCHFOUNTAIN: (
        locators.SEARCH_CASH_CRIME, locators.SEARCH_THE_WATER_FOUNTAIN),
    SEARCHDUMPSTER: (
        locators.SEARCH_CASH_CRIME, locators.SEARCH_THE_DUMPSTERS),
    SEARCHMOVIE: (locators.SEARCH_CASH_CRIME, locators.SEARCH_MOVIE_THEATER),

    CHOCOLATEBARS: (locators.SHOP_LIFT_CRIME, locators.LIFT_SWEET_SHOP,
                    locators.CHOCOLATEBARS),
}
