# Inheritance
# Inheritance allows us to define a class that inherits all the methods 
# and properties from another class.

# Parent class is the class being inherited from, also called base class or super class. represented by super keyword
# Child class is the class that inherits from another class, also called derived class.

class Employee:
    raise_percent = 1.04
    bonus = 1.05
    
    def __init__(self,fname,lname,pay,mob):
        self.fname = fname 
        self.lname = lname
        self.pay = pay
        self.mobile = mob
        
    def full_name(self):
        return f"{self.fname} {self.lname}"
    
    def e_mail(self):
        return f"{self.fname} {self.lname}@company.com"
    
    # we can access class variables in regular method using self keyword, 
    # see apply_bonus() function
    
    def apply_bonus(self):
        self.pay *= self.bonus
    
    
    def apply_raise(self):
        self.pay *= self.raise_percent
    

# create child classes Manager and Developer from employee class

class Developer(Employee):
    
    raise_percent = 1.10
    bonus = 1.10
    def __init__(self,fname,lname,pay,mob,prog_lang):
        super().__init__(fname,lname,pay,mob)
        
        # when we have multiple inheritance, we can use the following techinque instead of using super()
       #Employee.__init__(self,fname,lname,pay,mob)
        self.prog_lang = prog_lang
    
class Manager(Employee):
    
    raise_percent = 1.10
    bonus = 1.10
    def __init__(self,fname,lname,pay,mob,employees=None):
        super().__init__(fname,lname,pay,mob)
        
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    def add_employee(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_employee(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
            
    def list_of_employees(self):
        for i in self.employees:
            print('-->',f"{i.full_name()}")

# print full name and email of developer 
developer1 = Developer("muhammed","basheer",50000,9847313208,"Python")
security1 = Employee("shafeek","ahammed",20000,9832876542)
developer2 = Developer("akhil","mohan",50000,7638492839,"Java")

manager1 = Manager("Rahul","raj",60000,6537864532,[developer1])
#manager1.list_of_employees()
manager1.add_employee(developer2)
manager1.add_employee(security1)
#manager1.list_of_employees()
manager1.remove_employee(security1)
manager1.list_of_employees()
# security1.apply_raise()
# print(security1.pay)

# developer1.apply_raise()
# print(developer1.pay)

# developer1.apply_bonus()
# print(developer1.pay)
# print(developer1.full_name())
# print(developer1.e_mail())
# print(developer1.prog_lang)