# Class variable − A variable that is shared by all instances of a class. 
# Class variables are defined within a class but outside any of the class's methods. 
# Class variables are not used as frequently as instance variables are.

class Employee:
    # class variables
    num_employee = 0
    raise_percent = 1.04
    
    def __init__(self,first,last,pay):
        self.first = first 
        self.last = last 
        self.pay = pay
        
        # Change value of class variable num_employee, whenever we create an instance for this class
        # As we want to change class variable, here we are not using self key word , we will use class name
        
        Employee.num_employee += 1
        
    def full_name(self):
        return(f"{self.first} {self.last}")
    
    def email(self):
        return(f"{self.first}{self.last}@company.com")
    
    def apply_raise(self):
        self.pay = self.pay * self.raise_percent
        
        """ here, we used self.raise_amount to access raise amount. even we declared raise_amount as 
         class variable, we can assign different values to that class variable for each instances. 
         when we do so, it will automatically create an instance variable in the same name and we 
         can access it by refering instance name (self) and that value will not be applicable for 
         other instances """
         
        
emp_1 = Employee("muhammed","basheer",100000)
emp_2 = Employee("aswant","sing",80000)

print(emp_1.full_name())
print(Employee.email(emp_2))

# apply raise to employee one 
emp_1.apply_raise()
print(f"salary of emp.1 after raise is : {emp_1.pay}")
print(f"slary of emp.2 without raise is : {emp_2.pay}")

# change raise percentage of employee two only

emp_2.raise_percent = 1.07
emp_2.apply_raise()
print(f"salary of emp.2 after raise is : {emp_2.pay}")

# check class variable value and instance varibale value of raise_percent

print(f"raise_percentage of class variable is : {Employee.raise_percent}")
print(f"raise percentage of instance variable emp.1 is : {emp_1.raise_percent}")
print(f"raise percentage of instance variable emp.2 is : {emp_2.raise_percent}")
# Change value of class variable
Employee.raise_percent = 1.05
print(emp_1.raise_percent)

# Print the number of employees

print(f"Number of employees in this company is {Employee.num_employee}")