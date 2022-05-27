class Student:
    
    def __init__(self,name,country,age,school,secondName,currentYear):
        self.name=name
        self.country=country
        self.age=age
        self.school=school 
        self.secondName=secondName
        self.currentYear=currentYear
    def greeting(self):
     return f"Hello { self.name} age {self.age} from {self.country } welcome to {self.school}"
    def full_name(self):
        return f"Hello {self.name} your full names are {self.name} {self.secondName}"
    def initials(self):
        return f"Your Initials are {self.name[0]}.{self.secondName[0]}"
    def year_of_birth(self):
        return f"you were born in the year {self.currentYear - self.age}"
    