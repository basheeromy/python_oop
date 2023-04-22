# Create a class called Rectangle with a constructor that initializes
# the width and height instance variables. Add a method called area
# that returns the area of the rectangle.

class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        
    def area(self):
        area = self.width * self.height
        return(f"Area is : {area} sqm")
        
        
width = int(input("Enter the height : "))     
height = int(input("Enter the width : "))
        
room = Rectangle(width,height)
print(Rectangle.area(room))
