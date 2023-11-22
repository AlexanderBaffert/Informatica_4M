#Baffert Es13
#Classi
class Person:
    def __init__(self,name,age,passport_number,country) -> None:
        
        self.age=age
        self.name=name
        self.passport=Passport(passport_number,country)
        
    def issue_passport(self):        
        return print(f"Passport ID[name:{self.name}, age:{self.age}, country:{self.passport.country}, passport_number:{self.passport.passport_number}]")
class Passport:
    
    def __init__(self,passport_number,country) -> None:
        self.country=country
        self.passport_number=passport_number

#main
user1 = Person("Silvio",18,"YA0008Q93","Austria")
user1.issue_passport()