__author__ = 'kiryl_zayets'

from abc import *
from ammunition.material import Materials
from ammunition.material import ArmorDynasty
from ammunition.material import ArmorType
from common_descriptors.desc import Check


class ArmorSpec(object):
    """
        Carrying armor specifications in separated objects.
    """
    MAX_WEIGHT = 20
    MAX_DEFENCE_RATE = 100

    def __init__(self, material, weight, type_, rate):
        self.material = material
        self.weight = weight
        self.type_ = type_
        self.defense_rate = rate

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return (self.weight == other.weight and
                self.defense_rate == other.defense_rate)

    def __lt__(self, other):
        return (self.defense_rate) < (other.defense_rate)

    def get_weight(self):
        try:
            return self._weight
        except AttributeError:
            self._weight = None
        return self._weight

    def set_weight(self, value):
        if ArmorSpec.MAX_WEIGHT > value > 0:
            self._weight = value
        else:
            raise AttributeError

    def get_material(self):
        try:
            return self._material
        except:
            self._material = None
        return self._material

    def set_material(self, value):
        if value in Materials:
            self._material = value

    def set_type(self, value):
        if value in ArmorType:
            self._type_ = value

    def get_type(self):
        try:
            return self._type_
        except AttributeError:
            self._type_ = None
        return self._type_

    defense_rate = Check(typ=int, func=lambda x: 0 < x < ArmorSpec.MAX_DEFENCE_RATE)
    weight = property(fget=get_weight, fset=set_weight)
    material = property(fget=get_material, fset=set_material)
    type_ = property(fget=get_type, fset=set_type)


class Armor(metaclass=ABCMeta):
    """

    Abstract entity for all defense hierarchy

    """

    def __init__(self, armor_spec, part_of_set=None):
        self._armor_spec = armor_spec
        self.part_of_set = part_of_set

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return (self.part_of_set == other.part_of_set and
                self._armor_spec == other.armor_spec)


    @property
    def armor_spec(self):
        return self._armor_spec

    @property
    def part_of_set(self):
        try:
            return self._part_of_set
        except AttributeError:
            self._part_of_set = None
        return self._part_of_set

    @part_of_set.setter
    def part_of_set(self, value):
        if value in ArmorDynasty:
            self._part_of_set = value
        else:
            raise AttributeError


class Chest(Armor):
    pass


class Leg(Armor):
    pass


class Gloves(Armor):
    pass


class Boots(Armor):
    pass


class Helmet(Armor):
    pass


class Shield(Armor):
    pass