"""
Testing file for Question 3 of Interview Prac 2

__author__  = "Maria Garcia de la Banda"
__edited__  = "Ben Di Stefano"
__edited_by_student__ = 'Derek Anyanwu'

"""

import unittest
from army import Archer, Soldier, Cavalry, Army
from battle import Battle

class TestTask3(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.MaxDiff = None

    def tearDown(self):
        for item in self.verificationErrors:
            print(item)
        print("Number of Errors = "+str(len(self.verificationErrors)))

    def test__correct_army_given(self):
        t1 = Army()

        # Test if a (low) valid combination of unit values is accepted
        try:
            self.assertTrue(t1._Army__correct_army_given(1,1,1), msg = "Stack test 1,1,1 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # put your __correct_army tests here
        # simple test
        try:
            self.assertEqual(t1._Army__correct_army_given(1, 1, 1), True, msg = "correct_army method failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Testing for negative inputs
        try:
            self.assertEqual(t1._Army__correct_army_given(-1, -1, 1), False, msg = "correct_army method failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # testing for over the budget inputs
        try:
            self.assertEqual(t1._Army__correct_army_given(21, 41, 1), False, msg = "correct_army method failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))


    def test__str__(self):
        sold = "Soldier's life = 3 and experience = 0"
        arch = "Archer's life = 3 and experience = 0"
        cav = "Cavalry's life = 4 and experience = 0"
        t1 = Army()
        t2 = Army()
        t3 = Army()

        # Test if the string representation of the army matches expected output for low unit values
        t1._Army__assign_army("t1", 1, 1, 1, 0)
        t2._Army__assign_army("t2", 0, 1, 0, 0)
        t3._Army__assign_army("t1", 0, 0, 0, 0)

        try:
            self.assertEqual(str(t1.force), sold+","+arch+","+cav, msg = "String test 1,1,1 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        #  __str__ tests : testing 0 1 0
        try:
            self.assertEqual(str(t2.force), "Archer's life = 3 and experience = 0", msg="str method failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        #  __str__ tests : testing 0 0 0
        try:
            self.assertEqual(str(t3.force), "", msg = "str method failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

if __name__ == '__main__':
    unittest.main()
