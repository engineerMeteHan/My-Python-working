# Python program to demonstrate
# operator overloading

class Geek():
    def __init__(self, value):
        self.value = value

    def __and__(self, obj):
        print("And operator overloaded")
        if isinstance(obj, Geek):
            return self.value & obj.value
        else:
            raise ValueError("Must be a object of class Geek")

    def __or__(self, obj):
        print("Or operator overloaded")
        if isinstance(obj, Geek):
            return self.value | obj.value
        else:
            raise ValueError("Must be a object of class Geek")

    def __xor__(self, obj):
        print("Xor operator overloaded")
        if isinstance(obj, Geek):
            return self.value ^ obj.value
        else:
            raise ValueError("Must be a object of class Geek")

    def __lshift__(self, obj):
        print("lshift operator overloaded")
        if isinstance(obj, Geek):
            return self.value << obj.value
        else:
            raise ValueError("Must be a object of class Geek")

    def __rshift__(self, obj):
        print("rshift operator overloaded")
        if isinstance(obj, Geek):
            return self.value >> obj.value
        else:
            raise ValueError("Must be a object of class Geek")

    def __invert__(self):
        print("Invert operator overloaded")
        return ~self.value


# Driver's code
if __name__ == "__main__":
    a = Geek(10)
    b = Geek(12)
    print(a & b)
    print(a | b)
    print(a ^ b)
    print(a << b)
    print(a >> b)
    print(~a)

    # Assignment operator
    """
        Assignment operators are used to assign vales to the variables 
        Metehan GENCER is an Embedded System Engineer
    """
a = 10 
b = a 
print(b)
b += a
print(b)
b -= a 
print(b)
b *= a
print(b)
b <<= a 
print(b) 

print("These are the python assignment operators examples --->>")
# Assigning values using Assignmnt operator 
a = 3
b = 5

c = a + b

# Output
print(c)
a = 3 
b = 5

# a = a + b
a += b

# output 
print(a)

a = 3 
b = 5

a -= b
print(a)

a = 3 
b = 5

a *= b  # a = a * b
print(a)

a = 3
b = 5
a /= b
print(a)


a = 3
b = 5
a %= b
print(a)


a = 3
b = 5

a //= b
print(a)

a = 200
b = 10

a //= b
print(a)

a = 3
b = 5
a **= b
print(a)

a = 3 
b = 5

a &= b
print(a)

a = 3
b = 5

a |= b
print(a)

a = 3
b = 5

a ^= b
print(a)

a = 3 
b = 5

a <<= b
print(a)

# Walrus Operator (:=)

a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]     # a list

# walrus operator 
while(x := len(a)) >= 15:
    a.pop()
    print(x)

# Example of using the walrus operator in a while loop
"""
while (n := int(input("Enter a number (0 to stop): "))) != 0:
    print(f"You entered: {n}")
"""
i = 11
if (i < 15):
    print("i =",i,", i is smaller than 15")
    print("I'm in if block")
else:
    print("i =",i, ", i is greater than 15")
    print("I'm in else block")
print("I'm not in if and not in else block")

"""
i = 20 

# checking if i is greater than 15
if (i > 15):
    print("i is less than 15")

print("I am not in if")
"""

i = 0 

#Checking if i is greater than 0
if (i > 0):
    print("i is positive")
else:
    print("i is 0 or negative")

print("Not in if")

number = 0

# ternary conditional to check if number is positive or negative 
result = "Positive or zero" if number >= 0 else "negative"
print(result)

# Using logical operator with il-else
age = 10 
experience = 10

# Using > & 'and' with if-else
if age > 23 and experience > 8:
    print("Eligible")
else:
    print("not eligible")

#------------------------------------------------------------------------------------------------
# Nested if-else

i = 10
print("By the way, a = ", i)
if(i == 10):
    # First i statement
    if (i < 15):
        print("i is smaller than 15")

    # Nested if-else statement
    # Will only be executed if statemnt above
    # it is true
    if (i < 12):
        print("i is smaller than 12 too")
    else:
        print("i is greater than 15")

else:
    print("i is not equal to 10")

#---------------------------------------------------------------------------------------------------
i = -20

# Checking if i is equal to 10
if (i == 10):
    print("i is 10")

# Checking if i is equal to 15
elif (i == 15):
    print("i is 15")

# Checking if i is equal to 20

elif (i == 20):
    print("i is 20")

# If none of the above conditions true
else:
    print("i is not present")

#------------------------------------------------------------------------------------------
x = 4
if x > 15:
    print("i is greater than 15")
elif x > 5:
    print("x is greater than 5 but not greater than 15")
else:
    print("x is 5 or less")
#-----------------------------------------------------

# if statement example 
if 5 > 10:
    print("10 greater than 5")
else:
    print("10 is not greater than 20")
print("Program ended")

x = 4
if x == 4:
    print("yes")
else:
    print("no")

# if..else chain statement 

letter = "C"

if letter == "B":
    print("Latter is B")
else:
    if letter == "C":
        print("Latter is C")
    else:
        if letter == "A":
            print("Letter is A")
        else: 
            print("letter is not A, B, or C")

# print("Program ended")

num = 10 

try:
    if num > 5:
        print("Bigger than 5")
        if num <= 15:
            print("Between 5 and 15")
except:
    print("program ended")
    print("Now, except is runnig")

print("Now, program ended")
print("metehan gencer")
print("------------------------------------------------------------\n")

letter = "A"

if letter == "B":
    print("letter is B")
elif letter == "C":
    print("letter is C")
elif letter == "A":
    print("letter is A")
else:
    print("letter isn't A, B, or C")

print("-------------------------------------------------------------")
x  = 10 
y = 4

if x > 5:
    if y > 5:
        print("a and y greater than 5")
    elif y == 5:
        print("x is greater than 5 and y is 5")
    else:
        print("x is greater than 5 and y is less than 5")

print("None of the above conditions are true")

#-------------------------------------------------------------------------------
# Python for loop
for i in range(0, 105, 3):
    print(i)
#----------------------------------------------------------------
# This is my for loop example 

s = "Geeks"
# using for loop witg string 
for i in s:
    print(i)
print("-----------------------------------------------------")
a = "MetehanGencer"
for i in a:
    print(i)

mete = "python"
for i in mete:
    print(i)

# Iterating over a String 
print("String iteration")

s = "Geeks"
for i in s:
    print(i)


# Python for loop with range
for i in range(0,10,2):
    print(i)

print("--------------------------------------------------")
l1 = ["eat", "sleep", "repeat"]

for count, ele in enumerate(l1):
    print(count, ele)
#---------------------------------------------------------

l2 = ["mete", "han", "genc", "er"]

for count, ele in enumerate(l2):
    print(count, ele)
#---------------------------------------------------------------
l3 = ["BMW", "Ferrari", "Audi"]

for count, ele in enumerate(l3):
    print(count, ele)

#---------------------------------------------------------
# Nested for loop
for i in range(0, 4):
    for j in range(0, 4):
        print(i, j)

# Python for loop over list
# Python program to illustrate iterating over a list 

l = ["geeks", "for", "geeks"]       #This is a list 
for i in l:
    print(i)

l = ["metehan", "gencer", "in an embedded system engineer"]
for i in l:
    print(i)

numbers = [x for x in range(11)]
print(numbers)

myNumbers = [x for x in range(20)]
print(myNumbers)

myNewNumbers = [k for k in range(50)]
print(myNewNumbers)

mete = [x for x in range(5)]
print(mete)

#-------------------------------------------------------------------------------
# iterating over dictionary 
print("Dictionary Iteration")

d = dict()

d['xyz'] = 1234
d['abc'] = 3454

for i in d:
    print("% s % d" % (i, d[i]))

# Python for loop with tuple
t = ((1, 2), (3, 4), (5, 6))

for a, b in t:
    print(a, b)

#------------------------------------------------------------
fruits = ["apple", "banana", "cherry"]
colors = ["red", "yellow", "green"]
for fruit, color in zip(fruits, colors):
    print(fruit, "is", color)

#------------------------------------------------------------
# Print all letters except 'e' and 's'
"""
for letter in "geeksforgeeks":
    if letter == 'e' or letter == 's':
        continue
    print("Current Letter :", letter)
""" 
#-------------------------------------------------------------
for letter in 'metehanGEncerisAnEmbeddedSystemEnginner':

    # break the loop as soon it sees 'e' or 's'
    if letter == 'e' or letter == 'c':
        break

print("Current letter :", letter)

# An empty loop 
for letter in 'geekforgeeks':
    pass
print("last letter: ", letter)

# Python program to demonstrate for-else loop
for i in range(1, 40):
    print(i)
    if i == 30:
        break
else:       # Executed because no break in for 
    print("No Break\n")
print("--------------------------------------------------------------")

clothes = ["shirt", "sock", "pants", "sock", "towel"]
paired_socks = []
for item in clothes:
    if item == "shirt":
        continue
    else:
        print(f"Washing {item}")
paired_socks.append("shirt")
print(f"Washing {paired_socks}")
print("-------------------------------------------------------------")

for day in range(1, 8):
    distance = 3 + (day - 1) * 0.5
    print(f"Day {day}: Run {distance:.1f} miles")
print("------------------------------------------------------------")
# Example 1: Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
print("------------------------------------------------------------")
# Example 2: Iterating over a string
for char in 'Python':
    print(char)
print("------------------------------------------------------------")
# Example 3: Using enumarate to get index and value
for index, num in enumerate([10, 20, 30]):
    print(f"Index {index}: {num}")
# Example 4: Iterating over a dictioanry 
print("--------------------------------------------------------------")
person = {"name": 'Mete', 'age': 30}
for key, value in person.items():
    print(f'{key}: {value}')

print("--------------------------------------------------------------")

# Python While loop

# A python program to illustrate while loop
count = 0
while (count < 3):
    count += 1
    print("Hello geelk")
print("--------------------------------------------------------------")

# Infinite while loop 
age = 28

# The test condition is always true 
# while age > 19:
#    print("Infinite loop")
print("--------------------------------------------------------------")

# prints all letters except 'e' and 's'
i = 0
a = "geekforgeeks"

