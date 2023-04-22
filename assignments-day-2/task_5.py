# Create a class called Car with a constructor that initializes the 
# make and model instance variables. Add a method called start that 
# prints out a message with the car's starting sound. Create a subclass 
# called ElectricCar that overrides the start method to print out a 
# different message.

class Car:
    def __init__(self,make,model):
        self.make = make
        self.model = model 
        
    def start(self):
        print("Car started.. ### ")
        
class ElectricCar(Car):
    def start(self):
        print("Electric cars are silent... ")
        

ev = ElectricCar(2022,"tata nexon")
ev.start()