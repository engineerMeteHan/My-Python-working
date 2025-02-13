# Metehan GENCER
# EmbeddedTech Solutions 

# Import module 
import operator

# Using operator.contain()
# Checking an integer in a list 
print(operator.contains([1,2,3,4,5], 2))

# Checking character in a string 
print(operator.contains("Hello World", 'O'))

# Checking an integer in a set 
print(operator.contains({1,2,3,4,5}, 6))

# Checking for a key in a dictionary 
print(operator.contains({1: "Geeks", 2:"for", 3:"geeks"}, 3))

# checking for an integer in a tuple 
print(operator.contains((1, 2, 3, 4, 5), 9))
print("------------------------------------------------")

# Python prıgram rto illustrate the use of 'is' identity operator 
num1 = 5
num2 = 5

a = [1, 2, 3]    # Even though both the list have same data, the output is stil False. 
# This is because both the lists refers to different objects in the memory.
b = [1, 2, 3]
c = a

s1 = "hello world"
s2 = "hello world"

# using 'is' identity operator on different datatypes
print(num1 is not num2)
print(a is not b)
print(a is not c)
print(s1 is not s2)
print(s1 is not s2)
print("-----------------------------------------------------")
a = [1, 2, 3]
b = [1, 2, 3]

print(a is b)
print(a == b)
#------------------------------------------------------------------------------
# Python Data Types 
# int, float, string, list and set

x = 50              # int 
x = 60.5            # float 
x = "Hello World"   # string
x = ["geeks", "for", "geeks"] # list 
x = ("geeks", "for", "geeks") # set
print("------------------------------------------------------------")
a = 5 
print(type(a))   # <class 'int'>
b = 5.0
print(type(b))  # <class 'float'>
c = 2 + 4j
print(type(c))  # <class 'complex'>
print("-------------------------------------------")
age = "21"      # String 
print("age = ", int(age))
print("------------------------------------------------------")
# int() on string representation of numbers 
print("int('9') =", int('9'))

# int() on float values 
print("int(9.9) =", int(9.9))

# int() on Python int 
print("int(9) =", int(9) )
print("-------------------------------------------------")

# octal to decimal using int()
print("int() on 0o12 =", int('0o12', 8))

# binary to decimal using int()
print("int() on 0b110 =", int('0b110', 2))

# hexa-decimal to decimal using int()
print("int() on 0x1A = ", int('0x1A', 16))
#----------------------------------------------------------------
print(int('0b101', 2))
print(int('0b1111', 2))
print("-----------------------------------------------------")

#-------------------------------------------------------------
class Number:
    value = 7

    def __int__(self):
        return self.value

data = Number()
print("number =", int(data))
print("-----------------------------------------------")
#-------------------------------------------------------
class Number:
    value = 7

    def __index__(self):
        return self.value
    
data = Number()
print("Number =", int(data))
print(dir(int))
#---------------------------------------------------------------
print("---------------------------------------------------")
print(1.7e308)

print(1.82e308)
print("-------------------------------------------------")

def frac(d):

    # Using as integer ratio 
    b = d.as_integer_ratio()

    return b

# Driver Code 
if __name__ == '__main__':
    b = frac(3.5)
    print(b[0], "/", b[1])

def booln():

    # Using as_integer 
    print((-5.0).is_integer())
    print((4.8).is_integer())
    print(float.is_integer(275.0))

# Driver code 
if __name__ == '__main__':
    booln()

#---------------------------------------------------------------
def frac(a):

    # Using float.hex
    a = float.hex(35.0)

    return a

# Driver code 
if __name__ == '__main__':
    b = frac(35.0)
    print(b)

def frac(a):

    # Using a float.fromhex()
    a = float.fromhex('0x1.1800000000000p+5')
    return a

if __name__ == '__main__':
    b = frac('0x1.1800000000000p+5')
    print(b)
print("------------------------------------------")
print(complex(1, 2))
print(complex(10, 20))
#----------------------------------------------------------
# Numeric type 
# Nothing is passed 
z = complex()
print("complex() with no parameters:", z)

# Integer type 
# Passing first parameters only 
complex_num = complex(5)
print("Int: first parameter only", complex_num)

# Passing bpth parameter 
complex_num2 = complex(7, 2)
print("Int: both parameters", complex_num2)

