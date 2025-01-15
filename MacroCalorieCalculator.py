class Calories:

    def __init__(self, ht, wt, gender, activity_lvl):
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
       self.height = ht
       self.weight = wt
       self.activity_lvl = activity_lvl
       self.gender = gender
       self.maint_cals = self.set_maintenance_cals()
       self.sed_def = self.sedentary_deficit()
       self.fts = self.fats()
       self.ptn = self.protein()
       self.carbs = self.carbohydrates()

    def set_height(self, ht):
        '''
        Sets user's height based on created object
        :param ht: User's height. Must not be zero.
        :return: self.height (User's height param)
        '''
        if self.height != 0:
            self.height = ht
        if not isinstance(ht, int):
            raise TypeError(f'Invalid, enter height in inches')
        return self.height

    def get_height(self):
        return self.height

    def set_weight(self, wt):
        if self.weight != 0:
            self.weight = wt
        if not isinstance(wt, int):
            raise TypeError(f'Invalid, enter weight to the nearest pound')
        return self.weight

    def get_weight(self):
        return self.weight

    def set_gender(self, gender):
        valid = ['male', 'female']
        if not isinstance(gender, str):
            raise TypeError
        for i in valid:
            if gender.lower() != i:
                raise ValueError('Male or Female')
        return self.gender

    def get_gender(self):
        return self.gender

    def set_activity_level(self, activity_lvl):
        valid = ['sedentary', 'moderate', 'active']
        if not isinstance(activity_lvl, str):
            raise TypeError
        for i in valid:
            if activity_lvl.lower() != i:
                raise ValueError(f'Please select between sedentary, moderate, and active')
        return self.activity_lvl

    def get_activity_level(self):
        return self.activity_lvl

    def set_maintenance_cals(self):
        if self.weight != 0:
            self.maint_cals = self.weight * 15
        return self.maint_cals

    def active_deficit(self):
        if self.activity_lvl == 'active':
            if self.maint_cals != 0:
                self.active_def = self.maint_cals - 300
            return (f'For a caloric deficit while being active\n (exercise 5-6 times per week), '
                    f'your daily intake should be {self.active_def} calories.')

    def moderate_deficit(self):
        if self.activity_lvl == 'moderate':
            if self.maint_cals != 0:
                self.mod_def = self.maint_cals - 500
            return (f'For a caloric deficit while being moderately active\n (exercise 3-5 times per week), '
                    f'your daily intake should be {self.mod_def} calories')

    def sedentary_deficit(self):
        if self.activity_lvl == 'sedentary':
            if self.maint_cals != 0:
                self.sed_def = self.maint_cals - 800
            return (f'For a caloric deficit while being sedentary\nyour daily intake should be {self.sed_def} calories')
        
    def fats(self):
        return int(self.weight * .4)
    
    def protein(self):
        return int(self.weight)
    
    def carbohydrates(self):
        return int(self.weight * 2)
        
    def __str__(self):
        return f'Maint cals: {self.maint_cals}\n{self.sed_def}\nFats: {self.fts}\nCarbs: {self.carbs}\nProtein: {self.ptn}'


if __name__ == '__main__':
    c = Calories(62, 260, 'male', 'sedentary')
    print(c)