class Vehicle:
    def __init__(self,variant,making_month,seat_capacity,length,price):
        self.variant = variant
        self.making_month = making_month
        self.seating = seat_capacity
        self.length = length
        self.price = price 
        
    def segment(self):
        if self.price < 1500000 and self.seating < 6:
            if self.length < 4000:
                return("Hatch-back")
            else:
                return("Sedan") 
        elif self.price > 1500000 and self.seating > 6:
            return ("MPV")
        elif self.price > 1500000 and self.seating < 6:
            return ("SUV")
        
    def discount(self):
        disc = (self.price /100) * 13
        return disc
    
Alto = Vehicle("z+","january",5,3700,600000)
Harrier = Vehicle("z","june",5,4600,2500000)
Innova = Vehicle("xz+","august",7,4800,2800000)
City = Vehicle("s+","june",5,4100,1400000)
innova = Innova.segment()
harrier = Harrier.segment()
city = City.segment()
alto  = Alto.segment()
print(f"Innova is a {innova}")
print(f"Harrier is a {harrier}")
print(f"City is a {city}")
print(f"Alto is a {alto}")
