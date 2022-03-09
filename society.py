import random
import uuid
import json
import requests


class Person:
    def __init__(self, ID, sex, age, home, income, outcome, family, lifestyle, confidence):
        self.ID = ID
        
        if type(sex) == int and 0 < sex < 3:
            self.sex = sex
        else:
            self.sex = random.randint(1,2)
            
        if type(age) == int:
            self.age = age
        else:
            self.age = random.randint(1, 99)
            
        if type(home) == int and 0 < home < 3:
            self.home = home
        else:
            self.home = random.randint(1,2)
        
        if type(income) == int and 0 < income < 4:
            self.income = income
        else:
            self.income = random.randint(1,3)
            
        if type(outcome) == int and 0 < outcome < 4:
            self.outcome = outcome
        else:
            self.outcome = random.randint(1,3)        
            
        if type(family) == int:
            self.family = family
        else:
            self.family = random.randint(1,5)
            
        if type(lifestyle) == int and 0 < lifestyle < 4:
            self.lifestyle = lifestyle
        else:
            self.lifestyle = random.randint(1,3)
            
        if type(confidence) == int and 0 < confidence < 4:
            self.confidence = confidence
        else:
            self.confidence = random.randint(1,3)
            
        if sex == 1:
            self.sex = "female"
        else:
            self.sex = "male"
            
        if home == 1:
            home = "city"
        else:
            home = "village"
            
        if income == 1:
            self.income = "poor"
        elif income == 2:
            self.income = "average"
        else:
            self.income = "rich"
            
        if outcome == 1:
            self.outcome = "economy"
        elif outcome == 2:
            self.outcome = "normal"
        else:
            self.outcome = "overdraft" 
            
            
    def stats(self, ID, sex, age, home, income, outcome, family, lifestyle, confidence):
        return(self.ID, self.sex, self.age, self.home, self.income, self.outcome, self.family, self.lifestyle, self.confidence)
        
        
        
pers = Person(1234, 1, 2, 4, 5, 6, 7, 8, 9)
print(pers.stats())