__author__ = 'kiryl_zayets'


class Material:
    WOOD, STEEL, COPPER = range(3)


class Enum(set):
    def __getattr__(self, item):
        if item in self:
            return item
        raise AttributeError

    def add(self, other):
        raise AttributeError


Materials = Enum(['STEEL', 'WOOD', 'COPPER', 'CLOTH'])
ArmorDynasty = Enum(['BARBARIAN', 'CRUSADER', 'MAGIC', 'HORADERIC'])
ArmorType = Enum(['CLOTH', 'LIGHT', 'HEAVY'])