str = "GeeksforGeeks"

# Encoding the string with unicode 8 and 16
array1 = bytearray(str, "utf-8")
array2 = bytearray(str, "utf-16")
print(array1)
print(array2)
print("---------------------------------------------------")

# Size of array 
size = 30

# will create an array of given size and initialize with null bytes 
array1 = bytearray(size)
print(array1)
print("---------------------------------------")

#Creates bytearray from bytw literal
arr1 = bytearray(b"abcd")

for value in arr1:
    print(value)

arr2 = bytearray(b"aaaaccccc")

# Count bytes from the buffer
print("Count of c is: ", arr2.count(b"c"))

print("-----------------------------------------")
"""
# Simple list of integer 
list = [1, 2, 3, 4]

# iterable as source
array = bytearray(list)
print(array)
print("Count of bytes: ", len(array))
"""
                                                # Metehan GENCER 

array = bytearray()
print(array)

# Creating a mutable array
arr = bytearray(b'12345')
mv = memoryview(arr)

# Converting the memory view to immutable bytes 
result = mv.tobytes()
print("-----------------------------------------")
print(result) # b'12345'
print(type(result)) # <class 'bytes'>
print("-----------------------------------------")

import array

# Creating array of integers 
arr = array.array('i', [1, 2, 3, 4])
mv = memoryview(arr)

# Reinterpreting the data as unsigned bytes 
mv_cast = mv.cast('B')
print(mv_cast.tolist()) 

print(dir(int))

"""
    DUNDER OR MAGIC METHODS
    Python magic methods are the method starting abd ending with double underscore.
    They are also called dunder methods. They are defined by build-in classes in Python 
    and commanly used for operator overloading.
    For example, when we use the + operator, the magic method __add__ is called in the background.
    The magic methods are always surrounded by double underscores.
"""
from itertools import chain

# A list of odd numbers 
odd = [1, 3, 5, 7, 9]

# a list of even numbers
even = [2, 4, 6, 8, 10]

# chaining odd and even numbers 
numbers = list(chain(odd, even))    
print(numbers)

#----------------------------------------------
from itertools import chain

# A list of names
names = ['Alice', 'Bob', 'Charlie']
# A list of ages
ages = [24, 25, 26]
chain_object = chain(names, ages)
print(list(chain_object))   

# Some consonants
consonants = ['b', 'c', 'd', 'f', 'g']
# Some vowels
vowels = ['a', 'e', 'i', 'o', 'u']
# Reultant list 
res = list(chain(consonants, vowels))
# sorting the list 
res.sort()
print(res)
res = list(chain("ABC", "DEF", "GHI", "JKL"))
print(res)

str1 = "Geeks"
str2 = "for"
str3 = "Geeks"

res = list(chain(str1, str2, str3)) 
print("before joining :", res)

ans = "".join(res) 
print("after joining : ", ans)

str1 = "Mete"
str2= "han"
str3 = "Gencer"

res = list(chain(str1, str2, str3)) 
print("before joining :", res)

ans = "".join(res)
print("after joning : ", ans)

#----------------------------------------------
number_1 = "123456"
number_2 = "7890"
res = list(chain(number_1, number_2))   
print("before joining : ", res)

ans = "".join(res)      
print("after joining : ", ans)      
#----------------------------------------------
li = ["ABC", "DEF", "GHI", "JKL"]

# using chain-single iterable
res1 = list(chain(li))
res2 = list(chain.from_iterable(li))
print("-----------------------------------------")
print("using chain : ", res1, end="\n\n")   
print("using chain.from_iterable : ", res2)
#----------------------------------------------
print("-----------------------------------------")
li = ["123", "456", "789"]
res = list(chain.from_iterable(li)) 
print("res =", res, end="\n\n") 
new_res = list(map(int, res))
print("new_res", new_res)   
sum_of_li = sum(new_res)
print("\nsum = ", sum_of_li)
#----------------------------------------------
print("-----------------------------------------")  

li = ["123", "456", "789"]
res = list(map(int, list(chain.from_iterable(li)))) 
sum_of_li = sum(res)
print("res =", res, end="\n\n")
print("sum = ", sum_of_li)      
#----------------------------------------------
print("-----------------------------------------")
## SET exmples 
GEEK = set()
GEEK.add('s')
print("letters are: ", GEEK)

# Adding "e" again 
GEEK.add('e')
print("letters are: ", GEEK)