# Float type 
# Passing first parameter only 
complex_num3 = complex(3.6)
print("Float: first parameter only", complex_num3)

# Passing both parameters 
complex_num4 = complex(3.6, 8.1)
print("Float: both parameter", complex_num4)
print()

# type
print(type(complex_num))

# String 
# only first parameter is to be passed 
z1 = complex("7")
print(z1)

print()
z2 = complex("2")

# This will raise TypeError
print(z2)
#----------------------------------------------------
z1 = complex("7+17j")
print(z1)
print()
z2 = complex("7+17j")

# This will not raise ValueError due to spaces around operator. Because, I was correct the error 
print(z2)

s = "GFG"
print(s[1])
s1 = s + s[0]       # Update
print(s1)
s1 = s + "Mwet"       # Update
print(s1)

# Creating a String
s1 = 'mete'         # String
s2 = "Gencer"       # String
print(s1)
print(s2)

# Multi-line Strings
s = """I am learning 
Python String on Geeksforgeeks"""
print(s)

s = '''I'm an
    Engineer'''
print(s)

s = "Geeksforgeeks"

# Accesses first character: 'G'
print(s[0]) 

# Accesses 5th character: 's'
print(s[4])
print(s[-10])
print(s[-5])
# Retrieves characters from index 1 to index 3:
print(s[1:4])
print(s[:3])
print(s[3:])
# Reverse a string
print(s[::-1])
myName = "Metehan GENCER is an Embedded System Engineer"
print(myName[::-1])

s = "Metehan Gençer"

# Trying to change the first character raises an error 
# s[0] = 'I'  # Uncommenting this line will cause a TypeError 

# Instead, create a nre string
s = "G" + s[1:]
print(s)
print(s[1:])

s = "MEte"
del s   # This will deletes entire string
# print(s)

s = "Metehan GENCER"

# Updating by creating a new string
s1 = "H" + s[1:]
print(s1)
# Replacing "engineer" with "Metehan GENCER"
s2 = s.replace("GENCER", "Engineer")
print(s1)
print(s2)

s = "Metehan GENCER is an Embedded System Engineer. Also He loves Coding"
print(len(s))
print(s.upper())
print(s.lower())

s = "    Mete    "

# Removes spaces from both ends
print(s.strip())

s = "Python is fun"
print(s.replace("fun", "awesome"))

s1 = "mete"
s2 = "han"
s4 = s1 + s2
print(s4)
s = "hello "
print(s * 3)

name = "mete"
age = 22 
print(f"Name: {name}, Age: {age}")

name = "Metehan"
surname = "GENCER"
age = 35 
print(f"Name: {name}, Surname: {surname}, Age: {age}. Also, Metehan is an Embedded System Engineer")
s = "My name is {} and I am {} years old.".format("Metehan", 22)
print(s)
s = "My car is {} and My friend's car is {}.".format("blue", "black")
print(s)

s = "Metehan GENCER"
print("MetE" in s)
print("GfG" in s)

a = [10, 20, 15 ]
print(a[0])
a.append(11)
# a.remove(20)
a.append(100)
print(a)

# Creating a list
a = [1, 2, 3, 4, 5]

# List of strings
b = ["apple", "banana", "cherry"]

# List of integers
a = [1,2,3,4,5]

# Mixed Data types
c = [1, "Hello", 3.14, True]
print("---------------------------------------------------")
print(a)
print(b)
print(c)

# From a Tuple
a = list((1, 2, 3, 'apple', 4.5))
print(a)
print(list((1,2,3)))
print(list(("Metehan", "Gencer")))

a = [2] * 5
print(a)
print([0] * 7)
b = ["Mete"] * 10
print(b)
#------------------------------------------------------------------
a = [10, 20, 30, 40, 50]
print(a[0])
print(a[-1])
#--------------------------------------------------------
# Initialize an Empty list 
a = []

# Adding 10 to end of list 
a.append(10)
print("AFter append(10):", a)

# Inserting 5 at index 0
a.insert(0, 5)
print("After insert(0, 5):", a)

# Adding multiple elements [10, 20, 25] at the end 
a.extend([15, 20, 25])
print("After extend([15, 20, 25]):", a)

a = [10, 20, 30, 40, 50]

# Change the second element 
a[1] = 25
print(a)

a = [10,20,30,40,50]
print("-----------------------------------------------")
a.remove(30)
print("after remove(30):", a)