while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        continue

    print("Current Letter: ", a[i])
    i += 1
print("--------------------------------------------------------------")
# break the loop as soon it sees 'e' or 's'

i = 0
a = "Geekforgeeks"

while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        break

    print("Current letter", a[i])
    i += 1
print("------------------------------------------------------------------")
# An empty loop 
a = "geeksforgeeks"
i = 0
b = "mete"
print(len(b))

print("Lenght of a: ",len(a))
while i < len(a):
    i += 1
    pass 

print("value of i: ", i)
print("------------------------------------------------------------------")


# Python program to demonstrate while-else loop
i = 0
while i < 4:
    i += 1
    print(i)
    #break
else:       # Executed because no break in for 
    print("No break\n")

i = 0
while i < 4:
    i += 1
    print(i)
    break
else:       # not execute as there is a break
    print("No break")
print("------------------------------------------------------------------")
"""
a = int(input("Enter a number (-1 to quit): "))

while a != -1:
    a = int(input("Enter a number (-1 to quit): "))
print("------------------------------------------------------------------")
"""
# Inıtialize a counter 
count = 0

# Loop infinitely
while True:
    # increment the counter 
    count += 1
    print(f"Count is {count}")

    # Check if the counter has reached a certain value
    if count == 1000:
        # If so, exit the loop
        break

# This will be executed after the loop exists
print("The loop has ended")
print("------------------------------------------------------------------")

# Checks if list still contains any element
a = [1, 2, 3, 4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,55,25]

while a:
    print(a.pop())

# Python program to illustrate single statement whilie block 

count = 0

while (count < 5):
    count += 1
    print("metehanGencer")
print("The loop has ended")
print("Mete")
print("-------------------------------------------------------------------")


# Inititalizing variables 
initial_height = 10
bounce_factor = 0.5
height = initial_height

while height > 0.1:
    print("The ball is at a height of", height, "meters.")
    height *= bounce_factor
print("The ball has stopped bouncing")
print("-------------------------------------------------------------------------")

countdown = 10
while countdown >= 0:
    print(countdown)
    countdown -= 1
print("Blast Off!")

#---------------------------------------------------------------------------
"""
user_input = ""
while user_input.lower() != "exit":
    user_input = input("Enter Something (type 'exit' to stop): ")
    if user_input.lower() != "exit":
        print(f"You Entered: {user_input}")
print("Goodbye!") """
#---------------------------------------------------------------------------
# Python Functions
#
# A simple python function 
def fun():
    print("Welcome to GFG")
#---------------------------------------------------------------------------
# Driver code to call a function 
fun()

def add(num1: int, num2: int) -> int:
    """Add two numbers"""
    num3 = num1 + num2
    return num3

# driver code 
num1, num2 = 5, 12
ans = add(num1, num2)
print(f"The addition of {num1} and {num2} results {ans}.")

#-------------------------------------------------------------------------------
# Some more functions 
def is_prime(n):
    if n in [2, 3]:
        return True
    if (n == 1) or (n % 2 == 0):
        return False
    r = 3
    while r * r <= n:
        if n % r == 0:
            return False
        r += 2
    return True
print(is_prime(1507), is_prime(25007))
#------------------------------------------------------------------------
# A simple Python function to check whether x is even or odd

def evenOdd(x):
    if (x % 2 == 0):
        print(x, "is even")
    else: 
        print(x, "is odd")

# Driver code to call the function 
evenOdd(20)
evenOdd(30) # where 2 and 3 are function arguments 

#-------------------------------------------------------------------------

# Default argument example in here 
def myFun(x, y = 50):   # Where the x and y are arguments of function 
    print("x: ", x)
    print("y: ", y)

# Deriver code (We call myFun() with only arguments) 
myFun(10)       
#--------------------------------------------------------------------------
def myInfo(a, b = 100):
    print("a: ", a)
    print("b: ", b)

# Driver code 
myInfo(1)
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
# Keyword arguments 
def student(firstname, lastname):
    print(firstname, lastname)

student(firstname= "Metehan", lastname= "Gençer")
student(lastname= "Hello", firstname= "gençç")
print("--------------------------------------------------------------------")
#--------------------------------------------------------------------------

# Position argument example 
def nameAge(name, age):
    print("Hi, I am", name)
    print("My name is:", age)

# You will get correct output because argument is given order 
print("Case-1:")
nameAge("Suraj", 27)

# You will get incorrect output because argument is not in order 
print("Case-2")
nameAge(27, "Suraj")
print("--------------------------------------------------------------------")

# Arbitrary Keyword Arguments Example 
# Python program to illustrate *args for variable number of arguments 
def myFun(*argv):
    for arg in argv:
        print(arg)

myFun('Hello', 'Welcome', 'to', 'Geeks')
print("--------------------------------------------------------------------")

def myCars(*argv):
    for arg in argv:
        print(arg)

myCars("Hello My Car's names are", 'bmw', "volvo", "togg")
print("--------------------------------------------------------------------")

def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))

# Driver Code 
myFun(first = "Geeks", mid='for', last='Geeks')
print("--------------------------------------------------------------------")

def myNewInfo(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))

myNewInfo(first="Metehan", mid="Gencer", last="is an embedded System engineer")
print("---------------------------------------------------------------------")


""" The first string after the function is called Document string or Docstring in short"""
# A simple Python function to check whether x is even or odd

def evenOdd(x):
    """ The first string after the function is called Document string or Docstring in short"""
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")

# Driver code to call the function 
print(evenOdd.__doc__)

def myCarName(name, year):
    """This is docstring example-2 for understand for it used"""
    if (name == "yes"):
        print("yes")
    elif (name == "No"):
        print("No")
    else:
         print("No one is satisfied")

    if (year == "1990"):
        print("Year is true")
    else:
        print("Year is wrong")
print("++++++++++++++++++++++++++++++++")
print(myCarName.__doc__)
print("--------------------------------")
"""
# Nested Function 
def f1():
    s = "First Function ---->> I love geekforgeeks"
    m = "First Function ---->> Metehan Gencer is an Embedded System Engineer"
    def f2():
        print(s)
        print(m)

    def f3():
        try():
            print(input(f"Type the numbers: {p} {o}"))
            print("Second Function ---->> The sum of given arguments: ", p + o)
        except():
            print("Exception has occurred")
    f2()
    f3()

# Driver's Code 
f1()
"""
# Metehan GENCER is an EmBedded System Engineer
# Ptyhon code to illustrate the cube of a number using a lambda function 

# First Anonymous
def cube(x): 
    return x * x * x

cube_v2 = lambda x : x * x * x

print(cube(7))
print(cube_v2(7))

# Second anonymous Function 
def square(m):
    return m*m

square_v2 = lambda m : m * m

print(square(5))
print(square_v2(4))
print("-------------------------------------------------------------------------- ")
# Recursion in Python refers to when a function calls itself.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# n = int(input("Enter a number: "))
# print(factorial(n))
print("-----------------------------------------------------------")
#----------------------------------------------------------------------------------------
def square_value(num):
    """ This function returns the square value of the entered number"""
    return num ** 2

print(square_value(2))
print(square_value(-4))
#----------------------------------------------------------------------------------------
# Here x is a new reference to same list lst 
def myFun(x):
    x[0] = 20
    x[1] = 30
    print("Inside Function -> ", x)
# Driver code (Note that lst is modified after function call)
lst = [10,11,12,13,14,15]
myFun(lst)
print("Outside Funcrion -> ", lst)
def myFun(x):
    
    # After below line link of x with previous object gets broken.
    # A new object is assigned to x.
    x = [20, 30, 40]
    print("Inside function -> ", x)

# Driver Code (Note that lst is not modified after function call)
lst = [10, 11, 12, 13, 14, 15]
myFun(lst)
print("Outside function -> ", lst)
#----------------------------------------------------------------------------------------
def myFun(x):
    x = 20

x = 10
myFun(x)
print(x)
#-------------------------------------------------------------------------------------
def modify(x):
    x = 10      # Created a new object 

a = 5
modify(a)
print(a)  

# Pass by reference: Changes made inside the function affect the original object
def modify(lst):
    lst.append(10)      # Modifies the same object 
my_list = [1, 2, 3]
modify(my_list)
print(my_list)
#--------------------------------------------------------------------------------
def greet():
    print("HEllo world")

if __name__ == "__main__":
    greet()

# This is multiline comment
#-----------------------------------------------
# Script with function 
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == "__main__":
    print("Addition: ", add(10, 5))
    print("Subtraction: ", subtract(10, 5))
    
#-------------------------------------------------------------------------------------
# First Python Program 

print("Welcome to Python tutorial")
print("Metehan")

""" Multi-line comment used 
print("Hello world") """

# In Python, single line comments starts with hashtag symbol #

name = "geekforgeeks"
print(name)
# -------------------------------------------------------------------------------------------

name = 'Single-line comments using string literals'
print(name)

'This is a comment'

# Variable 'x' stores the integer value 10
x = 10
# Variable 'name' stores the string "Samantha"
name = "Samantha"
print(x)
print(name)
# ------------------------------------------------------
'valid example'
age = 21
_color = "lilac"
total_score = 90
print(age)
print(_color)
print(total_score)

x = 5
y = 3.14
z = "Hi"

print(x)
print(y)
print(z)

# Dynamic Typing
"""
Python variables are dynamically typed, meaning the same variable can hold different 
tyoes of values during execution
"""
x = 10
x = "Now a string"

print(x)
print(x)

# Multiple assignment 

a = b = c = 100
print(a, b, c)

x, y, z = 1, 2.5, "python"
print(x,y,z) 

# Casting variable 

s = "10"        # Initially a string 
n = int(s)      # Cast string to integer 
cnt = 5
f = float(cnt)  # Cast integer to float 
age = 25
s2 = str(age)   # Cast integer to string

# Displat results 
print(n)
print(f)
print(s2)

#print(type(n))
#print(type(f))
#print(type(s2))

# Define variables with different data types 
n = 42
f = 3.14
s = "Hello World"
li = [1, 2, 3]
d = {'key': 'value'}
   