# adding 's' again 
GEEK.add('s')
print("letters are: ", GEEK)    
#----------------------------------------------
print("-----------------------------------------")  
# set of letters 
geek = {"g", "e", "k"}
# adding 's'
geek.add("s")
print("letters are: ", geek)    

# adding 's' again
geek.add("s")   
print("letters are: ", geek)

# set of letters 
geek = {6, 0, 4}    
# Adding 1
geek.add(1) 
print("LETTERS are: ", geek)
# adding 0 
geek.add(0) 
print("letters are: ", geek)    

# Multiplication table from 1 to 10 in PY
"""num = int(input("Display multiplication table of? "))
for i in range(1, 11):
    print(num, 'x', i, '=', num*i)
newNum = int(input("Display multiplication table of? "))
for i in range(1, 11):
    print(newNum, 'x', i, "=", newNum * i)
"""#----------------------------------------------
print("-----------------------------------------") 
"""# program to display the Fibonacci sequence up to n-th term
nterms = int(input("How many terms?"))
# first two terms 
n1, n2 = 0, 1
count = 0   
# check if the number of terms is valid
if nterms <= 0:
    print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
    print("Fibonacci sequence upto", nterms, ":")
    print(n1)
# generate fibonacci sequence 
else:
    print("Fibonacci sequence:")    
    while count < nterms:
        print(n1)
        nth = n1 + n2
        # update values 
        n1 = n2 
        n2 = nth
        count += 1"""
#----------------------------------------------
print("-----------------------------------------")
print("mete")

# check armstrong number (for 3 digit)
## Python progrsm to check if the number is an Armstrong number or not 
"""
# Take input from the user 
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num 
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

# display the result    
if num == sum: 
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")"""

#----------------------------------------------------------------------------
# Add elements to an empty set
GEEK = set()
GEEK.add('s')
print("letters are: ", GEEK)

# adding 'e' again  
GEEK.add('e')
print("letters are: ", GEEK)        

# adding 's' again
GEEK.add('s')
print("letters are: ", GEEK)
#----------------------------------------------------------------------------
# set of letters    
GEEK = {'g', 'e', 'k'}

# addins "s"
GEEK.add('s')
print("letters are: ", GEEK)

# adding 's' again  
GEEK.add('s')
print("letters are: ", GEEK)
print("---------------------------------------------------")    
# set of letters
geek = {6, 0, 4}

# adding 1  
geek.add(1)
print("letters are: ", geek)    

# adding 0
geek.add(0)
print("letters are: ", geek)
#----------------------------------------------------------------------------
# Pythom code to demonstrate addition of tuple to a set 
print("-----------------------------------------")
s = {'g', 'e', 'e', 'k', 's'}   # Set
t = ('f', 'o')                  # Tuple 
l = ['a', 'e']                  # List 

# adding tuple t to set s 
s.add(t)

# Adding list l to set s 
s.update(l)    
print(s)

# Creting a set  
mySet = {1, 2, 3}

# Adding a new element to the set   
mySet.add(4)    
print(mySet)

# adding existing element to the set    
mySet.add(3)
print(mySet)        
#----------------------------------------------------------------------------
"""
    You can add elements to a set using the add() method for a single elements
    or the update() method for multiple elements.
"""
print("-----------------------------------------")
# Creating a set
mySet = {1, 2, 3}   
mySet.add(4)
print(mySet)    

mySet = {1, 2, 3}
mySet.update([4, 5, 6]) 
print(mySet)
mySet.update({7, 8, 9})
print(mySet)
print("-----------------------------------------")

def Remove(sets):
    sets.discard(21)
    print(sets)

# Driver Code 
sets = set([10, 20, 26, 41, 54, 20])
Remove(sets)
print("-----------------------------------------")

def Remove(sets):
    sets.remove("ram")
    print(sets)

# Driver code   
sets = set(["ram", "aakash", "kaushik", "anand", "prashant"])
Remove(sets)

testSet = {1, 2, 3, 4, 5}
testSet.clear()
print("after clear() on testSet: ", testSet)
print("-----------------------------------------")
GEEK = {"A", "B", "C"}
print("Geek before clear:", GEEK)

# Clearing vowels 
GEEK.clear()
print("Geek after clear:", GEEK)    
print("-----------------------------------------")

set1 = {1, 2, 3, 4}

# function to copy the set 
set2 = set1.copy()
print("copied set:", set2)

