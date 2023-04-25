# Write a Python program to find all the unique words and count the frequency 
# of occurrence from a given list of strings. Use Python set data type. 

mylist = ["catch","put","put","shoot","one","two","two","one","one"]
myset = set(mylist)
mydict = {}
for i in myset:
    count = 0
    for j in mylist:
        if i == j:
            count += 1
    mydict[i] = count
    
    #print(f"Number of {i} in list is {count}")
    
    
    
print(f"unique elements are {myset}")
print(f"Frequency of elements in list : {mydict}")