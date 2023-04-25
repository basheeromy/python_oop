# Write a Python program to convert JSON data to Python object. 
# Creating json file from python object is called serialization

import json 

student = {"name":"Shaheer","age":25,"present":True,"subjects":["sociology","journalism","computer application","communicative english"]}

studentJSON = json.dumps(student, indent=4,sort_keys = True)

# create json file from python dictionary
with open ('student.json','w') as file:
    json.dump(student, file, indent=4, sort_keys=True)
    
    
# create python dict from json string

student1 = json.loads(studentJSON)
print(student1)

# create python dict from json file, to do it, we have to open file first

with open('student.json','r') as file:
    student2 = json.load(file)
    print(f"for file : {student2}")