first = {"g", "e", "e", "k", "s"}
second = first.copy()

# Before adding 
print("before adding:")
print("first set:", first)
print("second set:", second)

# Adding element to second, first does not change
second.add("f")

# After adding 
print("after adding:")
print("first set:", first)
print("second set:", second)
print("-----------------------------------------")

s1 = {9, 1, 0}
print(s1.pop())
print(s1)

s1 = {1, 2, 3, 4}
print("Before popping:", s1)
s1.pop()
s1.pop()
s1.pop()

print("After 3 elements popped, s1", s1)

s = {}

# popping an elelement from empty set 
try:
    print(s.pop())  
    print("Updated set is:", s)
except:
    print("There is an error in popping an element from empty set") 

# original dictionary 
dict1 = {'a': 1, 'b': 2}    

# update with another dictionary
dict1.update({'b': 20, 'c': 3})
print(dict1)

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, "c": 4}    
dict1.update(dict2) 
print(dict1)    

dict1 = {'a': 1, 'b': 2}
dict1.update([('c', 3), ('d', 4)])  
print(dict1)    

dict1 = {'a': 1, 'b': 2}    
dict1.update(c = 3, d = 4, e = 100)
print(dict1)        

set1 = {1, 2, 3}
set2 = {3, 4, 5}

set1.update(set2)
print("Updated set1:", set1)

set2.update(set1)
print("Updated set2:", set2)

set1 = {1, 2, 3}
set1.update([4, 5, 6])          # Added list with using update() method  
print("Updated set1:", set1)

setMete = {1, 2, 3, 4}
setMete.update([5, 6, 7])   
print("Updated setMete:", setMete)  

set1 = {1, 2, 3}    
set1.update([4, 5], (6, 7), {8, 9}) 
print("Updated set1:", set1)    

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {1, 2}

d2.update(d1.keys())
print("Updated d2:", d2)    

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'x', 'y'}
dict2.update(dict1.values())
print(dict2)
print("----------------------------------")
print(dict1.keys())
print(dict1.values())

dict1 = {'a': 1, 'b': 2}
dict1.update({('c', 3), ('d', 4)})  
print(dict1)    

set1 = {1, 2, 3}
set1.update("geeks for geeks")
print("Updated set1:", set1)        

dict1 = {"a": 1, "b": 2}    
dict1.update(c=3, d=4, e=100)
print(dict1)

A = {1, 2, 3}
B = {3, 4, 5}
print(A.union(B))

A = {2, 4, 5, 6}
B = {4, 5, 7, 8}
C = {7, 8, 9, 10}

# using multiple union calls 
print("A U B U C:", A.union(B).union(C))

# directly passing multiple sets 
print("A U B U C:", A.union(B, C))  

A = {2, 4, 5, 6}
B = {4, 6, 7, 8}
C = {7, 8, 9, 10}

# using | operator for union 
print("A | B | C:", A | B | C)
print("A | B:", A | B)

A = {'ab', 'ba', 'cd', 'dz'}
B = {'cd', 'ab', 'dd', 'za'}

print("A U B:", A.union(B))

A = {10, 20, 30, 40, 50}
B = {100, 30, 80, 40, 60}

print(A.difference(B))       # Elements in A but not in B
print(B.difference(A))       # Elements in B but not in A

A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7} 
C = {5, 6, 7, 8, 9}

res = A.difference(B, C)    # Elements in A but not in B and C
print("A - B - C:", res)        

A = {10, 20, 30, 40}
B = set()   # Empty set 
print(A.difference(B))   # A - B = A

A = {10, 20, 30, 40, 80}
B = {10, 20, 30, 40, 80, 100}
print(A.difference(B))   # A - B = Empty set        

A = {10, 20, 30, 40, 80}
B = {100, 30, 80, 40, 60}   

# Modified A and returns None 
A.difference_update(B)

# Prints the modified set 
print("A after difference_update:", A)  

s1 = {1, 2, 3}
s2 = {2, 3}
print(s1.intersection(s2))  # Elements in both s1 and s2

set1 = {2, 4, 5, 6}
set2 = {4, 5, 7, 8}
set3 = {4, 5, 8}

# intersection of two sets
print("set1 intersection set2: ", set1.intersection(set2))

# intersection of three sets 
print("set1 intersection set2 intersection set3 :", set1.intersection(set2, set3))      