# Removes the element at index 1 (20)
popped_value = a.pop(1)
print("Popped element:", popped_value)
print("After pop(1):", a)

# Deletes the first element (10)
del a[0]
print("after del a[0]", a)
#-----------------------------------------------------
a = ["apple", "banana", "cherry"]
# Iterating over the list 
for item in a:
    print(item)
print("---------------------------------------------")
data = ["enginner", "software", "hardware"]
for item in data:
   print(item)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]    
print(matrix)
print(matrix[0][2])
print(matrix[1][2])
print(matrix[2][2])
print(matrix[0][0])
print(matrix[1][0])
print(matrix[2][0])
#-----------------------------------------------------------
a = [2, 5, 6, 7]
a.append(8)
print(a)
a.append(1000)
print(a)

a = [1, "hello", 3.14]
a.append(True)
print(a)

a = [1, 2, 3]
a.append([4, 5, 5])
print(a)
#--------------------------------------------------------------
a = [1, 2, 3]
b = [4, 5]

# Using extend() to add elements of b to a
a.extend(b)
print(a)

data = ["mete", "han"]
data_x = ["genç", "er"]
data.extend(data_x)
print(data)
print("----------------------------------")
#Using a tuple
a = [1, 2, 3]
b = (4, 5)
a.extend(b)
print(a)
print("----------------------------------")
# Using a set
a = [1, 2, 3]
b = {4, 5}
a.extend(b)
print(a)
print("----------------------------------")
# using a string
a = ['a', 'b']
b = "cd"
a.extend(b)
print(a)
print("----------------------------------")
fruit = ["banana", "cherry", "grape"]
fruit.insert(1, "apple")
print(fruit)
fruit.insert(2, "Mete")
print(fruit)

score = [43, 45, 99, 76]
score.insert(2, 45)
print(score)

list = ["sun", "rises", "in", "the", "east"]
list.insert(0, "The")
print(list)

list1 = [1, 2, 3, 4, 5, 6, 7]
# Insert 10 at 4th index
list1.insert(4, 10000000)
print(list1)

list1 = [1, 2, 3, 4, 5, 6]

# Element to be inserted
element = 13 
# Element to be inserted before 3
beforeElement = 3
# Find index
index = list1.index(beforeElement)
print("ssas ==", index)
# Insert element at beforeElement
list1.insert(index, element)
print(list1)

#-------------------------------------------------------------------
list1 = [1, 2, 3, 4, 5, 6]

num_tuple = (4, 5, 6)

#Inserting a tuple to the list 
list1.insert(2, num_tuple)
print(list1)
list1.insert(1, num_tuple)
print(list1)

fruits = ["apple", "banana", "cherry"]
fruits.insert(-1, "orange")
print(fruits)

my_list = [{'name': 'Alice', 'age': 30},
           {'name': 'Bob', 'age': 25}]
new_dict = {"name": "Metehan", "age": 48}
my_list.append(new_dict)
print(my_list)

list1 = [1, 2, 3]
list2 = [4, 5, 6]

list1 = list1 + list2
print(list1)

list1 = [1, 2, 3]
s = {4, 5, 6}
list1.insert(2,s)
print(list1)
#-----------------------------------------------------
a = ['a', 'b', 'c']
a.remove("c")
print(a)
print("-------------------------------------------------")
# Original list
a = [1, 2, 3, 4, 5, 6, 7, 8]

# list of elements to remove 
b = [2, 4, 6]

# Remove elements from main_list that are in remove_list
for item in b:
    if item in a:
        a.remove(item)

# print the updated main_list 
print(a)
print("-------------------------------------------------")

a = [1, 2, 3, 4, 5, 6, 7, 8]

# list of elements to remove 
b = [1, 2, 3]

# Remove elements from öaim_list that are im remove_list 
for item in b:
    if item in a:
        a.remove(item)

print(a)
print("***************************************************")
main_list = ["a", "b", "c", "d", "e", "f"]
remove_list = ["a", "b", "c"]

for item in remove_list:
    if item in main_list:
        main_list.remove(item)

print(main_list)

# Let's take an example to remove an element from the list using pop()
a = [10, 20, 30, 40, 10000]

# Remove the last element from list 
print("removed element : ", a.pop())
print(a)
print("------------------------------------------")

a = ["apple", "orange", "banana", "kiwi"]