# Get and print the type of each variable 
print(type(n))
print(type(f))
print(type(s))
print(type(li))
print(type(d))
print(type(bool))

# There are two methods how we define of a variable in Python which are local and global.  

def f():
    ll = "I am local"
    print(ll)
f()
ll = 100
print(ll)  # This would raise an error since 'local_var' is not accessible outside the function 

# Global variable 

a = "I am Global"

def f():
    global a
    a = "Modified globally"
    print(a)

f()
print(a)
#---------------------------------------------------------
x = 5
y = x
print(x)
print(y)
x = 'Geeks'
y = "computer"
print(x)
print(y)

#-----------------------------------------------------------------
# Assigning value to variable 
x = 10
print(x)

# Removing the variable using del 
del x

# print(x)

# Swapping two variables 
a, b = 5, 10
a, b = b, a
print(a, b)

x, y = 10, 11
x, y = y, x
print(x, y)

#---------------------------------------------------------------------------
word = "Python"
length = len(word)
print("Length of the word:", length)

newWord = "Metehan GENCER"
length = len(newWord)
print("Length of the word:", length)

import keyword

# printing all keywords at once using "kwlist()"
print("The list of keywords is : ")
print(keyword.kwlist)

# ----------------------------------------------------------
print(False == 0)
print(True == 1)

# True + True + True is 3
print(True + True + True)

# True + False + False is 1
print(True + False + False)

# None is not equal to 0 or an empty list []
print(None == 0)
print(None == [])

#-----------------------------------------------------------
a = True
b = False 

# Logical opetations 
print(a and b)      # AND: True if both a and b are True 
print(a or b)       # Or: True if at least one of a or b is True 
print(not a)        # NOT: Inverts the value of a 
#----------------------------------------------------------------------

# Example 1: Default argument Value 
def greet(name = None):
    if name is None:
        print("Hello, Guest!")
    else:
        print(f"Hello, {name}!")

greet()     # Output: Hello, Guest
greet("Alice")  # Output: "Hello, Alice"

#-------------------------------------------------------------------------------
# Example 2: Return value 
def find_even_number(numbers):
    for num in numbers:
        if num % 2 == 0:
            return num
    return None         # Explicitly return None if no even number is found 

result = find_even_number([1, 3, 5, 10])
if result is None:
    print("No even number found")
else:
    print(f"Found an even Number: {result}")
#-------------------------------------------------------------------------------
x = 10

if x is None:
    print("x is none")
else:
    print("x has a value")

print(10 in [1, 2, 3])

if 's' in "geeksforgeeks":
    print("s is part of geeksforgeeks")
else:
    print("s is not part of geeksforgeeks")

print(2 is 2)

a = [1, 2, 3]
b = a
c = [1, 2, 3]
d = c
# True: a and b refer to the same object 
print(a is b) 

# False: a and c have same value but are different objects 
print(d is c)
#-------------------------------------------------------------------------------

x = -10

#python if elif else statement 
if x > 0:
    print("positive")
elif x < 0:
    print("negative")
else:
    print("zero")

# for loop example 

for num in range(30):
    if num == 10:
        continue       # skip number 2
    print(num)


# while loop example 

count = 0
while count < 40:
    count += 1
    if count == 20:
        break           # Exit the loop when count reaches 4 
    print(count)

#--------------------------------------------------------------------------------
n = 10
for i in range(n):

    # pass can be used as placeholder 
    # when code is to added later 
    pass
#----------------------------------------------------------------------------
"""
a, b = 4, 2

try:
    k = a // b      # Attempt integer division (4 // 0)
    print(k)

# This block catches the ZeroDvivisionError
except ZeroDivisionError:
    print("Cannot divide by zero")

finally:
    # This block is always executed regardless or the exception 
    print("This is always executed")

print("The value of a / b is : ")

# Will raise an AssertionError because b == 0
assert b != 0, "Divide by 0 error"

# Division is attempted but will not reach due to assert 
print(a / b)

# Raise a TypeError if the strings are different 
temp = "geeks for geeks"
if temp != "geeks":
    raise TypeError("Both the strings are different")

temp = "geeks for geeks"
if temp != "geeks":
    raise TypeError("Both the strings are different") """

s = "geeksforgeeks"
print(s)

def fun():
    print("Inside Function")
fun()

class Dog:
    attr1 = "mammal"
    attr2 = "dog"

# return keyword  
def fun():

     # Assign th value 2 to the variable S
     s = 2

     # Return the value of s
     return s

# call the function and print the result 
print(fun())

# Yield keyword
def fun():
    # Yield the value 1, pausing the function here 
    yield 1
    # Yield the value 2, pausing the function again 
    yield 2
    # Yield the value 3, pausing the function once more  
    yield 3

# Iterate through the the values yielded by the function 
for value in fun():
    print(value)

g = lambda x: x*x*x

print(g(7))

# using with statement
with open('file_path', 'w') as file:
    file.write('hello world !')

import math as gfg 

print(gfg.factorial(10))

from math import factorial
import math 
print(math.factorial(10))

print(factorial(10))
#---------------------------------------------------------------------------
a = 15 
b = 10

def add():
     # Add a global variables a and b
     c = a + b
     print(c)

add()   # Output 25

def fun():
    
    # local variable in fun()
    var = 10 

    def gun():

        # Modify var1 in the enclosed scope (fun)
        nonlocal var 
        var += 10 
        print(var)

    gun()

fun()   # Output 20

#import asyncio

#async def fun():
 #   print("hello world")

# asyncio.run(fun())

import asyncio 

# Define an asynchronous main function 
async def main():
    await func()
    await mete()
    await add()

# Define another async function tht prints a message 
async def func():
    print("Hello World, This is mete")

async def mete():
    print("Bende özledim bende")

async def add():
    print(5+10)

# Run the main function using asyncio.run 
asyncio.run(main())

def check_return():
    pass 

print(check_return)

print(type(None))

# There is no Null in Python, we can use None instead of using Null values 
#print(type(Null))

var = 10

# Checking it's value 
if var is None:
    print("var has a value of None")
else:
    print("var has a value")

# Python prgoram to demonstrate is keyword 
x = ["a", "b", "c", "d"]
y = ["a", "b", "c", "d"]

c = y

print(c is y)
print(x == y)

x = 20
y = 201

if x is y:
    print(True)
else:
    print(False)

if 10 > 5:
    print("This is True")
    print("I am tab indentation")

print("I have no indentation")

a = 2

if a >= 18:
    print("GeeksforGeeks...")
else:
    print('retype the URL.')
print("All set !")

j = 0

while(j <= 5):
    print(j)
    j += 1

name = "Mete"
age = 25

print("name:", name, "Age:", age)

amount = 150.75
print("Amount: ${:.2f}".format(amount))

age = 150.52
print("Amount: ${:.2f}".format(age))

# end Parameter with '@'
print("Python", end='@')
print("GeeksforGeeks")

# Seprating with comma 
print('G', 'F', 'G', sep='')

# for formating a date 
print('09', "12", '2006', sep='-')

print("pratik", 'Geeksforgeeks', sep='@')

name = 'Tushar'
age = 23 
print(f"Hello my name is {name} and I am {age} years old.")

val = 'Geeks'
print(f"{val}for{val} is a portal for {val}.")

name = 'Om'
age = 22
print(f"Hello, My name is {name} and I am {age} years old")

import datetime

today = datetime.datetime.today()
print(f"{today:%B %d, %Y}")

print(f"'Geeksforgeeks'")
print(f"""Geeks"for"Geeks""")
print(f'''Geeks'for'Geeks''')

english = 78
maths = 56
hindi = 85

print(f"Ram got total marks {english + maths + hindi} out of 300")

newline = ord('\n')
print(f"newline: {newline}")

print(f"{{Hello, Mete}}")

print(f"{{{{Hello, Geeks}}}}")

Geek = { 'Id': 122,
         'Name': 'Mete'}

#print(f"Id of {Geek['Name']} is {Geek['Id']}")

name = "Mete"
age = 100
sentence = f"My name is {name} and I am {age} years old"
print(sentence)

num = 3.14159
formatted = f"{num:.2f}"
print(formatted)

name = "Alice"
age = 30
json_data = f'{{ "name": "{name}", "age": {age} }}'
print(json_data)

"""
name = input("enter your name: ")
message = f"Hello, {name}!"
print(message)

name = input("Enter your name: ")
message = f"Hello, {name}!"
print(message)
"""
name = "Mete"
age = 30
sentence = "My name is {} and I am {} years old.".format(name, age)
print(sentence)
"""
# Initialize variable as a string 
variable = '15'
string = "Variable as string = %s" %(variable)
print(string)
print(type(variable))

# Printing as raw data 
# Thanks to Metehan GENCER for this
print("Variable as raw data = %r" %(variable))

# Convert the variable to integer 
# And perform check other formatting options

variable = int(variable)   # Without this the below statement will give error 
string = "Variable as integer = %d" %(variable)
print(string)
print("Variable as float = %f" %(variable))

# printing as any string or char after a mark 
# here I use mayank as a string 
print("Variable as printing with special char = %c" %(variable))

print("Variable as hexadecimal = %x" %(variable))
print("Variable as octal = %o" %(variable))
"""
# Python program to demonstrate the use of formatting using % 

# Initialize variable as a string 
variable = '15'
string = "Variable as string = %s" %(variable) 
print (string ) 

# Printing as raw data 
# Thanks to Himanshu Pant for this 
print ("Variable as raw data = %r" %(variable)) 

# Convert the variable to integer 
# And perform check other formatting options 

variable = int(variable) # Without this the below statement 
						# will give error. 
string = "Variable as integer = %d" %(variable) 
print (string) 
print ("Variable as float = %f" %(variable)) 

# printing as any string or char after a mark 
# here i use mayank as a string 
print ("Variable as printing with special char = %c" %(variable)) 

print ("Variable as hexadecimal = %x" %(variable)) 
print ("Variable as octal = %o" %(variable)) 
 
