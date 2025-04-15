class Calories:

    def __init__(self, goal, ht, wt, gender, age, activity_lvl):
       '''
        Init for Calories class
        :param ht: User height (in inches)
        :param wt: User weight (in pounds)
        :param gender: User gender (Male or Female)
        :param activity_lvl: User's activity level (sedentary [1-2 30 mins exercise per week]
        moderate [3-4 30 mins exercise per week], active [5+ 30 mins exercise per week]).
        - maint_cals: User's calculated maintenance calories (daily
        calorie intake to maintain bodyweight) called from function set_maintenance_cals.
        '''
       self.goal = goal
       self.height = ht
       self.weight = wt
       self.activity_lvl = activity_lvl
       self.gender = gender
       self.age = age
       self.maint_cals = self.set_maintenance_cals()
       self.sed_def = self.sedentary_deficit()
       self.fts = self.fats()
       self.ptn = self.protein()
       self.carbs = self.carbohydrates()

    def set_goal(self, goal):
        '''
        Allows a user to set their goals
        If entry is in valid list, return self.goal
        Otherwise, raise ValueError if not in the list
        or TypeError if entry is not a string
        '''
        valid_goal = ['lose weight', 'gain weight', 'maintain weight']
        if self.goal.lower() not in valid_goal:
                raise ValueError(f'Invalid entry, must be from the following choices:\nLose Weight, Gain Weight, or Maintain Weight')
        if not isinstance(goal, str):
            raise TypeError(f'Must be a string')
        return self.goal
    
    def get_goal(self):
        '''
        Returns a user's goal
        '''
        return self.goal

    def set_height(self, ht):
        '''
        Sets user's height
        :param ht: User's height. Must not be zero.
        :return: User's height if check passes, raises TypeError if input is not an integer.
        '''
        if not isinstance(ht, int):
            raise TypeError(f'Invalid, enter height in inches')
        if self.height > 0:
            self.height = ht
        return self.height

    def get_height(self):
        '''
        Gets user's height
        '''
        return self.height

    def set_weight(self, wt):
        '''
        Sets user's weight
        :param wt: User's weight. Must not be zero
        :return: User's weight if check passes, raises TypeError if input is not an integer.
        '''
        if not isinstance(wt, int):
            raise TypeError(f'Invalid, enter weight to the nearest pound')
        if self.weight > 0:
            self.weight = wt
        return self.weight

    def get_weight(self):
        '''
        Gets user's height
        '''
        return self.weight

    def set_gender(self, gender):
        '''
        :param gender: User's gender, must be a string and within the list 'valid'
        Sets a user's gender if the user's input is within the list of valid gender options (male or female)
        If user's input is not a valid option, raises ValueError
        '''
        valid_gender = ['male', 'female']
        if not isinstance(gender, str):
            raise TypeError
        if gender.lower() not in valid_gender:
            raise ValueError('Male or Female')
        self.gender = gender
        return self.gender

    def get_gender(self):
        '''
        Gets/returns user's gender
        '''
        return self.gender

    def set_age(self, age):
        '''
        :param age: User's age
        Sets user's age if value is not 0 and is an integer
        '''
        if not isinstance(age, int):
            raise TypeError('Must be a number')
        if age > 0:
            self.age = age
        return self.age

    def get_age(self):
        '''
        Gets/returns user's age
        '''
        return self.age

    def set_activity_level(self, activity_lvl):
        '''
        Sets a user's activity level if it is a valid option and of type string
        valid = list of valid options for activity level
        '''
        valid_activity_level = ['sedentary', 'moderate', 'active']
        if not isinstance(activity_lvl, str):
            raise TypeError
        if activity_lvl.lower() not in valid_activity_level:
            raise ValueError(f'Please select between sedentary, moderate, and active')
        return self.activity_lvl

    def get_activity_level(self):
        '''
        Returns a user's activity level
        '''
        return self.activity_lvl

    def basal_metabolic_rate(self):
        '''
        Uses Harris-Benedict Formula to calculate a user's basal metabolic ratee (bmr)
        Basal Metabolic Rate - Amount of energy (calories) a person needs to function while at rest
        '''
        if self.gender.lower() == 'female':
            bmr = 655 + (4.35 * self.weight) + (4.7 * self.height) - (4.7 * self.age)
        if self.gender.lower() == 'male':
            bmr = 66 + (6.23 * self.weight) + (12.7 * self.height) - (6.8 * self.age)
        bmr = round(bmr, 2)
        return bmr

    def set_maintenance_cals(self):
        '''
        Calculate's a user's maintenance calories based off their activity level and BMR
        '''
        if not isinstance(self.basal_metabolic_rate(), float):
            raise TypeError
        if self.activity_lvl.lower() == 'active':
            self.maint_cals = self.basal_metabolic_rate() * 1.725
        if self.activity_lvl.lower() == 'moderate':
            self.maint_cals = self.basal_metabolic_rate() * 1.55
        if self.activity_lvl.lower() == 'sedentary':
            self.maint_cals = self.basal_metabolic_rate() * 1.2
        return round(self.maint_cals, 2)
        
    def active_deficit(self):
        '''
        Deficit's based off of activity level. Gradually decreases for each step 'up' in activity
        I.E. Active activity level will require more calroies for a deficit than sedentary 
        '''
        if self.goal.lower() == 'lose weight':
            if self.activity_lvl.lower() == 'active':
                if self.maint_cals != 0:
                    self.active_def = self.maint_cals - 300
                return round(self.active_def, 2)

    def moderate_deficit(self):
        '''
        See active_deficit comment
        '''
        if self.goal.lower() == 'lose weight':
            if self.activity_lvl.lower() == 'moderate':
                if self.maint_cals != 0:
                    self.mod_def = self.maint_cals - 500
                return round(self.mod_def, 2)

    def sedentary_deficit(self):
        '''
        See active_deficit comment
        '''
        if self.goal.lower() == 'lose weight':
            if self.activity_lvl.lower() == 'sedentary':
                if self.maint_cals != 0:
                    self.sed_def = self.maint_cals - 800
                return round(self.sed_def, 2)

    def active_surplus(self):
         '''
        Surpluses based off of activity level. Gradually increases for each step 'up' in activity
        I.E. Active activity level will require more calories for a surplus than sedentary 
        '''
         if self.goal.lower() == 'gain weight':
            if self.activity_lvl.lower() == 'active':
                if self.maint_cals != 0:
                    self.act_surplus = self.maint_cals + 800
                return round(self.act_surplus, 2)

    def moderate_surplus(self):
        '''
        See active_surplus comment
        '''
        if self.goal.lower() == 'gain weight':
            if self.activity_lvl.lower() == 'moderate':
                if self.maint_cals != 0:
                    self.mod_surplus = self.maint_cals + 500
                return round(self.mod_surplus, 2)

    def sedentary_surplus(self):
        '''
        See active_surplus comment
        '''
        if self.goal.lower() == 'gain weight':
            if self.activity_lvl.lower() == 'sedentary':
                if self.maint_cals != 0:
                    self.sed_surplus = self.maint_cals + 300
                return round(self.sed_surplus, 2)

    def fats(self):
        '''
        Calculates fats based off suggested daily calorie intake percentages
        '''
        if self.maint_cals != 0:
            return round(self.maint_cals * .20 / 9, 2)
    
    def protein(self):
        '''
        Calculates protein based off suggested daily calorie intake percentages
        '''
        if self.maint_cals != 0:
            return round((self.maint_cals * .3 / 4), 2)
    
    def carbohydrates(self):
        '''
        Calculates carbohydrates based off suggested daily calorie intake percentages
        '''
        if self.maint_cals != 0:
            return round(self.maint_cals * .45 / 4, 2)
        
    def __str__(self):
        '''
        Temporary str method for displaying output
        '''
        deficit = ''
        surplus = ''
        if self.goal.lower() == 'lose weight':
            if self.activity_lvl.lower() == 'active':
                deficit = self.active_deficit()
            if self.activity_lvl.lower() == 'moderate':
                deficit = self.moderate_deficit()
            if self.activity_lvl.lower() == 'sedentary':
                deficit = self.sedentary_deficit()
            return f'Maintenance calories: {self.maint_cals} kcal\nDeficit Calories: {deficit} kcal\nFats: {self.fts}g\nCarbs: {self.carbs}g\nProtein: {self.ptn}g'
        elif self.goal.lower() == 'gain weight':
            if self.activity_lvl.lower() == 'active':
                surplus = self.active_surplus()
            if self.activity_lvl.lower() == 'moderate':
                surplus = self.moderate_surplus()
            if self.activity_lvl.lower() == 'sedentary':
                surplus = self.sedentary_surplus()
            return f'Maintenance Calories: {self.maint_cals} kcal\nSurplus Calroies: {surplus} kcal\nFats: {self.fts}g\nCarbs: {self.carbs}g\nProtein: {self.ptn}g'
        elif self.goal.lower() == 'maintain weight':
            return f'Maintenance Calories: {self.maint_cals} kcal\nFats: {self.fts}g\nCarbs: {self.carbs}g\nProtein: {self.ptn}g'


if __name__ == '__main__':
    c = Calories('maintain weight', 60, 200, 'male', 20, 'active')
    print(c.__str__())
    