# We can also get intersection using '&' operator   
set1 = {2, 4, 5, 6}
set2 = {4, 5, 7, 8}
set3 = {1, 0, 12}

print(set1 & set2)       # intersection of two sets 
print(set1 & set3)     # intersection of two sets   
print(set1 & set2 & set3) # intersection of three sets      

set1 = {2, 4, 5, 6}
set2 = {4, 5, 7, 8}
set3 = {1, 0, 12}

print(set1.symmetric_difference(set2))
print(set1.symmetric_difference(set3))  
print(set2.symmetric_difference(set3))

set1 = {}
set2 = {}

# union of two sets 
print("set1 intersection set2: ", set(set1).intersection(set(set2)))

set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(set1.isdisjoint(set2))  # True, as there are no common elements

set1 = {2, 4, 5, 6}
set2 = {7, 8, 9, 10}
set3 = {1, 2}

# Checking of disjoint of two sets 
print("set1 and set2 are disjoint?", set1.isdisjoint(set2)) # True   
print("set1 and set3 are disjoint?", set1.isdisjoint(set3)) # False

# Set 
A = {2, 4, 5, 6}

# list 
lis = [1, 2, 3, 4, 5]

# Dictionary dict, Set is formed on Keys 
dict = {1: 'Apple', 2: "Orange"}

dict2 = {"Apple": 1, 'Orange': 2}

print("Set A and List lis disjoint?", A.isdisjoint(lis)) # False    
print("Set A and dict are disjoint?", A.isdisjoint(dict)) # False   
print("Set A and dict2 are disjoint?", A.isdisjoint(dict2)) # True      

s1 = set()
s2 = set()  

# Using the isdisjoint method with empty sets   
print(s1.isdisjoint(s2)) # True, as both sets are empty         

s1 = {1, 2, 3, 4, 5}
s2 = {4, 10}
print(s2.issubset(s1)) # True, as s2 is a subset of s1      

A = {4, 1, 3, 5}
B = {6, 0, 4, 1, 5, 0, 3, 5}
print(A.issubset(B)) # True, as A is a subset of B  
print(B.issubset(A)) # False, as B is not a subset of A 

A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {1, 2, 4, 5}

print(A.issubset(B)) # True, as A is a subset of B
print(B.issubset(A)) # False, as C is a subset of B

print(A.issubset(C))
print(C.issubset(B))

A = {4, 1, 3, 5}
B = {6, 0, 4, 1, 5, 0, 3, 5}

print("A.issuperset(B): ", A.issuperset(B)) # False, as A is not a superset of B
print("B.issuperset(A): ", B.issuperset(A)) # True, as B is a superset of A 

A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {1, 2, 4, 5}
 
print("A.issuperset(B): ", A.issuperset(B)) # False, as A is not a superset of B
print("B.issuperset(A): ", B.issuperset(A)) # True, as B is a superset of A     
print("A.issuperset(C): ", A.issuperset(C)) # False, as A is not a superset of C    
print("C.issuperset(B): ", C.issuperset(B)) # False, as C is not a superset of B    

setA = {1, 2, 3, 4, 5}
setB = {6, 7, 3, 9, 4}
print(setA.symmetric_difference(setB))

set1 = {1, 2, 3}
set2 = {3, 4, 5}

result = set1.symmetric_difference(set2) # Elements in either set1 or set2 but not both
print(result) # {1, 2, 4, 5}        

# Symmetric_diffrence() on a set and a list 
A = {3, 5, 9, 8}
B = [4, 5, 2, 1]

# finding symmetric difference
result = A.symmetric_difference(B) # Elements in either A or B but not both
print(result) # {1, 2, 3, 4, 8, 9}

set_A = {"ram", "rahim", "ajay", "rishav", "aakash"}
set_B = {"aakash", "ajay", "shyam", "ram", "ravi"}
print(set_A ^ set_B)

A = {'p', 'a', 'w', 'a', 'n'}
B = {'r', 'a', 'o', 'n', 'e'}
C = {}

print(A.symmetric_difference(B)) # Elements in either A or B but not both   
print(B.symmetric_difference(A)) # Elements in either A or C but not both

print(A.symmetric_difference(C))
print(B.symmetric_difference(C)) # Elements in either B or C but not both       

A = {'p', 'a', 'w', 'a', 'n'}
B = {'r', 'a', 'o', 'n', 'e'}

