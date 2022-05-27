class Fruit:
    def __init__(self, type, color,size):
        self.type = type
        self.color =color
        self.size=size
        
        
# Class methods - are used to definethe behaviour of objects. They are defined as functions inside the class. The first argument of a class is always self.


class Student:
    school='AkiraChix'
    def __init__(self,name,country,age,school):
        self.name=name
        self.country=country
        self.age=age
        self.school=school 
    def greeting(self):
     return f"Hello { self.name} age {self.age} from {self.country } welcome to {self.school}"
    def full_name(self):
        return f"Hello {self.name} your full names are {self.firstName} {self.secondName}"
        