"""
# Taking input from the user 
num = int(input("Enter a value: "))

add = num + 5 

print("the sum is %d" %add)
"""
"""# Taking two input at a time 
x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)
""""""
# Taking three input at a time 
x, y, z = input("Enter three values: ").split()
print("Total number of students: ", x)
print("Number of boys is:", y)
print("Number of girls: ", z)

#-----------------------------------------------------------------------------------------
# Prompting the user for input 
age_input = input("Enter your age: ")

# Converting the input to an integer 
age = int(age_input)

# Checking conditions based on user input  
if age < 0:
    print("please enter a valid age")
elif age < 18:
    print("you are a minor")
elif age >= 18 and age < 65:
    print("You are an adult")
else: 
    print("You are a senior citizen")
"""
"""name = input("Enter your name: ")
print("hello,",name, "! Welcome")
"""
"""
# Taking the inout as a string 
color = input("What color is rose?: ")
print(color)
"""
# Taking input as int
# Typecasting to int 
"""
n = int(input("How many roses: "))
print(n)
"""
"""
price = float(input("Price of each rose?: "))
print(price)

"""

a = "Hello World"
b = 10
c = 11.22
d = ("Geeks", "for", "Geeks")
e = ["Geeks", "for", "Geeks"]
f = {"Geeks":1, "for":2, "Geeks":3}

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))

#Using standart output system 
import sys 
sys.stdout.write("This is some output data.\n")
sys.stdout.write("Hello, I am MEtehan gencer\n")
"""
val = input("Enter Your value:")
print("Your value is:",val)

# Taking string as an input 
name = input("What is your name? -->")
print("Your name is: ", name)
"""
"""num = input("Enter number: ")
print(num)
name1 = input("Enter name: ")
print(name1)
"""
"""
    # Printing type of input value 
    print("Type of number", type(num))
    print("Type of name", type(name1))
    #------------------------------------------------------------------------
    num = int(input("Enter a number: "))
    print(num, " ", type(num))

    floatNum = float(input("Enter a decimal number: "))
    print(floatNum, " ", type(floatNum))
""""""
# Input a number 
num = input("Enter a number: ")
# Convert input to integer 
num = int(num)
print(num, " ", type(num))
"""""""
# input a character 
char = input("Enter a character: ")
print(char)
"""
"""
user_input = input("Enter something: ")
print(type(user_input))

"""
#------------------------------------------------------------------
"""
user_input = input("Enter something: ")
print("You entered:", user_input)

"""
""""
import datetime
time_str = input("Enter a time (HH:MM:SS): ")
# Convert string to datetime object 
time_obj = datetime.datetime.strptime(time_str, "%H:%M:%S")
print(time_obj)
"""
"""
x, y, z = input("Values: ").split()
print(x)
print(y)
print(z)
"""
"""
# Asking for multiple space-separated values 
inputs = [i for i in input().split()]
print(inputs) 
"""
"""
# taking multiple inputs at a time separated bu comma 
x = [int(x) for x in input().split(",")]
print(x)
"""
""""
            # Take space-separated inputs and convert them to integers 
            a = map(int, input().split())

            # Convert the map object to a list and print it 
            b = list(a)
            print(b)

            c = map(int, input().split())
            f = list(c)
            print(f)
""""""
#------------------------------------------------------------------------------------
# Create an empty list to store the inputs 
a = []      # An empty list 

# Ask the user for how many items they want to input 
b = int(input("How many item do you want to enter? "))

# Loop to collect multiple inputs
for i in range(b):
    val = input(f"Enter item {i + 1}: ")
    a.append(val)

# Display the list on the screen 
for i in a: 
    print(i)
#------------------------------------------------------------------------------------

# Create an empty list to store the input 
user_list = []      # An empty list 

# Ask the user for how many item they want to enter? 
item_list = int(input("How many item do you want to enter? "))

# Loop to collect multiple inputs 
for i in range(item_list):
    val = input(f"Enter item {i + 1}: ")
    user_list.append(val)

for i in user_list: 
    print(i)
#------------------------------------------------------------------------------------

        """"""

        # Create an empty list to store the input 
        user_list_second = []

        # Ask the user for hoe many item they want to enter? 
        item_value = int(input("How mant item do you want to enter? "))

        # Loop to collect multiple inputs 
        for i in range(item_value):
            val = input(f"Enter item {i + 1}: ")
            user_list_second.append(val)

        # Display the list on the screen 
        for i in user_list_second:
            print(i)
""""""
# Taking multiple input in a single line 
inputs = input("Enter multiple values separated by space: ").split()

# Printing the inputs
print(inputs)
"""
"""# Taking multiple numeric inputs in a single line and converting then to integers 
inputs = list(map(int, input("Enter multiple integers separated by space: ").split("?")))

# Printing the integer inputs
print(inputs)
"""

print("Meet")
a = [1, 2, "gfg"]
print(a)

name = "Meethan"
age = 30
print("Name:", name, "Age:", age)

name = "Mete"
age = 300000

print("Hello My name is", name, "and I am", age, "years old")
print("GeeksforGeeks \n is best for DSA Content.")
print("GeeksforGeeks is a Wonderful" + " platform for learning.")

# Without end parameter
print("GeeksforGeeks is the best platform to learn Python")

# Print() function ends with '**' as set in the end parameter
print("GeeksforGeeks is the best platform to learn Python", end='**\n')
print("Welcome to GeeksforGeeks")

# sep parameter in print() function
a = 12
b = 12
c = 2022

print(a, b, c, sep="-")

print("Welcome to GeeksforGeeks Python World.!!", file=open("file.txt", "w"))
# Using flush parameter to immediately flush the output buffer
print("This will be printed immediately.", flush=True)

# Using format() method for string formatting
name = "Alice"
age = 30
print("Hello, my name is {} and I am {} years old.".format(name, age))

# Using f-strings for string formatting
print(f"Hello, my name is {name} and I am {age} years old.")

# Using % operator for string formatting
print("Hello, my name is %s and I am %d years old." % (name, age))

# Printing a dictionary
person = {"name": "Alice", "age": 30}
print("Person details: Name = {name}, Age = {age}".format(**person))

# Printing a list
fruits = ["apple", "banana", "cherry"]
print("Fruits:", fruits)

# Printing a tuple
coordinates = (10, 20)
print("Coordinates: x = {}, y = {}".format(*coordinates))

# Printing a set
unique_numbers = {1, 2, 3, 4, 5}
print("Unique numbers:", unique_numbers)

# Printing a boolean
is_valid = True
print("Is valid:", is_valid)

# Printing a float with specific precision
pi = 3.141592653589793
print("Pi to 3 decimal places: {:.3f}".format(pi))

# Using format() method for string formatting
name = "Alice"
age = 30
print("Hello, my name is {} and I am {} years old.".format(name, age))

name = "Metehan"
age = 300
print("Hello, my name is {} and I am {} years old.".format(name, age))

# Using f-strings for string formatting
name = "Alice"
age = 30
print(f"Name: {name}, Age: {age}")

# Using % operator for string formatting
name = "Alice"
age = 30
print("Name: %s, Age: %d" % (name, age))
print("Name: %s, Age: %d" % (name, age))

# How to print without a Newline in Python
print("Hello", end=" ")
print("World")
# Real-world example: Simple Banking System

class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self):
        return self.balance

# Example usage
account = BankAccount("123456789", "John Doe", 1000)
account.deposit(500)
account.withdraw(200)
print(f"Account balance: {account.get_balance()}")

print("Hello", end=" ")
print("World")

print("Metehan", end=" ")
print("Gencer")
#-----------------------------------------------------------------------------
# String modulo operator

print("Geeks : %2d, Portal : %5.2f" % (1, 05.333))

print("Total students: %3d, Boys: %2d" % (240, 120))

print("%7.3o" %(25))        # Print octal value
print("%10.3E" %(356.08977 ))   # Print exponential notation

# Formatting output using format method
# Positional formatting with format() method
# Using indexed placeholders for string formatting

print("I love {0} for \"{1}!\"".format("Geeks", "Geeks"))

# {0} is replaced by the first argument value "Geeks"
print("{0} and Portal".format("Geeks"))

# Formatting with placeholders, {0} replaced by 'Geeks'
print("Portal and {0}".format("Geeks"))

# Advanced usage with Positional and Named Parameters

# Using positional and named arguments to format a string
template = "Number one portal is {0}, {1}, and {other}."
print(template.format("Geeks", "For", other="Geeks"))

# Format integer and floats with specified width and precidsion 
print("Geeks : {0:2d}, Portal : {1:8.2f}".format(12, 0.5534))

# Demonstrate order swapping and formating precision 
print("Second argument: {1:3d}, first one: {0:8.2f}".format(47.42, 11))

# Using named arguments for clarity in complex format 
print("Geeks: {a:5d}, Portal: {p:8.2f}".format(a=453, p=59.058))

# Formaitng output using String method
cstr = "I love geeksforgeeks"

# Printing the center aligned string with fillchr
print("Center aligned: ")
print(cstr.center(50, '#'))

# Printing the left aligned string with "-" padding
print("left aligned: ")
print(cstr.ljust(40, '-'))	

# Printing the right aligned string with "-" padding
print("Right aligned: ")
print(cstr.rjust(40, '-'))

name = "Mete"
age = 30
formatted_string = "Name: {}, Age: {}".format(name, age)
print(formatted_string)

name = "Mete"
age = 30
formatted_string = f"Name: {name}, Age: {age}"
print(formatted_string)

# How to format .2f in PY?
value = 3.14159
formatted_value = f"{value:.2f}"
print(formatted_value)

# format with .format() method
value = 3.14159 
formatted_value = "{:.3f}".format(value)
print(formatted_value)

# What is %s formatting in Python?
name = "Alice"
formatted_string = "Hello, %s!" % name
print(formatted_string) 

surname = "Gencer"
formatted_surname = "My surname is %s" % surname
print(formatted_surname)

#-----------------------------------------------------------------
# Python String

s = "GFG"

print(s[1])     # Access 2nd char 
s1 = s + s[0] + s[0]   # Concatenatio, update the string
print(s1)   

s1 = 'GeeksforGeeks'
s2 = "GeeksforGeeks"
print(s1)
print(s2)
#-------------------------------------------------------------------

