#Question 1
import sqlite3
con = sqlite3.connect('students.db')
print("Complied")
con.close()
#Question 2
try:
    con = sqlite3.connect('Students.db')
    cursor = con.cursor()
    query = 'create table student12(name varchar(20),marks number(3))'
    print('Created')
    cursor.execute(query)
    for i in range(10):
        print("Enter name",i,"and marks " , i)
        n = input()
        m = int(input())
        query = 'insert into student12(name,marks) values(?,?)'
        cursor.execute(query,(n,m))
    con.commit()
except sqlite3.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem occured: ', e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
#Question 4
try:
    con=sqlite3.connect('Students.db')
    cur = con.cursor()
    query = 'Select * from student12 where marks>80'
    cur.execute(query)
    data = cur.fetchall()
    for row in data:
        print('Name: {} , Marks: {}'.format(row[0], row[1]))
except sqlite3.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem occured: ', e)

finally:
    if cur:
        cur.close()
    if con:
        con.close()