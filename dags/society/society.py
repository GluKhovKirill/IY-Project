import random
import json


class Person:
    def __init__(self, ID, sex, age, home, income, outcome, budget, family, lifestyle, confidence):
        self.ID = ID
        
        if type(sex) == int and 0 < sex < 3:
            self.sex = sex
        else:
            self.sex = sex
            self.sex = random.randint(1,2)
            
        if type(age) == int:
            self.age = age
        else:
            self.age = age
            self.age = random.randint(1, 99)
            
        if type(home) == int and 0 < home < 3:
            self.home = home
        else:
            self.home = home
            self.home = random.randint(1,2)
        
        if type(income) == int and 0 < income < 4:
            self.income = income
        else:
            self.income = income
            self.income = random.randint(1,3)
        
        if type(outcome) == int and 0 < outcome < 4:
            self.outcome = outcome
        else:
            self.outcome = outcome
            self.outcome = random.randint(1,3)        
            
        if type(budget) == int and 0 < budget < 4:
            self.budget = budget
        else:
            self.budget= budget
            self.budget = random.randint(1,3)        
            
        if type(family) == int:
            self.family = family
        else:
            self.family = family
            self.family = random.randint(1,5)
            
        if type(lifestyle) == int and 0 < lifestyle < 4:
            self.lifestyle = lifestyle
        else:
            self.lifestyle = lifestyle
            self.lifestyle = random.randint(1,3)
            
        if type(confidence) == int and 0 < confidence < 4:
            self.confidence = confidence
        else:
            self.confidence = confidence
            self.confidence = random.randint(1,3)
            
        if self.sex == 1:
            self.sex = "female"
        else:
            self.sex = "male"
            
        if self.home == 1:
            self.home = "city"
        else:
            self.home = "village"
            
        if self.income == 1:
            self.income = random.randint(15000, 35000)
        elif self.income == 2:
            self.income = random.randint(50000, 80000)
        else:
            self.income = random.randint(100000, 200000)
            
        if self.outcome == 1:
            self.outcome = "economy"
        elif self.outcome == 2:
            self.outcome = "normal"
        else:
            self.outcome = "overdraft"
            
        if self.budget == 1:
            self.budget = random.randint(12000, 30000)
        elif self.budget == 2:
            self.budget = random.randint(31000, 80000)
        else:
            self.budget = random.randint(81000, 150000)     
            
        if self.lifestyle == 1:
            self.lifestyle = "healthy"
        elif self.lifestyle == 2:
            self.lifestyle = "moderate"
        else:
            self.lifestyle = "unhealthy"
            
        if self.confidence == 1:
            self.confidence = "unconfident"
        elif self.confidence == 2:
            self.confidence = "somewhat confident"
        else:
            self.confidence = "very confident"        
            
            
    def stats(self):
        test_dict= self.__dict__
        test_json = json.dumps(test_dict)        
        return test_json

    def salary(self):
        self.budget += self.income
        
        
        
pers1 = Person(1234, 1, 43, 34, 1, 1, 1, 1, 1, 45)
pers2 = Person(1234, 1, 46, 34, 1, 1, 1, 1, 1, 45)
print(pers1.stats())
pers1.salary()
print(pers1.stats())