s = """I am learning 
Python String on Geekforgeeks"""
print(s)    

s = '''I am 
learning'''
print(s)

s = "GeeksforGeeks" 

# Access first character: 'G'
print(s[0])

# Access 5th character  
print(s[4])

print(s[-10])    
print(s[-5])

# String slicing
s = "GeeksforGeeks"

# Retrieves character from index 1 to 3: 'eek'
print(s[0:5])

# Retrieves character from beginning to index 2: 'Gee'
print(s[:8])

# Retrieves character from index 3 to end: 'ksforGeeks'
print(s[3:])

# Reverse a string 
print(s[::-1])

sentence = "GeeksforGeeks is a computer science portal for geeks"
print(sentence[::-1])

nameSurname = "Metehan Gencer"
print(nameSurname[::-1])

s = "GeeksforGeeks"

# Trying to change the first character raises an error 
# s[0] = 'I' # Uncommenting this line will cause a TypeError 

# Instead, create a new string
s = 'M' + s[1:]
print(s)

s = "GfG"
# Delete entire string
# del s
print(s)

# Updating a String

s = "hello, Geeks"
# Updating by creating a new string
s1 = "H" + s[1:]
print(s1)

# Replacing "geeks" with "GeeksforGeeks"
s2 = s.replace("Geeks", "Metehan GENCER")
print(s2)

# len() function to get the length of the string
# This function returns the total number of character in a string
s = "Metehan GENCER"
s1 = "Bende Özledim Bende, Ferdi Tayfur"
print ("The length of first sentence:",len(s))   
print("The length of second length:",len(s1))  

# upper() and lower() method
s = "GeeksforGeeks"
print(s.upper())
print(s.lower())   

# strip() method and replace() method
s = "    Geeks for Geeks    "

# Remove spaces from both ends 
print(s.strip())

s = "Ptyhon is fun"

# Replace 'fun' with 'programming'
print(s.replace("fun", "programming"))

# Concatenating and Repeating Strings
s1 = "Hello"
s2 = "World"
s3 = s1  + " " + s2
print(s3)

name = "Metehan"
surmane = "Gencer"
concatenated = name + " " + surmane
print(concatenated) 

# Formatting Strings
name = "Alice"
age = 30    
print(f"name: {name}, age: {age}")

name_Me = "Metehan"
surname_Me ="Gencer"
print(f"My name is {name_Me} and my surname is {surname_Me}")

# Using format() method
# Another way to format strings is by using format() method

s = "My name is {}, I am {} years old.".format("Metehan", 35)
print(s)

name = "my best footballers are {} and {}.".format("Messi", "Ronaldo")
print(name) 

#Using in for String Membership Testing
s = "GeeksforGeeks"
print("Geeks" in s)
print("Gfg" in s)

# Numbers in Python

a = 4
b = 4.5     # Float
c = 4J      # Complex number

print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))

x = 5       # A positive integer
y = -23    # A negative integer
z = 0      # Zero is also considered an integer 

print(type(x))
print(type(y))
print(type(z))

# Addition 
res = 5 + 3
print(res)

# Subtraction
res = 10 - 4
print(res)

# Multiplication
res = 5 * 3
print(res)

# Division
res = 10 / 2
print(res)

# Floor Division
res = 10 // 3
print   (res)

# Modulus 
res = 10 % 3
print(res)

# Exponentiation (**)
res = 2 ** 3  # 2^3 = 8 (because 2 raised to the power of 3 is 8)
print(res)

# Absolute value
res = abs(-10)  
print(res)

# Round a number
res = round(3.14159, 2)
print(res)
print(type(res))

#--------------------------------------------------------------------------------
# Float Numbers
a = 3.14        # positive float
b = -0.99       # negative float
c = 0.0         # A float value that represents zero

print(type(a))
print(type(b))
print(type(c))

# Performing arithmetic operations on float numbers
# Addition (float)
res = 3.5 + 2.2 
print(res)

# Subtraction (float)
res = 10.5 - 4.5
print(res)

# Multiplication (float)
res = 3.5 * 2.5
print(res)

# Division (float)
res = 10.5 / 2.5
print(res)

# Floor Division (float)
res = 10.5 // 2.5
print(res)

# Modulus (float)
res = 10.5 % 2.5
print(res)

# Exponentiation (float)
res = 2.5 ** 3
print(res)

# Absolute value (float)
res = abs(-10.5)
print(res)

# Round a number (float)
res = round(3.14159, 2)
print(res)

# Complex Numbers
a = 3 + 5j
b = 2 - 4j
c = 0 + 1j

print(type(a))
print(type(b))
print(type(c))

# Performing arithmetic operations on complex numbers

# Addition (complex)
res = (3 + 5j) + (1 + 2j)
print(res)  
print(type(res))

# Subtraction (complex)
res = (3 + 5j) - (1 + 2j)
print(res)
print(type(res))

# Multiplication (complex)
res = (3 + 5j) * (1 + 2j)
print(res)
print(type(res))

# Division (complex)
res = (3 + 5j) / (1 + 2j)
print(res)
print(type(res))

# Exponentiation (complex)
res = (1 + 1j) ** 2
print(res)
print(type(res))    

# Absolute value (complex)
res = abs(3 + 4j)
print(res)

# Conjugate of a complex number
res = (3 + 4j).conjugate()
print(res)

# Real and imaginary parts of a complex number
real = (3 + 4j).real
imag = (3 + 4j).imag
print(real)
print(imag)

# Type Conversion
a = 10
print(float(a))

b = 3.14 
print(int(b))

c = '3'
print(type(c))
print(type(int(c)))

d = "3.14"
print(type(d))
print(type(float(d)))

e = 5
print(complex(e))
print(type(complex(e)))

f = 6.5
print(complex(f))
print(type(complex(f)))

# using arithmetic operations 
a = 10.6
b = 3
c = a + b

print(c)
a = int(a)
c = a + b
print(c)

complex_number = 3 + 5j
# convert_int = int(complex_number)
# print(convert_int)

# Random Numbers

import random
x = random.randint(1, 100)
print(x)

# Generating Random Floating Point Integer 
x = random.uniform(1.0, 10.0)
print(x)

# Generating Random Floating Point Number
y = random.uniform(100.0, 1000.0)
print(y)

# Special Numbers in Python

# NaN (Not a Number) Example 

import math 
n = math.nan 
print(n)

# Infinity and -Infinity Example
x = float('inf')
y = float('-inf')
print(x)
print(y)

# Returnd False as x is None 
x = None
print(bool(x))

# Returns False as x is an empty sequence
x = ()
print(bool(x))

# Returns False as x is an empty mapping
x = {}
print(bool(x))

# Returns False as x is 0
x = 0.0
print(bool(x))

# Returns True as x is a non-empty string
x = 'GeeksforGeeks'
print(bool(x))  

var1 = 0 
print(bool(var1))

var2 = 1
print(bool(var2))

var3 = -9.7
print(bool(var3))

a = 5
b = 3 
c = 1

if a > b and b < c:
    print("True")
else: 
    print("False this condition")

print("Boolean AND operator")
a = 10
b = 2 
c = 4 

if a > b and b < c:
    print("True")
else: 
    print("False")

if a and b and c:
    print("All are True")
else:
    print("All are not True")

a = 0

if (a):
    print("False")
else: 
    print("True")

#----------------------------------------------------------------------------
a = 0
b = 1

if a == b:
    print("a is equal to b")
else:
    print("a is not equal to b")

if a == 0:
    print("a is equal to 0")

if a != b:
    print("a is not equal to b")


x = 20
y = 20 
if x is y:
    print("True")
else:
    print("False")

# Create a list
a = [1, 2, 3]

# Check if lion in list or not
if 1 in a:
    print("True")

if 2 in a:
    print("The value is in the a") 
else:
    print("The value is not in the a")

# Python Lists
a = [10, 20, 30, 40, 50]

print(a[0])
a.append(11)  # add item 
a.remove(20)    # remove item

print(a)

# list of integers 
a = [1, 2, 3, 4, 5]

# List of strings 
b = ["apple", "banana", "cherry"]

# Mixed data type list
c = [1, "hello", 3.14, True]

print(a)
print(b)
print(c)

# using a tuple 
a = list((1, 2, 3, 'apple', 4.5))
print(a)

# Create a list [2,2,2,2,2]
a = [2] * 5

# Create a list [0,0,0,0,0,0,0]
b = [0] * 7 

print(a)
print(b)

a = [10, 20, 30, 40, 50]

# Access the first item of a list
print(a[0])

# Access last element of a list
print(a[-1])

# initialize an empty list
a = []

# Adding 10 to end of list 
a.append(10)
print(a)

# Inserting 5 at index 0
a.insert(0, 5)
print(a)

#Adding multiple elements [15, 20, 25] at the end
a.extend([15,20,25])
print("After extend([15, 20, 25]):", a)

a.append(100)
print(a)

a = [10, 20, 30, 40, 50]

# Change the second element
a[1] = 25
print(a)

a = [10, 20, 30, 40, 50]

# Remove the first occurence of 30
a.remove(30)
print("After remove(30):", a)

# Remove the element at index 1 
popped_val = a.pop(1)
print("Popped element:", popped_val)
print("After pop(1):", a)

# delete the first element (10)
del a[0]
print("After del a[0]:", a)

del a[0]
print("After del a[0]:", a)

a = ['apple', 'banana', 'cherry', 'date']

# Iterate over the list 
for item in a:
    print(item)
print("-----------------")
my_item_list = ["Methan", "Gencer", "GeeksforGeeks", "Python", "Nuran", "kemel", "Fatma", "Çiğdem"]
for item in my_item_list:
    print(item)

# NEsted list in PYTHON

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access the element at row 2, column 3
print(matrix[1][2])

a = [10, 20, 30, 40, 50]
length = len(a)
print(length)

mete= ["Mete", "Gencer", "GeeksforGeeks", "Python", "Nuran", "Kemel", "Fatma", "Çiğdem"]
length = len(mete)
print("new length: ", length)

a = [10, 20, 30, 40, 50]

# initialize a counter to zero
count = 0

