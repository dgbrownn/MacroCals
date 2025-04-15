import unittest
from MacroCalorieCalculator import Calories as cals

class CaloriesTesting(unittest.TestCase):

    def test_sanity(self):
        self.assertEqual(1 + 1, 2)

    def setUp(self):
        '''
        Create sample object to use in tests
        '''
        self.mc = cals('maintain weight', 70, 180, 'male', 25, 'active')

    def test_isInteger(self):
        '''
        Test attributes requiring integer values
        '''
        self.assertIsInstance(self.mc.get_height(), int, "Is an Integer")
        self.assertIsInstance(self.mc.get_weight(), int, "Is an Integer")
        self.assertIsInstance(self.mc.get_age(), int, "Is an Integer")

    def test_isString(self):
        '''
        Test attributes requiring string values
        '''
        self.assertIsInstance(self.mc.get_activity_lvl(), str, "Is a string")
        self.assertIsInstance(self.mc.get_gender(), str, "Is a string")
        self.assertIsInstance(self.mc.get_goal(), str, "Is a string")
    
    def test_maintcals(self):
        '''
        Test maintenance calorie calculation ensuring calculation is as expected
        '''
        bmr = self.mc.basal_metabolic_rate()
        expected_maint_cals = round(bmr * 1.55, 2)
        self.assertEqual(self.mc.set_maintenance_cals(), expected_maint_cals)
    
    def test_deficits(self):
        '''
        Test each deficit to ensure calculation is as expected
        '''
        maint_cals = self.mc.set_maintenance_cals()
        expected_active_def = round(maint_cals - 300, 2)
        expected_moderate_def = round(maint_cals - 500, 2)
        expected_sedentary_def = round(maint_cals - 800, 2)
        self.assertEqual(self.mc.active_deficit(), expected_active_def)
        self.assertEqual(self.mc.moderate_deficit(), expected_moderate_def)
        self.assertEqual(self.mc.sedentary_deficit(), expected_sedentary_def)
    
    def test_surplus(self):
        '''
        Test each surplus to ensure calculation is as expected
        '''
        maint_cals = self.mc.set_maintenance_cals()
        expected_active_surplus = round(maint_cals + 800, 2)
        expected_moderate_surplus = round(maint_cals + 500, 2)
        expected_sedentary_surplus = round(maint_cals + 300, 2)
        self.assertEqual(self.mc.active_surplus(), expected_active_surplus)
        self.assertEqual(self.mc.moderate_surplus(), expected_moderate_surplus)
        self.assertEqual(self.mc.sedentary_surplus(), expected_sedentary_surplus)

    def test_macros(self):
        '''
        Test each macronutrient calculation to ensure accuracy
        '''
        maint_cals = self.mc.set_maintenance_cals()
        expected_fats = round((maint_cals * .3 / 4), 2)
        expected_carbs = round((maint_cals * .45 / 4), 2)
        expected_protein = round((maint_cals * .45 / 4), 2)
        self.assertEqual(self.mc.fats(), expected_fats)
        self.assertEqual(self.mc.carbohydrates(), expected_carbs)
        self.assertEqual(self.mc.protein(), expected_protein)
