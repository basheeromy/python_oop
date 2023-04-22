# Create a class called Person with a constructor that initializes the 
# name and age instance variables. Add a method called greet that prints 
# out a greeting message with the person's name.

class Person:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def greeting(self):
        print(f"Hi {self.name}. welcome..!")
        
        

person1 = Person("Rahul",28)
person1.greeting()