# Loop through each element in the list
for val in a:
    # Incremet the counter for each element
    count += 1
print(count)

from operator import length_hint

a = [10, 20, 30, 40, 50]
length = length_hint(a)
print(length)

a = [10, 20, 3000, 40, 50]

# max() will return the largest in "a"
largest = max(a)
print(largest)

a = [10, 24, 76, 23, 1200]
# Assuming firt element is largest 
largest = a[0]
print("---------------------------------------------------")
# Iterate through list and find largest 
for val in a:
    if val > largest:
        # If current element is greater then largest update it
        largest = val 
print(largest)

# Using reduce() function from functools module
from functools import reduce

a = [10, 24000, 7600, 23, 12]

# Find the largest number using reduce 
largest = reduce(lambda x, y: x if x > y else y, a)
print(largest)

# Using sort()
a.sort()
largest = a[-1]
print(largest)

a = [10, 20, 30, 40, 50]

temp = a[2]
a[2] = a[4]
a[4] = temp 

print(a)

a = [10, 20, 30, 40, 50]

# Check if 30 exists in the list using loop
key = 30
flag = False

for val in a:
    if val == key:
        flag = True
        break

if flag:
    print("Element exists in the list")
else:
    print("Elment does not exist")

# A list of boolean values 
l = [False, False, True, False, False]
print(any(l))

# All elements of list are True
l = [4, 5, 1]
print(any(l))

# All elements of list are false 
l = [0, 0, False]
print(any(l))

l = [1, 0, 6, 7, False]
print(any(l))

l = []
print(any(l))

# All elements of tuple are True
t = (2, 4, 6)
print("------------------------------------")
print(any(t))

t = (0, False, False)
print(any(t))

t = (0, 0, 0, 0, False)
print(any(t))

t = ()
print(any(t))

# All elements of set are True
a = {1, 1, 3}
print("SET ---------------------------------------------")
print(any(s))

s = {0 , 0, False}
print(any(s))

s = { 1, 2, 0, 8, False}
print(any(s))
s = {}
print(any(s))

d = {1: "Hello", 2: "Hi"}
print("DICT ---------------------------------------------------------")
print(any(d))

d = {0: "Hello", False: "Hi"}
print(any(d))

d = {0: "Hello", 1: "Hi", 2: "Hi"}
print(any(d))

d = {}
print(any(d))

s = "Hi there"
print("String -------------------------------------")

print(any(s))

s = "000"
print(any(s))

s = ""
print(any(s))

# initialize a list 
test_list = [4, 5, 8, 9, 10, 17]

print("The original list: ", test_list)

res = any(ele > 10 for ele in test_list)

print("Does any element satisfy specified condition ? : ", res)   

# This function gives same result as built-in any() function 
def my_any(list_x):
    for item in list_x:
        if item:
            return True
    return False 

x = [4, 5, 8, 9, 10, 17]
print(my_any(x))
#------------------------------------------------------------------

a = [10, 20, 30, 40, 50]

flag = any(x == 30 for x in a)

if flag:
    print("Element exists in the list")
else: 
    print("Element does not exist")

#--------------------------------------------------------------------
b = [100, 200, 600]

flag = any(x == 250 for x in b)

if flag: 
    print("That's right")
else: 
    print("Noo")

#------------------------------------------------------------
a = [10, 30, 20, 40, 50]

if a.count(30) > 0:
    print("Element exist in the list")
else: 
    print("Element does not exist")


# Check if 30 exists in the list using count()
if a.count(200) > 0:
    print("MEtehan GENCER")
else: 
    print("Hello My name is mete")

# Example of using count() function
a = [10, 20, 30, 40, 50, 30, 30]

# Count the occurrences of 30 in the list
count_30 = a.count(30)
print(f"The number 30 appears {count_30} times in the list.")

# Count the occurrences of 20 in the list
count_20 = a.count(20)
print(f"The number 20 appears {count_20} times in the list.")

# Count the occurrences of 100 in the list
count_100 = a.count(100)
print(f"The number 100 appears {count_100} times in the list.")

# List index()
a = ["cat", "dog", "tiger"]  # List name is a 

print(a.index("tiger"))

a = [10, 20, 30, 40, 50, 40, 60, 40, 70]

# Find the index of 40 between index positions 4 and 8 
res = a.index(40, 4, 8)
print(res)

a = ["red", "green", "blue"]

try: 
    index = a.index('yellow')
    print(a)
except ValueError:
    print("'yellow' is not in the list")


a = [1, 2, 2, 3, 4, 4, 5,5,5,5,5,5,5,5,5,5,5,5]

# Remove duplicate by converting to a set 
a = list(set(a))
print(a)

#------------------------------------------------------------------------
a = [1, 2, 2, 3, 4, 4, 5]

# Create an empty list to store unique values
res = []

# Iterate through each value in the list: 
for val in a: 

    # Check if the value is not already in 'res'
    if val not in res:

        # If not present, append to 'res'
        res.append(val)

print(res)
#-----------------------------------------------------------------------
# Using list Comprehension 
a = [i for i in range(10)]
print(a)
b = [m for m in range(40)]
print(b)
#=======================================================================
coordinates = [(x, y) for x in range(3) for y in range(3)]
print(coordinates)
#=======================================================================
coordinates = [(x, y, z) for x in range(3) for x in range(3) for y in range(3)]
print(coordinates)
#=======================================================================

mat = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
res = [val for row in mat for val in row]
print(res)

mat1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
res1 = [val for row in mat1 for val in row]
print(res1)

#-------------------------------------------------------------------------------

a = [1, 2, 2, 3, 4, 4, 5]

# Create an empty list to store unique values 
res = []

"Use list comprehension to append values to 'res' if they are not already present"

[res.append(val) for val in a if val not in res]
print(res)

a = [1, 2, 2, 3, 4, 4, 5]

# Remove dıplicate using dictionary fromkeys()
a = list(dict.fromkeys(a))
print(a)
#========================================================================================
a = [1,2,3,4,5]
# Reverse the list in-place
a.reverse()
print(a)
#========================================================================================
a = [1,2,3,4,5]
rev = a[::-1]
print(rev)
a = [10,20,30,40,50]
newRev = a[::-1]
print(newRev)
#========================================================================================
a = [1, 2, 3, 4, 5]
# Use reversed() to create an iterator and convert it back to a list 
rev = list(reversed(a))
print(rev)
#=======================================================================================
a = [1,2,3,4,5]
# İnitialize an empty list to store reversed element 
res =  []

for val in a: 
    res.insert(0, val)
print(res)
#=======================================================================================
mete = [90,80,70]
res = []
for val in mete:
    res.insert(0, val)
print(res)
#=======================================================================================
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# define the start and end indices 
start, end = 2, 6 

# reverse the elements from index 2 to 6
while start < end:

    # Swap elements at start and end 
    a[start], a[end] = a[end], a[start]

    # Move the start index forward 
    start += 1

    # Move the end index backward
    end -= 1

print(a)
#_-------------------------------------------------------------------------------
a = [1,2,3,4,5]

# Use list comprehension to create a reversed version of the list 

rev = [a[i] for i in range(len(a) -1, -1, -1)]
print(rev)
#__________________________________________________________________________________
a = [10, 20, 30, 40]
res = sum(a)
print(res)
#---------------------------------------------------------------------------
b = [1,2,3,4,5,6]
sum = sum(b)
print(sum)
#_---_---_---_---_---_---_---_---_---_---_---_---_---_---_---_---_---_---_---_
a = [10, 20, 30, 40, 100]

# Initialize a variable to hold the sum 
res = 0

# Loop through each value in the list 
for val in a:

    # Add the current value to the sum 
    res += val 

print(res)
#------------------------------------------------------------------------------
a = [1, 2, 3]
b = [4, 5 ,6]

# Merge two list and assign the result to a new list 
c = a + b 
print(c)

mete = [10,10,10,10,10]
han = [20,20,20,20,20,20,20]
gencer = mete + han 
print(gencer)

a = [1, 2, 3, 4]
b = [5, 6]

# Add all elements from list 'b' to the end of list 'a'
a.extend(b)
print(a)

#--------------------------------------------------------------------------------
a = [10,20,30,40,50]
b = [60,70,870,60]

# Use the unpacking operator to merge the list 
c = [*a, *b]
print(c)

mete = [100,200,300]
han = [40, 50, 60]
gencer = [*mete, *han]
print(gencer)

#----------------------------------------------------------
a = [1,2,3]
b = [4,5,6]

# Initialize an ampry list to store the merged elements 
res = []

# Append all elements from the first list 
for val in a: 
    res.append(val)

# Append all elements from the second list 
for val in b:
    res.append(val)

print(res)
# ___________________________________________________________
mete = [100,200,300,40,50]
han = [500,600,789]

res = []

# Append all elements from the first list 
for val in mete:
    res.append(val)

# Append all elements from the second list 
for val in han:
    res.append(val)

print(res)
#-----------------------------------------------------------
a = [1, 2, 3]
b = [4, 5, 6]

# Use list comprehension to create a new merged list 
c = [item for item in a] + [item for item in b]
print(c)
#------------------------------------------------------------------------------------------------------------

# Imports chain function from itertools module 
from itertools import chain
# For merge two list 
a = [1,2,3]
b = [4,5,6]

# Use itertool.chain to merge the list in an efficient manner  
c = list(chain(a, b))

print(c)
#----------------------------------------------------------------------------
a = [5, 1, 5, 6]

# Sort modifies the given list
a.sort()
print(a)

b = [5, 2, 9, 6]

# Sorted does not modify the given list and returns a different sorted list 
bs = sorted(b)
print(b)
print(bs)

a = [5, 2, 9, 1, 5, 6]

# Sorted the list in ascending order 
a.sort()
print("Sorted list (ascending):", a)

a.sort(reverse = True)
print("Sorted list (descending order): ", a)

a = [5, 2, 9, 1, 5, 6]

# Sorted the list in descending order
sa = sorted(a)
print("Sorted list (ascending): ", sa)

sa = sorted(a, reverse=True)
print("Sorted list (descending): ", sa)

