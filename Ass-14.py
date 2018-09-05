#Question 1
list4=[1,2,3]
cube=[i**3 for i in list4]
print('The cube of each value in list are: ',cube)

#Question 2
x=[p for p in range(2,100) if 0 not in [p%d for d in range(2,p)]]
print("Prime number in the range are:",x)

#Question 3
#In terms of syntax, the only difference is that you use parenthesis instead of square brackets.
#The main advantage of generator over a list is that it take much less memory.

#Lambda and Map
#Question 4
celsius = [39.2, 36.5, 37.3, 37.8]
num=list(map (lambda x:(x*1.8)+32,celsius))
print(num)
#Question 5
list1=[23,34,544,3234]
num1=list(map(lambda x:(x**2),list1 ))
print(num1)

#Filter and Reduce
#Question 6
list2=[1,2,3,4,5,6,7,8,9,12,45,67,89]
def prime(x):
    c=0
    for i in range(2, int(x / 2)):
        if (x % i == 0):
            c += 1
        if (c == 0):
            return True
        else:
            return False

sum1= list(filter(prime, list2))
print(sum1)

#Question 7
from funtools import reduce
list6=[1,2,3,4,5]
sum=reduce(lambda x,y: x*y,list6)
print(sum)

