"""
Testing file for Question 2 of Interview Prac 2

__author__  = 'Derek Anyanwu'
__author__  = "Maria Garcia de la Banda"
__edited__  = "Ben Di Stefano"

"""

import unittest
from army import Archer, Soldier, Cavalry


class TestTask2(unittest.TestCase):

    def setUp(self):
        """ The 'setUp' method is a frequently used method in unittest, and is called BEFORE every test case is run.
    This is useful when you want to create certain conditions before running a series of tests, without having to
    repeat code within those tests. Used in conjuction with tearDown to help ensure the test is isolated from
    the performance of other tests.

    Here it's just creating storage for any potential raised errors in the tests."""
        self.verificationErrors = []

    def tearDown(self):
        """ The 'tearDown' is another frequently used method in unittest, and is called AFTER every test case is run.
    This is useful when you want to delete created instances or do other required tasks,
    without having to repeat code within those tests. Used in conjuction with setUp to help
    ensure the test is isolated from the performance of other tests.

    Here it's just printing off the errors that may have been stored in our list of errors, as well as the total number
    of errors.
    """
        for item in self.verificationErrors:
            print(item)
        print("Number of Errors = " + str(len(self.verificationErrors)))

    def test_Soldier(self):
        t1 = Soldier()

        # Test if Soldier properties correctly initialised
        try:
            self.assertEqual(str(t1), "Soldier's life = 3 and experience = 0", msg="Soldier not created correctly")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test Soldier attack damage
        try:
            self.assertEqual(t1.attack_damage(), 1, msg="Soldier attack damage not correct")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test Soldier Defend methods
        try:
            t1.defend(3)
            self.assertEqual(t1.life, 2, msg="Soldier defend method is not working properly")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Checking if t is an instance of Soldier
        try:
            self.assertEqual(isinstance(t1, Soldier), True, msg="Object is not an instance of Soldier")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_Archer(self):
        t1 = Archer()

        # Test if Archer properties correctly initialised
        try:
            self.assertEqual(str(t1), "Archer's life = 3 and experience = 0", msg="Archer not created correctly")
        except AssertionError as e:
            self.verificationErrors.append(str(e))


        # Test Archer attack damage
        try:
            self.assertEqual(t1.attack_damage(), 1, msg="Archer attack damage not correct")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test Archer Defend methods
        try:
            t1.defend(2)
            self.assertEqual(t1.life, 2, msg="Archer defend method is not working properly")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Checking if t is an instance of Archer
        try:
            self.assertEqual(isinstance(t1, Archer), True, msg="Object is not an instance of Archer")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_Cavalry(self):
        t1 = Cavalry()

        # Test if Cavalry properties correctly initialised
        try:
            self.assertEqual(str(t1), "Cavalry's life = 4 and experience = 0", msg="Cavalry not created correctly")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test Cavalry attack damage
        try:
            self.assertEqual(t1.attack_damage(), 1, msg="Cavalry attack damage not correct")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test Cavalry Defend methods
        try:
            t1.defend(2)
            self.assertEqual(t1.life, 3, msg="Cavalry defend method is not working properly")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Checking if t is an instance of Cavalry
        try:
            self.assertEqual(isinstance(t1, Cavalry), True, msg="Object is not an instance of Cavalry")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_is_alive_lose_life(self):

        s = Soldier()
        # Test if Soldier created alive
        try:
            self.assertTrue(s.is_alive(), msg="Soldier not created alive")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test if Soldier stays alive after losing only a small amount of life
        s.lose_life(1)
        try:
            self.assertTrue(s.is_alive(), msg="Soldier lost too much life")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        a = Archer()
        # Test if Archer created alive
        try:
            self.assertTrue(a.is_alive(), msg="Archer not created alive")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test if Archer stays alive after losing only a small amount of life
        a.lose_life(1)
        try:
            self.assertTrue(a.is_alive(), msg="Archer lost too much life")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        c = Cavalry()
        # Test if Cavalry created alive
        try:
            self.assertTrue(c.is_alive(), msg="Cavalry not created alive")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test if Cavalry stays alive after losing only a small amount of life
        c.lose_life(1)
        try:
            self.assertTrue(c.is_alive(), msg="Cavalry lost too much life")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_gain_experience_get_experience(self):

        s = Soldier()

        # Test if Soldier experience gain is updated correctly
        s.gain_experience(3)
        try:
            self.assertTrue(s.get_experience() == 3, msg="Soldier's experience incorrect")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test if speed is updated correctly for Soldier upon gaining experience
        try:
            self.assertTrue(s.get_speed() == 4, msg="Soldier's speed not correct" + str(s))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test if pre-condition is enforced correctly (negative experience gain raises exception)
        with self.assertRaises(Exception, msg="Soldier's gain_experience should have raised exception"):
            s.gain_experience(-3)

        a = Archer()

        # Test if Archer experience gain is updated correctly
        a.gain_experience(3)
        try:
            self.assertTrue(a.get_experience() == 3, msg="Archer's experience incorrect")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test if speed is updated correctly for Archer upon gaining experience
        try:
            self.assertTrue(a.get_speed() == 3, msg="Archer's speed not correct")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test if pre-condition is enforced correctly (negative experience gain raises exception)
        with self.assertRaises(Exception, msg="Archer's gain_experience should have raised exception"):
            a.gain_experience(-3)

        c = Cavalry()

        # Test if Archer experience gain is updated correctly
        c.gain_experience(3)
        try:
            self.assertTrue(c.get_experience() == 3, msg="Cavalry's experience incorrect")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test if speed is updated correctly for Archer upon gaining experience
        try:
            self.assertTrue(c.get_speed() == 2, msg="Cavalry's speed not correct")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test if pre-condition is enforced correctly (negative experience gain raises exception)
        with self.assertRaises(Exception, msg="Cavalry's gain_experience should have raised exception"):
            c.gain_experience(-3)


if __name__ == '__main__':
    unittest.main()
