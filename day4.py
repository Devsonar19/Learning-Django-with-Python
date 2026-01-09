# Even Number Checker Program
'''
num= int(input('Enter the Number: '))

if num % 2 == 0:
    print(num, 'is even number')
else:
    print(num, 'is odd number')

'''

#Dictionaries DataTypes, should be unique key
'''
lang={
    'name':'Python',
    'speed':'not so fast',
    'bool':True,
    'number':3,
    'lists':['Java','C++','Rust'],
}
print(lang)
print(type(lang))

x = lang['bool']
print(x)

'''

# While loop
'''
i=1
while i < 5 or i == 5:
    print(i)
    i += 1

'''
# For Loop, break, range(included, excluded)
'''
my_list=[10, 20, 30]
for i in my_list:
    print(i)
    if i == 20:
        break

for x in range(4, 9):
    print(x)
else:
    print('Finoshed')

'''

# 2D lists, nested loops
'''
lists_2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print(lists_2d[0][2])

for i in lists_2d:
    for j in i:
        print(j)

'''
#Comments
#single line
'''multi line'''

#Basic Calculator
'''
num1=int(input('Enter first Number: '))
num2=int(input('Enter second number: '))
op=input('Enter operator(+,-,*,/): ')

if op == '+':
    print(num1+num2)
elif op == '-':
    print(num1-num2)
elif op == '*':
    print(num1*num2)
elif op == '/':
    print(num1/num2)
else:
    print('Enter a valid operator..!')

'''
#Try except 
'''
try:
    x = int(input('Enter integer: '))
    print(x)
except ValueError:
    print('not an integer')
finally:
    print('trying done')
else:
    code

'''
# Reading and writing Files
'''

test = open('testingLang.txt','r')
print(test.readable())
print(test.readline() )#1st line
print(test.readline()[3]) #2nd line
print(test.readlines()) #all lines

test = open('testingLang.txt','r')

test = open('newfile.txt','w')
test = open('newfile.txt','a')
test.write('New text to check if the file updates')



test.close()

'''
#Classes and Objects
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    

p1 = Person('Light', 29)
print(p1.name)

del p1.age

'''
#Inheritance
'''
class Student():
    name='Light Yagami'
    age= 25
    gender= 'male'

class Person1(Student):
    pass

p1 = Person1()
print(p1.name)

'''

#Python Shell
# terminal -> python3
# can write code there also


#Simple Login and Signup System
'''
userName =  input('Enter UserName: ')
password = input('Enter Password: ')

print('Account Created..!!')
print('You can Login')

userName1 = input('Enter UserName: ')
password1 = input('Enter Password: ')

if userName == userName1 and password == password1:
    print('Logged in')
else:
    print('Invalid Credentials')

'''
#Modules and PIP
'''

import math #module
PIP used to install packages

'''