# resılt is always None 
result = A.symmetric_difference_update(B) # Elements in either A or B but not both

print("A = ", A)
print("B = ", B)    
print("result = ", result) # None       

A = {'s', 'u', 'n', 'n', 'y'}
B = {'b', 'u', 'n', 'n', 'y'}   

result = A.symmetric_difference_update(B) # Elements in either A or B but not both

print("A = ", A)    
print("B = ", B)
print("result = ", result) # None   

# Python code to demonstrate working of
# symmetric_difference_update()

A = {1, 2, 3, 4, 5, 6}
B = [4, 5, 7, 8]

# passing argument as list

A.symmetric_difference_update(B)
print("A =", A)

A = {2, 4, 6, 8}
B = (i for i in range(2, 6))

# passing argument as generator object

A.symmetric_difference_update(B)
print("A=", A)

# --------------------------------------------------------
s = "Geeksforgeeks"
v = "aeiou"

# Check if each vowel exists in the string 
if all(i in s.lower() for i in v):
    print("All vowels are present in the string")
else:
    print("All vowels are not present in the string")       

s = "Geeksforgeeks" 

# Define set of vowels 
v = set("aeiou")

# Check if all vowels present in the string (case-insensitive)
if v.issubset(set(s.lower())):
    print("All vowels are present in the string")
else:
    print("All vowels are not present in the string")

# USING LOOP 
s = "Geeksforgeeks"
v = "aeiou"
a = set()
# Loop through each character in 's'
for char in s.lower():
    if char in v:
        # add the vowel to the found set 
        a.add(char) 
    if len(a) == 5:
        # If all vowels are found, exit early 
        print("True")
        break 
else:
    print("False")  
#----------------------------------------------------------------------
import re 
s = "Geeksforgeeks" 

# Check if all vowels are present using regex
if re.search(r'(?=.*a)(?=.*e)(?=.*i)(?=.*o)(?=.*u)', s.lower()):
    print("All vowels are present in the string")
else:
    print("All vowels are not present in the string")
#----------------------------------------------------------------------

a = [1, 2, 3, 4, 10]
b = [2, 3, 5, 6, 10]
c = [1, 2, 3, 7, 10]

# Convert lists to sets and find common elements
res = set(a) & set(b) & set(c) 
print(f"Common elements: {res}")

a = [1, 2, 3, 4, 10]
b = [2, 3, 5, 6, 10]
c = [1, 2, 3, 7, 10]

# set comprehension to find common elements     
res = {x for x in a if x in b and x in c}
print(f"Common elements: {res}")

a = [1, 2, 3, 4, 10]
b = [2, 3, 5, 6, 10]
c = [1, 2, 3, 7, 10]

# filter common elements 
res = set(filter(lambda x: x in b and x in c, a))       # Resulting common elements are converted to a set printed as the output
print(f"Common elements: {res}")

#----------------------------------------------------------------------
### Find missing and additional values in two lists 

a = [1, 2, 3, 4, 5, 6]
b = [4, 5, 6, 7, 8]

# missing values in a (values in b but not in a)
missingInA = [x for x in b if x not in a]

# Additional values in a (values in a but not in b)
additionalInA = [x for x in a if x not in b]

# Missing values in b (values in a not in b)
missingInB = [x for x in a if x not in b]

# Additional values in b (values in b not in a)
additionalInB = [x for x in b if x not in a]
print("-------------------------------------------------------")
print("Missing in a:", missingInA)
print("Additional in a:", additionalInA)
print("Missing in b:", missingInB)
print("Additional in b:", additionalInB)

a = [1, 2, 3, 4, 5, 6]
b = [4, 5, 6, 7, 8]

# Convert lists to sets
setA = set(a)   
setB = set(b)   

# Missing values in a (elements in b but not in a)
MissingInA = list(setA - setB)  

# Additional values in a (elements in a but not in b)   
additionalInA = list(setA - setB)

# missing values in b (elements in a but not in b)
MissingInB = list(setB - setA)

# Additional values in b (elements in b but not in a)
additionalInB = list(setB - setA)

print(missingInA)
print(additionalInA)
print(MissingInB)
print(additionalInB)

import numpy as np 

# List 1 and List 2 
a = np.array([1, 2, 3, 4, 5, 6])
b = np.array([4, 5, 6, 7, 8])

# Missing values in a (values in b not in a)    
missingInA = np.setdiff1d(b, a)

