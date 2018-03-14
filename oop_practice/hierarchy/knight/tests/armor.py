from ammunition.material import ArmorType, ArmorDynasty

__author__ = 'kiryl_zayets'
import unittest
from ammunition.armor import Chest, ArmorSpec
from ammunition.armor import Materials
from ammunition.weapon import TwoHandSword

class ArmorTest(unittest.TestCase):

    def test_create_armor(self):
        spec = ArmorSpec(Materials.COPPER, 15, ArmorType.HEAVY, 43)

        chest = Chest(armor_spec=spec, part_of_set=ArmorDynasty.BARBARIAN)

        self.assertEqual(chest.armor_spec.material, Materials.COPPER)
        self.assertEqual(chest.armor_spec.weight, 15)

    def test_create_armor_type(self):
        spec = ArmorSpec(Materials.STEEL, 15, ArmorType.HEAVY, 50)
        chest = Chest(armor_spec=spec, part_of_set=ArmorDynasty.HORADERIC)
        self.assertEqual(chest.part_of_set, ArmorDynasty.HORADERIC)

    def test_equal_armor(self):
        armor1 = ArmorSpec(Materials.STEEL, 13, ArmorType.HEAVY, 40)
        armor2 = ArmorSpec(Materials.STEEL, 14, ArmorType.HEAVY, 40)
        self.assertEqual(armor1, armor2)

    def test_lt_armor(self):
        armor1 = ArmorSpec(Materials.STEEL, 13, ArmorType.HEAVY, 50)
        armor2 = ArmorSpec(Materials.STEEL, 14, ArmorType.HEAVY, 30)
        armor_ls = [armor1, armor2]
        armor_ls.sort()
        self.assertEqual(armor1, armor2)


class WeaponTest(unittest.TestCase):

    def test_create_weapon(self):
        weapon = TwoHandSword(134.3, 13)
        self.assertEqual(weapon.one_hand, False)

