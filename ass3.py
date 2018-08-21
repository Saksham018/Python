#Question 1

list=[]
size=int(input("Enter the size of list"))
for i in range(0,size):
    a=input("enter you want to insert")
    list.append(a)
print(list)

#Qusetion 2
list2=['google','apple','facebook','microsoft','tesla']
list.extend(list2)
print(list)

#Question 3
num=input("Enter the object you want to count from list: ")
print(list.count(num))

#Qusetion 4
list3=[1,3,56,78,44,78,97,355,9007,333,3]
list3.sort()
print(list3)

#Question 5
list4=[1,2,34,56,78,65]
list5=[3,22,66,88,00]
list4.extend(list5)
list4.sort()
print(list4)

#Question 6
odd=0
even=0
for i in list4:
    if(i%2==0):
        even=even+1
else:
    odd=odd+1
print("NUMBER IS EVEN ARE: ",even)
print("NUMBER IS ODD ARE: ",odd)

         #TUPLE
#Question 7
tuple=(1,2,3,4,56)
print(tuple[::-1])

#Question 8
tuple1=(12,34,567,9008,335)
print(max(tuple1))
print(min(tuple1))

        #STRINGS
#Question 9
string='asdfghjkl'
print(string.upper())

#Question 10
string1=input("Enter the numeric character: ")
print(string1.isdigit())

#Question 11
string2='world'
print(string2.replace('world','HEllo'))