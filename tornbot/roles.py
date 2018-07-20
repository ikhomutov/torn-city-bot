# coding: utf-8

from .pages.gym import constants


class Fighter(object):
    """
    Класс-примесь, отвечающая за поведение бойца:

    - посещение спортзала
    - атака других игроков
    """
    role_index = '1'

    def get_full_action_index(self, action_index):
        return '{}{}'.format(self.role_index, action_index)

