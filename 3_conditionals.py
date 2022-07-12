#if conditions

#Even or odd

number = 2
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

#elif implies else if

# --------------------------------------

#Positive or negative

if number == 0:
    print("This is zero.")

elif(number>0):
    print("Positive")
else:
    print("Negative")

# --------------------------------------

#above age 18 can get vaccinated
age = 19
is_vaccinated = False
if (age < 18):
    print("Rejected")

else:
    if not (is_vaccinated): #and,or,not keywords nai xaan
        print("Get vaccinated")
    else:
        print("already vaccinated")

# --------------------------------------

# while loop
# Syntax: while condition:
# statement

i = 0
while i < 10:
    print("Hello")
    i += 1

#Even numbers between 0 - 100
i = 2
sum = 0
while i < 100:
    if (i % 2 == 0):
        sum += i
    i += 2
print(sum)

# --------------------------------------

# for loop
# syntax:
# for range:
# statement

# RANGE
print(range(10)) #by default: 0 bata start if euta argument
print(list(range(1,10))) # 1 dekhi start
print(list(range(1,10,2))) # third argument is step
print(list(range(10)))

# --------------------------------------

my_list = (1,2,3,4,5,6)
for num in my_list:
    print(num)

# #--------------------------------------

for i in range(10):
    print(i)

# --------------------------------------

students =[
    {"name" : "Jess", "age" : 20},#List vitra dictionary
    {"name" : "Mals", "age" : 20},
    {"name" : "Suman", "age" : 20},

]
for student in students:
    print(student)
    print(student["name"])
    print(f"I am {student['name']}")
# --------------------------------------

numbers = [1, 2, 3, 4, 5]
square = []
for n in numbers:
    square.append(n**2)

print(square)

# --------------------------------------

# To find length
# len(square)

# --------------------------------------

# To print true for even numbers in list
is_even = True
for num in square:
    if(num % 2 == 0):
        print(num, is_even)

# --------------------------------------

# To print true if all the numbers in the list are even.
for num in square:
    if (num % 2 != 0):
        is_even = False
        break # to exit from loop as soon as condition is false
print(is_even)

# --------------------------------------

# Enumerate
# this gives an index with value

names = ['jess', 'jjsjs', 'sss']
print(names)
print(list(enumerate(names)))  # enumerate gives tuples


name = (0, 'Jess')  # esto garda pura tuple naii name ma assign hunxa
i, name = (0, 'Jess')  # esto garda divide vayera 1 le 0 name le jess pauxa
i, name = (0, 'Jess', 'mhrzn')  # error hanxa cuz mhrzn ko lai kei ni xaina
# esto garda 0 i ma basxa while bakii chai name ma basxa
i, *name = (0, 'Jess', 'mhrzn')
print(i, name)

for name in enumerate(names):
    print(name)

for i, name in enumerate(names):
    print(i, name)

# --------------------------------------

# List comprehension
# Mathi ko problem using list comprehension
numbers = [1, 2, 3, 4, 5]
squares = [num**2 for num in numbers] #here num**2 can be replaced by a function as well
squares_if_even = [num**2 for num in numbers if num % 2 == 0]
print(squares)
print(squares_if_even)

# --------------------------------------

# Ternery operator
# condition?value_1:value_2 in C

age = 53
category = 'old' if age > 60 else 'young'
print(category)

# --------------------------------------

# FUNCTIONS
# Syntax: def function-name():
# statements

def name():
    print("jess")

#Passing arguments to function
def display(name):
    print(name)
display('jess')  # passing argument


def display_1(name,roll):
    print(f"Name: {name}, Roll: {roll}")
display_1(name = 'jess' , roll = 13) #Pass named parameters 

# --------------------------------------

#Args and kwargs
#If arguments kati ota auxa thaha xaina vane use args and kwargs garne to represent all arguments.
# *args 
# **kwargs
# if arguments (1,2,3) type xa vane use *args
# if arguments tala ko jasto xaa vane use **kwargs

def display_marks(name, roll, **subject_scores):
    print(f"name: {name} , roll: {roll}, {subject_scores}")
display_marks('jess', 13, maths = 30, science = 45)

# Find maximum
def find_max(*numbers):
    max = numbers[0] #esma max = 0 halyo vane negative ko case ma issue auxa
    for num in numbers:
        if (num > max):
            max = num
    print(max)
find_max(1,2,3,5)

# --------------------------------------
