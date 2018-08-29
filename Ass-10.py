#Question 1

f=open("file.txt",'r')
lines=f.readlines()
n=int(input("enter the number"))
for i in range(n):
    print(lines[i],end="")
f.close()

#Question 2
f=open('file1.txt')
read=f.readlines()
string=''.join(read)
string1=string+' '
count=1
for i in range(len(string)):
    if(string[i]==' ' or string[i]=='\n'):
        if(string1[i+1]!=' ' and string1[i+1]!='\n'):
            count+=1
print("words are:",count)
f.close()


#Question 3
f=open("file2.txt")
b=open("file3.txt",'w')
b.write(f.read())
f.close()
b.close()

#Question 4
f=open('file2.txt')
g=open('file3.txt')
for i in f:
    print(i.strip()+g.readline()

#Question 5
f=open('file4.txt')
list=f.readlines()
list=[int(i.strip()) for i in list]
list.sort()
list2=[]
for i in list:
    list2.append(str(i))
my_str='\n'.join((list2))
g=open('test5.txt','w')
g.write(my_str)
g.close()
f.close()