# Additional values in a (values in a not in b)
AdditionalInA = np.setdiff1d(a, b)  

# Missing values in a (values in a not in b)
missingInB = np.setdiff1d(a, b) 

# Additional values in b (values in b not in a) 
additionalInB = np.setdiff1d(b, a)      

print("Missing in a:", missingInA)
print("Additional in a:", AdditionalInA)
print("Missing in b:", missingInB)
print("Additional in b:", additionalInB)

# Using loop 
a = [1, 2, 3, 4, 5, 6]
b = [4, 5, 6, 7, 8] 

# Empty lists to store missinf and additional values 
missingInA = [] 
additionalInA = []
missingInB = []
additionalInB = []

# Check for missing and additional values in both lists 
for x in a: 
    if x not in b:
        missingInB.append(x)

for x in b:
    if x not in a:
        missingInA.append(x)
    
print("Missing in a:", missingInA)
print("Additional in a:", additionalInA)
print("Missing in b:", missingInB)
print("Additional in b:", additionalInB)
#-----------------------------------------------------------------

def has_all_letters(s):
    mask = 0
    for char in s.lower():
        if 'a' <= char <= 'z':
            mask |= (1 << (ord(char) - ord('a')))
    return mask == ALL_LATER

ALL_LATER = (1 << 26) - 1   # All letters in bit format 
print(has_all_letters("The quick brown fox jumps over the lazy dog"))

def get_letter_mask(s):
    mask = 0
    for char in s.lower():
        if 'a' <= char <= 'z':
            mask |= (1 << (ord(char) - ord('a')))   
    return mask 

mask = get_letter_mask("Hello")
print(hex(mask))
print("---------------------------------------------------")    

ALL_LATER = (1 << 26) - 1   # All letters in bit format

# Initializes counter c 
c = 0
a = ['abcdefgh', 'geeksforgeeks', 'lmnopqrst', 'abc', 'metehan']
b = ['ijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz', 'defghijklmnopqrstuvwxyz']

for s1 in a: 
    for s2 in b: 
        # Get bitmask representation of s1
        mask1 = 0 
        for char in s1: 
            mask1 |= (1 << (ord(char) - ord('a')))

        # Get bitmask representation of s2      
        mask2 = 0
        for char in s2: 
            mask2 |= (1 << (ord(char) - ord('a')))
        res = mask1 | mask2
        if res == ALL_LATER:
            c += 1

print(c)

# Using set 

a = ['abcdefgh', 'geeksforgeeks', 'lmnopqrst', 'abc', 'metehan', "a"]
b = ['ijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz', 'defghijklmnopqrstuvwxyz']

c = 0
for i in a: 
    for j in b: 
        combine = i + j 
        if len(set(combine)) == 26:
            c += 1
print(c)    

from collections import Counter 

a = ['abcdefgh', 'geeksforgeeks', 'lmnopqrst', 'abc', 'metehan', 'Metehan Gencer']
b = ['ijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz', 'defghijklmnopqrstuvwxyz', 'Embedded Systems'] 

c = 0       # Initialize count
for i in a: 
    for j in b:
        combine = i + j
        char_count = Counter(combine) # Count the characters in the combined string
        if len(char_count) == 26 and all(char_count[chr(k + ord('a'))] > 0 for k in range(26)): # Ensures the combined string has 26 unique character 
            c += 1
print(c)
#-------------------------------------------------------------------------------------------------------------------
# Functions to check whether a given string is Hererogram or not 

def heterogram(input):
    # Separate out list of alphabets using list comprehension 
    # ord function returns ascii value of character
    alphabets = [ch for ch in input if (ord(ch) >= ord('a') and ord(ch) <= ord('z'))]
    # convert list of alphabets into set and compare lenght 
    if len(set(alphabets)) == len(alphabets):
        print('Yes')
    else:
        print('No')

# Driver Program 
if __name__ == "__main__":
    input = "the big dwarf only jumps"
    heterogram(input) # Yes     
#-------------------------------------------------------------------------------------------------------------------
def is_heterogram(string):
    sorted_string = sorted(string.lower())  
    for i in range(1, len(sorted_string)):
        if sorted_string[i] == sorted_string[i - 1] and sorted_string[i].isalpha():
            return 'No'
    return 'Yes'

string = "the big dwarf only jumps" 
print(is_heterogram(string)) # Yes      
print("Mete==", ord("d"))































































                           























































