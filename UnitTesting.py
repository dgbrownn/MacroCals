import unittest
import MacroCalorieCalculator as mc

class test_getters(unittest.TestCase):
    def isInteger(self):
        self.assertIsInstance(mc.get_height(5), "Is an Integer")
        self.assertIsInstance(mc.get_weight(5), "Is an Integer")
        self.assertIsInstance(mc.get_age(5), "Is an Integer")
        self.assertNotIsInstance(mc.get_age('str'), "Entry contained a string, not an integer\nPlease try again.")
    def isnotZero(self):
        self.assertEqual(mc.get_height(0), "Is Zero, not a valid entry")


if __name__ == "__main__":
    unittest.main(verbosity=1)