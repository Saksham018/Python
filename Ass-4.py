#QUSETION 1
list1=[1,23,45,67,86,44]
print(list1[::-1])

#Question 2
string="Hello I Am Learning Python"
for i in string:
    if(i.isupper()):
        print(i)

#Question 3
user=input("Enter the elements: ")
s=user.split(',')
list2=[]
for i in s:
    list2.append(int(i))
print(list2)

#Quetsion 4
str1 = input("Enter to check: ")
str=str1[::-1]
if(str==str1):
    print("Palidrome")
else:
    print("Not palidrome")

#Qusetion 5
import copy as c
list1=[1,2,3,[4,5],6]
l1=c.deepcopy(list1)
l1[3][0]=3
print(list1)
print(l1)
#Diff in shallow copy and deep copy
#A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original.
#A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.