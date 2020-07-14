"""
Testing file for Question 5 of Interview Prac 2

__author__  = "Maria Garcia de la Banda"
__edited__  = "Ben Di Stefano"
__edited_by_student__ = 'Derek Anyanwu'

"""

import unittest
from army import Archer, Soldier, Cavalry, Army
from battle import Battle


class TestTask5(unittest.TestCase):

    def setUp(self):
        self.verificationErrors = []

    def tearDown(self):
        for item in self.verificationErrors:
            print(item)
        print("Number of Errors = "+str(len(self.verificationErrors)))

    def test__conduct_combat(self):
        t1 = Army()
        t2 = Army()
        t3 = Army()
        t4 = Army()
        battle = Battle()
        formation = 1

        # Test if combat is conducted correctly and if it returns
        # appropriate result for all Archer p1 army and empty p2 army
        # Assumes __assign_army is working correctly
        t1._Army__assign_army("", 0, 10, 0, formation)
        t2._Army__assign_army("", 0, 0, 0, formation)
        t3._Army__assign_army("", 0, 4, 0, formation)
        t4._Army__assign_army("", 0, 0, 0, formation)

        try:
            self.assertTrue(battle._Battle__conduct_combat(t1, t2, formation) == 1, "Fairer 0,10,0 0,0,0 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Tests combat is conducted correctly and if it
        # returns appropriate result for 1 Soldier p1 army and 1 Archer p2 army
        # Assumes __assign_army is working correctly
        t1._Army__assign_army("", 1, 0, 0, formation)
        t2._Army__assign_army("", 0, 1, 0, formation)
        try:
            self.assertTrue(battle._Battle__conduct_combat(t1, t2, formation) == 0, "Fairer 1,0,0 0,1,0 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertEqual(str(t1.force), "", msg="Army 1 wrong for Fairer 1,0,0 0,1,0")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        try:
            self.assertEqual(str(t2.force), "", msg="Army 2 wrong for Fairer 1,0,0 0")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Checking if t1 is an instance of Army
        try:
            self.assertEqual(isinstance(t3, Army), True, msg="Object is not an instance of Army")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Testing __conduct_combat method
        try:
            self.assertTrue(battle._Battle__conduct_combat(t3, t4, formation) == 1, "Fairer 0,4,0 0,0,0 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))



if __name__ == '__main__':
  unittest.main()
