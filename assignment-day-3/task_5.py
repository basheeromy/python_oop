
# Write a Python program to generate and print a list of the first and 
# last 5 elements where the values are square numbers between 1 and 30 
# (both included).

# create list of square numbers between 1 and 30 
limit = 30
value = 1
list1 = []
while (value*value) < limit:
    number = value * value
    value += 1
    list1.append(number)
    
print(f"first 5 elements of square numbers in between 1 and {limit} are : {list1[:5]} and last 5 elements are : {list1[-5:]}")