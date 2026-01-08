#tuples 
three_numbers=(1,2,3,1,2)
earth=('water', 'air', 'land')
combo=('water', 10, True)
print(type(three_numbers))
print(combo)
lang=tuple(('Java', 'Python','C#'))
print(type(lang))

#functions
# def greetings(name, age):
#     print('Welcome to Python World, '+name+' Your age is '+str(age))

# name=input('Enter Name: ')
# age=int(input('Enter Age: '))
# greetings(name, age) #calling the functions

# def checking(*names):
#     print('Yellow '+names[1])
# checking('yoii','hoii')

# #return keyword
def add(num1, num2):
    return num1+num2

print(add(10, 20))


#if statement
a=1
b=2

if b > a or b > 0:  #and
    print(str(b)+' is greater.')
else:
    print(str(a)+' is greater..')