# Sorted a tuple :
a = (10, 12, 5, 1)
print(sorted(a))

# Sorted a set 
s = {'gfg', 'course', 'python'}
print(sorted(s))

# Sorted a String 
st = 'gfg'
print(sorted(st))

# Attempting to sort a dictionaty 
d = {10: 'gfg', 15: 'ide', 5: 'course' }
print(sorted(d))

# Sorting a list of tuples 
l = [(10, 15), (1, 8), (2,3)]
print(sorted(l))
#------------------------------------------------------------
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def myFun(p):
    return p.x

l = [Point(1, 15), Point(10, 5), Point(3, 8)]
l.sort(key = myFun)

for i in l:
    print(i.x, i.y)
#-------------------------------------------------------------
class Point:
    def __init__(self, x, y): 
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.x < other.x

l = [Point(1, 15), Point(10,5), Point(3,8)]
l.sort()

for i in l:
    print(i.x, i.y)

a = [1, -5, 10, 6, 3, -4, -9]

# Sorted by absolute values in descending order 
sa = sorted(a, key=abs, reverse=True)
print("Sorted by absolute vales: ", sa)

# List of tuples 
a = [(1, 'one'), (3, 'three'), (2, 'two')]

# Sorted by the second element of eacg tuple 
sa = sorted(a, key=lambda x: x[1])
print('Sorted by second element: ', sa)
#-----------------------------------------------------------------------
# Initializing list 
test_list = [5, 6, 3, 8, 2, 1, 7, 1]
print("------------------------------------------------------------------")
print("The original list: " + str(test_list))

# Initializing sublist 
sublist = [80, 2, 1]

res = False
for idx in range(len(test_list) - len(sublist) + 1):
    if test_list[idx: idx + len(sublist)] == sublist:
        res = True
        break

print("Is sublist present in list ? : " + str(res))

test_list = [5, 6, 3, 8, 2, 1, 7, 1]
print("----------------------------------------------------------------")
print("The original list : " + str(test_list))

sublist = [8, 2, 1]

res = any(test_list[idx: idx + len (sublist)] == sublist
        for idx in range(len(test_list) - len(sublist) + 1))

print("Is sublşist present in list ? : " + str(res))
#------------------------------------------------------------------------
# Initializing list 
test_list = [5, 6, 3, 8, 2, 1, 7, 1]

print("The original list : " + str(test_list))

sublist = [8, 2, 1]

res = ''.join(map(str, sublist)) in ''.join(map(str, test_list))

print("Is sublist present in list = : " + str(res))
#------------------------------------------------------------------------
### THIS IS A PYTHON CODE FILE TO CHECK WHETHER A SUBLIST IS PRESENT IN A LIST

# Initializing list 
test_list = [5, 6, 3, 8, 2, 1, 7, 1]

# Initializing sublist to be checked 
sublist = [8, 2, 10]

# Printing original list 
print("The original list : " + str(test_list))

# Using list comprehension and zip function to check for sublist 
res = any(sublist == list(x) for x in zip(*[test_list[i:] for i in range(len(sublist))]))

print("Is sublist present in list ? : " + str(res))
#---------------------------------------------------------------------------------
# New Code begins here 
test_list = [5, 6, 3, 8, 2, 1, 7, 1]                                # Initializing list
print("The original list" + str(test_list))                         # Printing original list
sublist = [8, 2, 70]                                                 # Initializing sublist 
if set(sublist).intersection(set(test_list)) == set(sublist):       # Check for sublist in list 
    res = True
else:
    res = False
print("Is sublist present in list ? : " + str(res))                 # Printing result 
#____________________________________________________________________________________________________________
a = 7 
print(type(a))
b = 3.0
print(type(b))
c = a + b
print(c)
print(type(c))
d = a * b 
print(d)
print(type(d))
#--------------------------------------------------------------
a = 5          # type is int
n = float(a)   # Typecast to float 
print(n)
print(type(n))
#--------------------------------------------------------------
# Python convert Float to Int 
a = 5.9
n = int(a)
print(n)
print(type(n))
#-------------------------------------------------------------
a = 5 
n = str(a)
print(n)
print(type(n))
#-------------------------------------------------------------
a = "5.9"
n = float(a)
print(n)
print(type(n))
#-------------------------------------------------------------
a = "5"
b = 't'    # If the given string is not number, then it will throw an error

n = int(a)
print(n)
print(type(n))

try:
    m = int(b)
    print("Tyoe of a: ", type(a))
    print(m)
    print(type(m))
except:
    print("If the given string is not number, then it will throw an error")

num_int = 6
num_float = 1.2
result = num_int + num_float
print(result)                      # Python automatically converts int to float 
print(type(result))
#------------------------------------------------------------------------------------
tup = ()        # Creating an empty Tuple 
print(tup)
tup = ("Geeks", "For")
print(tup)
li = [1, 2, 3, 4, 5, 6]     # Using list 
print(tuple(li))
tup = tuple("MEte")         # Using built-in function 
print(tup)
tup = tuple("Metehan GENVBD")
print(tup)
#-------------------------------------------------------------------------------------
print("----------------------------------------------------------------")
tup = (5, "Welcome", 7, "Geeks")
print(tup)
# Creating a Tuple with nested tuple 
tup1 = (0, 1, 2, 3)
tup2 = ('Python', 'geek')
tup3 = (tup1, tup2)
print(tup3)
# Creating a Tuple with repetition 
tup1 = ("Geeks",) * 5
print(tup1)
# Creating a Tuple with the use of loop
tup = ('Metehan')
n = 50 
for i in range(n):
    tup = (tup,)
    print(tup)
#-------------------------------------------------------------------------------------
# Accessing Tuple with Indexing 
print("--------------------------------------------------------------------------------------------------------------------")
tup = tuple("Geeks")
print(tup[0])
# Accessing a range of elements usinh slicing
print(tup[1:4])
print(tup[:3])
# Tuple unpacking 
tup = ("Geeks", "For", "Geeks")
# This line unpsck values of tuple1
a, b, c = tup 
print(a)
print(b)
print(c)
#------------------------------------------------------------------------------------
tup_new = ("Metehan", "GEENCER", "is an Embedded System Enginner")
a, b, c = tup_new
print(a)
print(b)
print(c)
# Concatenation of Tuples 
try: 
    tup1 = (1,2,3,4,5)
    tup2 = ["Geeks", "For", "Geeks"]
    tup3 = tup1 + tup2
    print(tup3)
except:
    print("An error arises if a list and a tuple are combined")
#------------------------------------------------------------------------------
# Slicing of a Tuple with a number 
tup = tuple("GEEKSFORGEEKS") 
# Removig first element
print(tup[3:])
# Reversing the Tuple
print(tup[::-1])
# Printing elements of a Range 
print(tup[4:9])
#--------------------------------------------------------------------------
tup = (0, 1, 2, 3, 4)
try:
    del tup
    print(tup)
except:
    print("If you try to print the deleted tuple to the screen, you will encounter an error.")
#---------------------------------------------------------------------------------------
# Ptyhon data types

val1 = 2 
val2 = 3 

# Usin the addition operator 
res = val1 * val2
print(res)

