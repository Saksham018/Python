#Qusetion 1
a=3
if a<4:
    try:
        a=a/(a-3)
        print(a)
    except:
        print("Division not allowed by zero")

#Qusetion 2
l=[1,2,3]
try:
   print(l[3])
except:
    print("List index out of range")

#Qusetion 3
#Name error: Hi there


#Question 4
#-5.0
#a/b result in 0



#Question 5
#1 IMPORT ERROR
try:
    import saksham
except ImportError:
    print("Module not found")


#2 VALUE ERROR
try:
    print(int('num'))
except:
    print("Value error")

#3 INDEX ERROR
l=[1,2,3]
try:
   print(l[3])
except:
    print("List index out of range")
