# Write a Python program for binary search of an ordered list. 

mylist = [0,5,6,8,9,23,24,34,56,78,199,2000]

data = int(input("Enter any number from given array :"))
length = (len(mylist))-1
        
         
def binary_search(mylist,length,data):
    left = 0
    right = length
    find = False
    while (left < right):
        mid = int((left + right)/2)
        if (data == mylist[mid]):
            find = True
            return mid
        elif(data < mylist[mid]):
            right = mid-1
        else:
            left = mid+1
    if find == False:
        return find   
    
print(binary_search(mylist,length,data))