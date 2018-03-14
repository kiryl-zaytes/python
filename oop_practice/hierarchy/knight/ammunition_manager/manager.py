__author__ = 'Kiryl_Zayets'


class WarriorManager(object):
    def __init__(self, armor, weapon, warrior):
        self.armor = armor
        self.weapon = weapon
        self.warrior = warrior

    def dress(self):
        pass


class ArmorManager(object):

    def __init__(self, armor_dole):
        self._price = 0
        self._armor_doll = armor_dole

    def __call__(self, *args, **kwargs):
        pass

    @classmethod
    def create(cls, armor_spec):
        pass


class WeaponManager(object):
    pass