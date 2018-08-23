#Qusetion 1
def sphere(num):
    return 4*3.14*num*num
num=int(input("Enter the radius: "))
print(sphere(num))

#Question 2

def perfect(num):
    sum=0
    for i in range(1,num-1):
        if(num%i==0):
            sum=sum+i
    if(sum==num):
        return True
    return False
print("List of Perfect numbers is:")
for i in range(1,1001):
    if(perfect(i)):
        print(i)
#Question 3
n=int(input("enter integer:"))
for i in range(1,11):
    print(n,"*",i,"=",n*i)

#Question 4
def power(num1,num2):
    if(num2!=0):
        num2-=1
    else:
        return 1
    return num1*power(num1,num2)
num1=int(input("Enter num1: "))
num2=int(input("Enter num2: "))
print(power(num1,num2))