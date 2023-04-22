# Static Methods
# static methods uses @staticmethod decorator to flag it as a static method.

# This type of method takes neither a self nor a cls parameter (but of course
# it’s free to accept an arbitrary number of other parameters).

# Therefore a static method can neither modify object state nor class state. 
# Static methods are restricted in what data they can access - and they’re 
# primarily a way to namespace your methods.

class School:
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True 
    
import datetime

my_time = datetime.date(2023,4,22)

print(School.is_workday(my_time))