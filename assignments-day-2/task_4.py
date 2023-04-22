# 4. Create a class called Animal with a constructor that initializes the name and species instance variables. 
# Add a method called make_sound that prints out a message with the animal's sound. Create two subclasses called 
# Dog and Cat with their own implementations of make_sound.

class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound of the animal : ####*****")
        
        
class Dog(Animal):
    def make_sound(self):
        print("Sound of dog is : bark ")
        
class Cat(Animal):
    def make_sound(self):
        print("Sound of cat is : mewww ")
        
# Test cat
cat = Cat("kitty","cats")
cat.make_sound()
print(cat.name)

# Test Dog
dog = Dog("jimmy","Canis")
dog.make_sound()
print(dog.species)