# Remove the 2nd index from list 
val = a.pop(0)

print(val)
print(a)
#----------------------------------------------------
a = [10, 20, 30, 40]

# Remove the last element from list 
val = a.pop()
print(val)
print(a)
#---------------------------------------------------

class gfg_class:
    a = 20 

# Creating instance of class 
obj = gfg_class()

# Delete object using del 
del obj

# We can also delete class using del keyword 
del gfg_class

# Deleting variables -> Del keyword can be used to delete variables 
a = 20
b = "metehanGencer"

# Delete both the variables 
# del a, b 

print(a)
print(b)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a)

del a[1]
print(a)

del a[3:5]

print(a)

d1 = {"small": "big", "black": "white", "up": "down"}
d2 = {"a": 1, "b": 2, "c": 3}
del d1["black"]
print(d1)
print(d2)
#----------------------------------------------------------------
# tuple

# Creating an empty tuple 
tup = ()

#Using string
tup = ("Geek", "For")
print(tup)

# Using list 
li = [1, 2, 3, 4, 4]
print(tuple(li))

# Using built-in function 
tup = tuple("Geek")
print(tuple)


tup = (5, "welcome", 7, "geeks")
print(tup)

tup1 = (0, 1, 2, 3)
tup2 = ("python", "geek")
tup4 = ("MetehanGencer")
tup3 = (tup1, tup2, tup4)
print(tup3)

tup1 = ("Geek") * 30
print(tup1)

"""
# Creating a Tuple with the use of loop
tup = ("Geeks")
n = 50
for i in range(int(n)):
    tup = (tup,)
    print(tup)

tup = ("mete")
n = 10
for i in range(int(n)):
    tup = (tup,)
    print(tup)"""

# Accessing Tuple with indexing 
tup = tuple("Geeks")
print(tup)
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])

# Accessing a range fo elements using slicing
print(tup[1:4])
print(tup[:3])

# Tuple unpacking 
tup = ("Geeks", "For", "Geeks")

# This line unpack values of Tuple1
a, b, c = tup
print(a)
print(b)
print(c)

new_tuple = ("mete", "han", "gencer")
x, y, z = new_tuple
print(x)
print(y)
print(z)

tup1 = (1, 2, 2, 4)
tup2 = ("mete", "han",  "gencer")
tup3 = tup1 + tup2
print(tup3)

#------------------------------------------------------------------------
tup = tuple("METEHAn")
print(tup)

# Removing first element 
print(tup[1:])

print(tup[::-1])

# Printing element of a range 
print(tup[4:9])

a = ["cat", "dog", "tiger"]
print(a.index("dog"))

a = [10, 20, 30, 40, 50, 40, 60, 40, 70] #This is list

res = a.index(40, 4, 8)
print(res)

# try-except
a = ["red", "green", "blue"]

try: 
    index = a.index("red")
    print(a)
except:
    print("yellow is not in the list")

a = [1, 2, 3, 1, 2, 1, 4]

c = a.count(7)
print(c)

a = [1, "gfg", 3.14, "gfg", 1, True, True, 1,True,True,True,True,True,True]

c1 = a.count("gfg")
c2 = a.count(1)
print("------------------------------------------")
print(c1)
print(c2)
#---------------------------------------------------------------------------------
a = [1, [2, 3], 1, [2, 3], 1]
c = a.count([2,3])
print(c)
#-------------------------------------------
print(all([True, True, True]))
print("--------------------------------------------")

# All elements of list are True
l = [4, 5, 1]
print(all(l))

# All elements of list are False 
l = [0, 0, False]
print(all(l))

# Some elements of list are True while others are false 
l = [1, 0, 6, 7, False]
print(all(l))

# Empty list 
l = []
print(all(l))

# all() with condition - to check if all elements ore greater than 0
l = [1, 3, 1, 2, 4]
print(all(ele > 0 for ele in l))
print("------------------------------------")
# all elements of tuple are true
t = (2,4,6)
print(all(t))

# all elements of tuple are false 
t = (0, False, False)
print(all(t))

# some elemets of tuple are true while others are false 
t = (5, 0, 3, 1, False)
print(all(t))

t = ()  # This is an empty list 
print(all(t))

# all() w,th condition - to chack if all elements are even 
l = (2, 4, 6, 8, 11)
print(all(ele % 2 == 0 for ele in l))
print("-------------------------------------------")

