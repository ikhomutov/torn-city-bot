# coding: utf-8

import os

from dotenv import load_dotenv
from tornbot.bot import Bot

load_dotenv(dotenv_path='.env')

TORN_EMAIL = os.getenv('TORN_EMAIL')
TORN_PASSWORD = os.getenv('TORN_PASSWORD')

bot = Bot(TORN_EMAIL, TORN_PASSWORD)
