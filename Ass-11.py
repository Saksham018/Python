#Q.1- Write a python code to find a valid email address from a text

import re
email=re.finditer('[a-zA-Z0-9_.]*[@](gmail.com|yahoo.com)','saksham@gmail.com,kapila@yahoo.com')
print("valid email id are: ")
for i in email:
    print(i.group())

#Q.2- Write a python program to find a valid Indian phone number from a text.(Valid Indian numbers will start with "+91-" and after that [6-9] followed by 9 digits. )
phone=re.finditer('[+][9][1][-][6-9][0-9]{9}','+91-9023240226 asdf 899754' )
print("Phone numbers are: ")
for i in phone:
    print(i.group())