# Class Methods
# class method uses @classmethod decorator to flag it as a class method.
# Instead of accepting a self parameter, class methods take a cls parameter 
# that points to the class—and not the object instance—when the method is called.

# Because the class method only has access to this cls argument, it can’t modify 
# object instance state. That would require access to self. However, class methods 
# can still modify class state that applies across all instances of the class.

# we can use inbuilt classmethod() function to create a class method

class Students:
    count = 0
        
    def print_count(self,count):
        self.count = count
        print(f"Number of students is : {count}")
        
Students.print_number = classmethod(Students.print_count)

Students.print_number(33)

print(f"Class variable count has a value of : {Students.count}")

""" 
    In this way, when we are using built in classmethod() to create class method, we are actually creating 
    a regular method to purpose fully to use as a class method later and converting that regular method to 
    static method using classmethod() function, the self key word will automatically change as cls
"""


# let's try the same with another example

class Cars:
    count = 0
    
    def increment_count(self,count):
        self.count += count
        
    def print_count(self):
        print(f"number of cars is : {Cars.count}")
        

Cars.add_count = classmethod(Cars.increment_count)
Cars.add_count(260)

alto = Cars()
alto.print_count()

# Class method with decorator @classmethod
# This way of creating class method is more pythonic

class Student:
    count = 0
    name = "School 1"
    mail = "school@campus.com"
    contact = "0495 812 3945"
    def __init__(self,name,subject):
        self.name = name
        self.subject = subject
        Student.count += 1
    # Alternative constructor created using class method
    @classmethod
    def from_string(cls,string):
        name,subject = string.split(",")
        return cls(name,subject)
        
    
    # we can create a classmethod using decorator like follows, cls used to refer class as first variable.
    @classmethod
    def print_school_details(cls):
        print(f"School name: {cls.name}, E mail : {cls.mail}, Contact : {cls.contact},Number of students : {cls.count}")
    
    
student_1 = Student("jishnu","science")

# we can access class method through object
student_1.print_school_details()

# Acess class object through class itself

student_2 = Student("Risham","science")

Student.print_school_details()


student_3 = Student.from_string("Shafeek,science")
student_1.print_school_details()
print(student_3.name)