print(5/5)
print(10/2)
print(-10/2)
print(20.0/2)
print("---------------------------------------")
print(10//3)
print(-5//2)
print(5.0//2)
print(-5.0//2)
print("---------------------------------------")
val1 = 3
val2 = 2

res = val1 % val2
print(res)
res = val1 ** val2
print(res)

a = 9 
b = 5 
c = 9
print(a == b)
print(a == c)
print("-------------------------------------")
print(a != b) 
print(a != c)
print("-----------------------------------")

a = 9 
b = 5
print(a > b)
print(b > a)
print("----------------------------------")

a = 9 
b = 5
c = 9
print(a <= b)
print(a <= c)
print(b <= a)
print("------------------------------------")
a = 5 
print(1 < a < 10)       # True
print(10 > a <= 9)      # True
print(5 != a > 10)      # False 
print(a < 10 < a*10 == 50)  # True

# a < b < c => This is equivalent a < b and b < c 
a, b, c = True, False, True
print("---------------------------------------------------------------")
# AND: Both conditions must be true
if a and c: 
    print("Both a and c are True")

# OR: At least one condition must be True 
if b or c:
    print("Either b or c is True")

# NOT: Reverces the condition
if not b:
    print("b is false")
#----------------------------------------------------------
# Logical and operatoe examples 
a = 10 
b = 10
c = -10

if a > 0 and b > 0:
    print("The numbers are greater than 0")
if a > 0 and b > 0 and c > 0:
    print("The numbers are greater than 0")
else:
    print("At least one number is not greater than 0")

a = 10 
b = 12 
c = 10
if a and b and c:
    print("All the numbers have boolean value as True")
else: 
    print("At least one number has boolean value as False")

# Logical OR Operators 
a = 10 
b = -10 
c = 0
if a > 0 or b > 0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0 ")

if b > 0 or c > 0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")
#--------------------------------------------------
a = 0 
b = 0 
c = 0

if a or b or c:
    print("At least oen number has boolean value as True")
else: 
    print("All the number have boolean value as False")

#---------------------------------------------------------------
a = 10 

if not a:
    print("Boolean value of a is True")
if not (a % 3 == 0 or a % 5 == 0):
    print("10 is not divisible by either 3 or 5")
else:
    print("10 is divisible by either 3 or 5")
#------------------------------------------------------------
def order(x):
    print("Method called for value:", x)
    return True if x > 0 else False

a = order
b = order
c = order

if a(-1) or b(-5) or c(10):
    print("At least one of the number is positive")

a = 10 
b = 4 
# Print bitwise AND operation 
print("a & b =", a & b) # Bitwise AND
print("a | b =", a | b) # Bitwise OR
print("a ^ b =", a ^ b) # Bitwise XOR
print("~b =", ~b)

a = 10
b = -10
print("a >> 1 =", a >> 1)
print("b >> 1 =", b >> 1)

a = 5 
b = -10
print("a << 1 = ", a << 1)
print("b << 1 = ", b << 1)

# --------------------------------------------------------------------------
# Bitwise Operator Overloading
""" 
    Python program to demonstrate
    operator overloading
    """
class EmbeddedTech_Solutions():
    def __init__(self, value):
        self.value = value

    def __and__(self, obj):
        print("And operator overloaded")
        if isinstance(obj, EmbeddedTech_Solutions):
            return self.value & obj.value
        else: 
            raise ValueError("Must be a object of class EmbeddedTech_Solutions")

    def __or__(self, obj):
        print("Or operator overloaded")
        if isinstance(obj, EmbeddedTech_Solutions):
            return self.value | obj.value
        else:
            raise ValueError("Must be a object of class EmbeddedTech_Solutions")
        
    def __xor__(self, obj):
        print("Xor operator overloaded")
        if isinstance(obj, EmbeddedTech_Solutions):
            return self.value ^ obj.value
        else:
            raise ValueError("Must be a object of class EmbeddedTech_Solutions")

    def __lshift__(self, obj):
        print("lshift operator overloaded")
        if isinstance(obj, EmbeddedTech_Solutions):
            return self.value << obj.value
        else:
            raise ValueError("Must be object of class EmbeddedTech_Solutions")    

    def __rshift__(self, obj):
        print("rshift operator overloaded")
        if isinstance(obj, EmbeddedTech_Solutions):
            return self.value >> obj.value
        else: 
            raise ValueError("Must be an object of class EmbeddedTech_Solutions")
        
    def __invert__(self):
        print("Invert operator overloaded")
        return ~self.value
    
# Driver's Code 
if __name__ == "__main__":
    a = EmbeddedTech_Solutions(10)
    b = EmbeddedTech_Solutions(12)
    print(a & b)                        # Bitwise AND
    print(a | b)                        # Bitwise OR 
    print(a ^ b)                        # Bitwise XOR
    print(a << b)                       # Bitwise Shift left
    print(a >> b)                       # Bitwise Shitt right
    print(~a)                           # Bitwise NOT

#------------------------------------------------------------------------------------------------------
a = 3
b = 5
c = a + b 
print(c)
#-----------------------------------
a = 3 
b = 5
a += b # Equivalent a = a + b
print(a)
a -= b
print(a)
a = 3 
b = 5
a *= b 
print(a)
a = 3 
a /= b
print(a)
a = 3 
a %=b 
print(a)
a = 3
a //= b
print(a)
a = 3
b = 5
a **= b
print(a)
a = 3 
b = 5
a &= b
print(a)
a = 3 
b = 5
a|=b
print(a)
a = 3 
b = 5
a ^= b
print(a)
a = 3
a <<= b
print(a)
#--------------------------------------------------------------------------------
# Walrus Operator (:=)
a = [1, 2, 3, 4, 5]
print("-----------------------------------------")
while(x := len(a)) > 2:
    a.pop()
    print(x)
#-------------------------------------------------------------------------
"""
# Example without walrus operator 
data = input("Enter some data: ")
while data != "quit":
    print(f"You Entered: {data}")
    data = input("Enter some data: ")
    # example with walrus operator 

while (data := input("Enter Some data: ")) != "quit":
    print(f"You entered: {data}")
"""

# Example without walrus operator 
values = [1, 2, 3, 4, 5]
squares = [x ** 2 for x in values if x**2 > 10]
print(squares)
print("-----------------------------------------------")
values = [1, 2, 3, 4, 5]
squares = [y for x in values if (y := x ** 2) > 8]
print(squares)
#---------------------------------------------------------------------------------
value = len("Hell")
if value > 5:
    print(f"The length is {value}")
else:
    print("The lenght of value is less than 5")
#------------------------------------------------------------------------------
# Example with walrus operator 
if (value := len("Hello, World!")) > 5:
    print(f"The lenght is {value}")
#------------------------------------------------------------------------------
# Initialize some sequences
list1 = [1, 2, 3, 4, 5]
str1 = "Hello world"
dict1 = {1: "Geeks", 2:"for", 3:"geeks"}

# Using membership 'in' operator 
# checking an integer in a list 
print(2 not in list1)

# Checking a character in a string 
print('0' not in str1)

# Checking for a key in a dictionary 
print(3 not in dict1)
#-------------------------------------------------

def uniqueRows(input):

	# convert each row (list) into tuple
	# we are mapping tuple function on each row of
	# input matrix
	input = map(tuple, input)

	# put all rows in set
	result = set(input)

	# print all unique rows
	for row in list(result):
		print (row)

# Driver program
if __name__ == "__main__":
	input = [[0, 1, 0, 0, 1],
			[1, 0, 1, 1, 0],
			[0, 1, 0, 0, 1],
			[1, 1, 1, 0, 0]]
	uniqueRows(input)

#--------------------------------------------------------------------
# Python sets 
set1 = {1, 2, 3, 4, 5}
print("------------------------------------------------------------")
print(set1)

# Creating a set 
set1 = set()
print(set1)
set1 = set("metehan gencer  ")
print(set1)
# Creating a Set with the use of a list 
set1 = set(["Geeks", "For", "Geeks"])
print(set1)
set2 = set(["Metehan", "Gencer", "GeeksforGeeks"])
print(set2)
# Creating a Set with the use of the a tuple 
tup = ("Geeks", "For", "Geeks")
print(set(tup))
newTuple = ("Metehan GENCER", "is an EMbedded System Engineer")
print(set(newTuple))    
# Creating a Set with the use of a dictionary 
d = {"Geeks": 1, "For": 2, "Geeks": 3}
print(set(d))   

# Creating s set
set1 = {3, 1, 4, 1, 5, 9, 2}

# Unordered: The order of elements is not preserved 
print(set1) 

# Unindexed: Accessing elements by index is not possible 
# This will raise a type error 
try:
    print(set1[0])
except TypeError as e:
    print(e)

# Creating a list 
set1 = {1, 2, 3}

# Add one item 
set1.add(4)
# Add multiple items 
set1.update([5, 6, 7])
print(set1)
set1.update([8, 9], {10, 11, 12})
print(set1)
print("--------------------------------------------")
# Accessing a Set in Py
set1 = set(["Geeks", "For", "Geeks"])

# Accessing elements using for loops
for i in set1:
    print(i, end = " ")

# Checking the elements using in keyword 
print("Geeks" in set1)
#---------------------------------------------------------
# Removing elements from the set 

# Using remove method 
set1 = {1, 2, 3, 4, 5}
set1.remove(3)
print(set1)

# Attempting to remove an element that does not exist
try:
    set1.remove(10)
except KeyError as e:
    print("Error:", e)

# Using discard method
set1.discard(4)
print(set1)

# Attempting to discard an elements that does not exist
set1.discard(10)      # No error raised 
print(set1)

set1 = {1, 2, 3, 4, 5}
val = set1.pop()
print(val)
print(set1) 

# using pop on an empty set 
set1.clear()
try:
    set1.pop()
except KeyError as e:
    print("Error", e)

set1 = {1, 2, 3, 7}
set1.clear()
print(set1)  

# Creating a frozenset from a list
fset = frozenset([1, 2, 3, 4, 5])
print(fset) 

# Creating a frozenset from a set 
set1 = {1, 2, 3, 4, 5, 6}
fset = frozenset(set1)
print("New frozeset:", fset)
#-------------------------------------------------------------
# Typecasting list into set
li = [1, 2, 3, 3, 4, 5, 5, 6, 2]    # list
set1 = set(li)
print(set1)

# Typecasting string into set
s = "Metehan GENCER"
set1 = set(s)
print(set1)

# Typecasting dictionary into set
d = {1: "One", 2: "two", 3: "Three"}
set1 = set(d)
print(set1) 

# Deep into the frozenset 
animals = frozenset(["dog", "cat", "rabbit"])
print("cat" in animals)
print("elephand" in animals)
print("rabbit" in animals)

fruits = frozenset(["apple", "banana", "orange"])
print(fruits)
try:
    fruits.add("cherry")
    print(fruits)
except:
    print("An error occured")

# passing an empty tuple 
nu = ()

# Converting tuple to frozenset 
fnum = frozenset(nu)

# Print empty frozenset object 
print("Frozenset object is: ", fnum)

l = ["Geeks", "for", "geeks"]

# converting list to frozenset 
fnum = frozenset(l)
# printing empty frozenset object 
print("Frozenset object is: ", fnum)

# Creating a dictionary 
Student = {"name": "Metehan", "age": 35, "sex": "Male", "colliage": "Erciyes University", "address": "Kayseri"}
fnum = frozenset(Student)
print(fnum)

# Creating a list 
favourite_subject = ["OS", "DMBS", "Algo"]

# Creating a frozenset
f_subject = frozenset(favourite_subject)

# below line will generate error
try:
    f_subject[1] = "Networking"
    print(f_subject)
except TypeError:
    print("A TypeError is occurred")
print("--------------------------------------------------------------------------")
# FrozenSet operations 

# Initialize A and B
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])
print("A is:", A)
print("B is:", B)

# Copying a frozenset
C = A.copy()
print("C is:",C) 
D = B.copy()
print("D is:", D)   

# Union 
unionSet = A.union(B)
print(unionSet)

# Intersection 
intersectionSet = A.intersection(B)    # Contains only the elements that are present in both sets   
print("intersection:",intersectionSet)

differenceSet = A.difference(B)
print(differenceSet)

# Symmetric difference
symmetricDifferenceSet = A.symmetric_difference(B)
print(symmetricDifferenceSet)

# Creating a memory view of a bytearray 
data = bytearray("hello", "utf-8")
mv = memoryview(data)
print("--------------------------------------------")
print(mv[0])
mv[1] = 105
print(data)
#--------------------------------------------------------------
print("-------------------------------------------------------")
# Creating a memory view from bytes 
data = b'PythonAB'
mv = memoryview(data)

# Accessing individual byte using indexing 
print(mv[6])
print(mv[7])
# Accessing a range of bytes using slicing 
print(mv[0:1].tobytes())
print("--------------------------------------------------")

# Creating a bytearray for mutable data 
arr = bytearray(b'abcde')
mv = memoryview(arr)

# Modifying a byte using indexing 
mv[0] = 66 
print(arr)






















































































































































































































    










































