# all element of set are true 
s = {1, 1, 3}
print(all(s))

# All elements of set are false 
s = {0,0,False}
print(all(s))

# Some elements of set are true while others are false 
s = {1,2,0,8,False}
print(all(s))

s = {} #empty set
print(all(s))

# all() eith condition - to check if absolute of all elements is greater than 2
l = {-4, -3, 6, -1, 4}
print(all(abs(ele) > 2 for ele in l))

print("----------------------------------------")
# Working of all() with dictionaries
# all elemets of dictionary are true
d = {1: "Hello", 2: "Hi"}
print(all(d))

# all elements of dictionary are true while others are false
d = {0: "Mete", 1: "hello", 2: "Hi"}
print(all(d))

d = {} # This is an empty dictionary
print(all(d))

# all() with condition - to check if all letters of word 'time' are there
l = {"t":1, "i":1, "m":2, "e":1}
print(all(ele > 0 for ele in l.values()))

print("----------------------------------------------------------")
# non-empty string 
s = "Hi there"
print(all(s))

# Non-empty string
s = "000"
print(all(s))

# Empty string
s = ""
print(all(s))
#--------------------------------------------------------------
# list of boolean values 
l = [False, False, True, False, False]
print("------")
print(any(l))
print("------")

# All elemnts of list are true
l = [4, 5, 6]   #
print(any(l))

# All elements of list are false
l = [0, 0, False]
print(any(l))

# Some elements of list are true while others are false 
l = [1, 0, 6, 7, False]
print(any(l))

# Empty list 
l = []
print(any(l))
print("------")

# All elements of tuple are true 
t = (2, 4, 6)
print(any(t))

# All elments of tuple are false 
t = (0, False, False)
print(any(t))

# Some elements of tuple are true while others are false 
t = (5, 0, 3, 1, False)
print(any(t))

t = () #Empty tuple
print(any(t))
#-----------------------------------------------------------------------------
print("------")
# All elements of set are true 
s = {1,1,3}
print(any(s))

# All elements of set are False 
s = {0,0,False}
print(any(s))

# Some elements of set are True while others are False 
s = {1,2,0,8,False}
print(any(s))

s = {}
print(any(s))
#--------------------------------------------------------------------------------
# All keys of dictionary are True 
print("------")
d = {1: "Hello", 2: "Hi"}
print(any(d))

# All keys of dictionary are false 
d = {0: "Hello", False: "Hi"}
print(any(d))

# Some keys of dictionary are True while others are false 
d = {0: "Metehan", 1: "Hello", 2: "Hi"}
print(d)
print(any(d))

d = {}
print(any(d))
print("------")
#---------------------------------------------------------------------------------------
# non-empty string
s = "hi there"
print(any(s))

s = "000"
print(any(s))

s = ""
print(any(s))
#--------------------------------------------------------------------
# Initializing list 
test_list = [4, 5, 8, 9, 10, 1]
print("The original list: ", test_list)

# Check if any element in list satisfies a condition using any()
res = any(ele > 10 for ele in test_list)
print("Does any element satisfy specified condition ? : ", res)

print("--------------------------------------------------------------------------------")

# This function gives same result as built-in any() function 
def my_any(list_x):
    for item in list_x:
        if item:
            return True
    return False

x = [0, 0, 0, 0, True, 0]
print(my_any(x))
#-------------------------------------------
s1 = "abcd"
print(len(s1))

s2 = ""
print(len(s2))

s3 = "a"
print(len(s3))
#----------------------------------------------------
print("---------------")

# with tuple
tup = (1, 2, 3)
print(len(tup))

# with list 
l = [1, 2, 3, 4]
print(len(l))

# This is a dictionary
dic = {"a": 1, "b": 2}
print(len(dic))

# This is a set
s = {1,2,3,4}
print(len(s))

# Python len() with custom object
class Public:
    def __init__(self, number):
        self.number = number
    def __len__(self):
        return self.number

obj = Public(12)
print(len(obj))

l = range(1, 11)
print(l)
print(len(l))

a = ["Geeks", "for", "Geeks"]

# Iterating list using enumerate to get both index and element
for i, name in enumerate(a):
    print(f"Index {i}: {name}")

# Converting to a list of tuples
print(list(enumerate(a)))














































































































































































































































































































