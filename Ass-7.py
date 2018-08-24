#Question 1
dict={}
for i in range(3):
    key=input("Enter the elemnts")
    value=input("Enter value")
    dict[key]=value
print(dict)

#Question 2
dic={}
dic1={}
for i in range(3):
    name=input("Enter the students names: ")
    print ('student',name)
    for i in range(4):
        subject=input("Enter the subjects: ")
        marks=int(input("Enter the marks of students"))
        dic1[subject]=marks
    dic[name]=dic1.copy()
    dic1.clear()
print(dic)
