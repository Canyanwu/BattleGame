"""
Testing file for Question 4 of Interview Prac 2

__author__  = 'Derek Anyanwu'
__author__  = "Maria Garcia de la Banda"
__edited__  = "Ben Di Stefano"
"""

import unittest
from army import Archer, Soldier, Cavalry, Army
from battle import Battle


class TestTask4(unittest.TestCase):

    def setUp(self):
        self.verificationErrors = []

    def tearDown(self):
        for item in self.verificationErrors:
            print(item)
        print("Number of Errors = "+str(len(self.verificationErrors)))

    def test___conduct_combat(self):
        t1 = Army()
        t2 = Army()
        t3 = Army()
        t4 = Army()
        battle = Battle()
        formation = 0

        # Test if combat is conducted correctly and returns appropriate result for empty p1 army and all Archer p2 army
        # Assumes __assign_army is working correctly
        t1._Army__assign_army("", 0, 0, 0, formation)
        t2._Army__assign_army("", 0, 10, 0, formation)
        t3._Army__assign_army("", 0, 4, 0, formation)
        t4._Army__assign_army("", 0, 0, 0, formation)
        try:
            self.assertTrue(battle._Battle__conduct_combat(t1, t2, formation) == 2, "Gladiatorial 0,0,0 0,10,0 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Checking if t1 is an instance of Army
        try:
            self.assertEqual(isinstance(t1, Army), True, msg="Object is not an instance of Army")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Testing __conduct_combat
        try:
            self.assertTrue(battle._Battle__conduct_combat(t3, t4, formation) == 1, "Gladiatorial 0,4,0 0,0,0 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))


if __name__ == '__main__':
    unittest.main()
