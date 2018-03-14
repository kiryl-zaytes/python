from common_descriptors.desc import Check

__author__ = 'kiryl_zayets'
from abc import ABCMeta


class Weapon(metaclass=ABCMeta):
    MAX_LENGTH = 200.0

    def __init__(self, length, offense_rate, for_one_hand=True, for_throw=False):
        self.length = length
        self.offense_rate = offense_rate
        self._one_hand = for_one_hand
        self._throw = for_throw

    length = Check(typ=float, func=lambda x: 0 < x < Weapon.MAX_LENGTH)
    offense_rate = Check(typ=int, func=lambda x: x > 0)

    @property
    def throw(self):
        return self._throw

    @property
    def one_hand(self):
        return self._one_hand

    @throw.setter
    def throw(self, value):
        if value in ['true', 'false']:
            self._throw = value
        else:
            raise AttributeError

    @one_hand.setter
    def one_hand(self, value):
        if value in ['true', 'false']:
            self._throw = value
        else:
            raise AttributeError


class TwoHandedWeapon(Weapon):
    def __init__(self, length, offense_rate):
        super().__init__(length, offense_rate, for_one_hand=False, for_throw=False)


class OneHandedWeapon(Weapon):
    def __init__(self, length, offense_rate):
        super().__init__(length, offense_rate, for_one_hand=True, for_throw=False)

class ThrowingWeapon(Weapon):
    def __init__(self, length, offense_rate):
        super().__init__(length, offense_rate, for_one_hand=True, for_throw=True)


class OneHandAxe(OneHandedWeapon):
    pass

class TwoHandSword(TwoHandedWeapon):
    pass