# Inheritance
# Inheritance allows us to define a class that inherits all the methods 
# and properties from another class.

# Parent class is the class being inherited from, also called base class or super class. represented by super keyword
# Child class is the class that inherits from another class, also called derived class.

class Employee:
    def __init__(self,fname,lname,pay,mob):
        self.fname = fname 
        self.lname = lname
        self.pay = pay
        self.mobile = mob
        
    def full_name(self):
        return f"{self.fname} {self.lname}"
    
    def e_mail(self):
        return f"{self.fname} {self.lname}@company.com"
    

# create child classes Manager and Developer from employee class

class Manager(Employee):
    pass
    

# print full name and email of manager 
manager1 = Manager("muhammed","basheer",50000,9847313208)
print(manager1.full_name())
print(manager1.e_mail())