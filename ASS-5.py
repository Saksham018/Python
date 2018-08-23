#Question 1
leap=int(input("Enter the year to check leap year or not: "))
if(leap%4==0):
    print("leap Year".format(leap))
elif(leap%100==0):
    print("Not Leap Year".format(leap))
elif(leap%400==0):
    print("leap Year".format(leap))
else:
    print("Not Leap Year".format(leap))

#Question 2
length=int(input("Enter the length: "))
breadth=int(input("Enter the breadth: "))
if(length==breadth):
    print("Square")
else:
    print("Reactangle")

#Question 3
first=int(input("Enter the age: "))
second=int(input("Enter the age: "))
third=int(input("Enter the age: "))
print("oldest",max(first,second,third),"Youngest",min(first,second,third))

#Qusetion 4
age=int(input("Enter the age"))
sex=input("Male or Female")
status=input("Yes or No")
if(sex=='Female'):
    print(" she will work only in urban areas")
elif(sex=='Male' and (age>=20 and age<=40)):
    print("He may work in anywhere")
elif(sex=='Male' and (age>40 and age<=60)):
    print("He will work in urban areas only")
else:
    print("Error")

#Question 5
cost=100
s=int(input("Enter the cost: "))
p=float(s*cost)
if(s>1000):
    num=float(0.1*p)
    val=float(p-num)
    print("cost after discount")
else:
    print("sorry no discount")


         #loops
#Question 6
size=int(input("Enter the size: "))
for i in range(0,size):
    num=int(input("Enter the elements"))
    print(num)

#Question 7

     while(true):
    print("This is infinte loop")
#Question 8
#ques  8
n=int(input("How many elements do you want to enter\n"))
l=[]
for i in range(0,n):
    h=int(input("Enter element\n"))
    l.append(h)
l2=[]
for i in l:
    h=i*i
    l2.append(h)
print(l2)

#ques 9
st=[]
fl=[]
iy=[]
l=[4,5,6,7,8,'a','b','c','d',5.00,6.00,8.098]
for i in l:
    if(type(i) is str):
        st.append(i)
    elif(type(i) is float ):
        fl.append(i)
    elif(type(i) is int):
        iy.append(i)
print("List of integer type is ",iy)
print("List of float type is ",fl)
print("List of string type is",st)
#ques 10
l=[]
for i in range(1,101):
    count=0
    for j in range(2, int(i/2)) :
        if(i%j==0):
            count+=1
    if(count==0):
        l.append(i)
print(l)

#ques 11
q='*'
for i in range(1,5):
    print(i*q)
#ques 12
l=[]
n=int(input("how may elements in list?\n"))
for i in range(0,n):
    h=input("Enter element")
    l.append(h)
h=input("Which element you want\n")
l.remove(h)
print(l)




