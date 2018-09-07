#Question 1
import pymongo
client = pymongo.MongoClient()
data = client['Students1']
collection = data['Stud']

#Question 2
#Question 3
for i in range(0,11):
    name = input('Enter name: ')
    marks = int(input('Enter marks: '))
    collection.insert_one({'Name':name,'Marks':marks})
d = collection.find()
for doc in d:
    print(doc)

#Question 4
print("Marks greater than 80 students are:")
p=collection.find({'Marks':{'$gt':80}})
for i in p:
    print(i)
