a = ["Geeks", "for", "Geeks"]

# Iterating list using enumerate to get both index and element
for i, name in enumerate(a):
    print(f"Index {i}: {name}")

# Converting to a list of tuples
print(list(enumerate(a)))
#------------------------------------------------------
a = ["geeks", "for", "geeks"]

# Looping through the list us,ng enumarate starting the index from 1
for index, x in enumerate(a, start=0):
    print(index, x)
print("------------------------------------------")

a = ["geeks", "for", "geeks"]

# Printing the tuples in object directly 
for ele in enumerate(a):
    print(ele)
print("----------------------------------")
mete = ["Metehan", "is an", "Embedded System", "Engineer"]
for ele in enumerate(mete):
    print(ele)
print("-----------------------------")
myFamily = ["Mete", "Fatma", "Efe", "Ela", "Nuran", "Kemal"]
for ele in enumerate(myFamily):
    print(ele)
print("--------------------------------------------------------------")

a = ["Geeks", "for", "geeks"]

# Creating an enumarate object from the list a
b = enumerate(a)

# This retrieves the first index-element pait from 'b'
nxtVal = next(b)
print(nxtVal)
next_element = next(b)
print(next_element)
next_element = next(b)
print(next_element)

myFamily = ["Mete", "HAn", "gencer"]
b = enumerate(myFamily)
nxtVal = next(b)
print("*********************")
print(nxtVal)
nxtVal = next(b)
print(nxtVal)
nxtVal = next(b)
print(nxtVal)

fruits = ['apple', 'banana', 'cherry']
indexed_fruits = [(i, fruit) for i, fruit in enumerate(fruits)]
print(indexed_fruits)

var1 = 4
var2 = 8
var3 = 2
maxVal = max(var1, var2,var3)
print("max value of given variables:", maxVal)
#-----------------------------------------------------------
var1 = "geeks"
var2 = "for"
var3 = "geek"

maxVal = max(var1, var2, var3, key=len)
print(maxVal)
#------------------------------------------------------------
integer = 5
string = 10
maxVal = max(integer, string)
print(maxVal)

list = [1.2, 1.3, 0.1]
maxVal = max(list)
print(maxVal)

# function to find minimum and maximum position in list 
def maximum(a, n):

    # inbuilt funciton to find the position of maximum 
    maxPos = a.index(max(a))

    # printing the position 
    print("The maximum is at position", maxPos+1)

# driver code 
a = [300000, 400, 10, 3, 4, 5]
maximum(a, len(a))

#-----------------------------------------------------------------------
string = "GeeksforGeeks"
maxVal = max(string)
print(maxVal)
#-----------------------------------------------------------------------
stringList = ["zeeks", "bor", "heeks"]
maxVal = max(stringList)
print(maxVal)

dictionary = {}

maxVal = max(dictionary, default={1: "Geek"})
print(maxVal)
#----------------------------------------------------------------------
numbers = [23, 25, 65, 21, 98]
print(min(numbers))
#----------------------------------------------------------------------
print("The min function: ",min(45, 56))

numbers = [3, 2, 8, 5, 10, 6]    # This is a list
small = min(numbers)             # This is a variable which is hold the smallest number given list 
print("The smallest number is: ", small)        # print the value on the screen 

languages = ["python", "C Programming", "Jave", "JavaScript", "PHP", "Kotlin"]
small = min(languages)
print("The smallest string is: ", small)
print("---------------------------------------------")
square = {2: 25, 8: 64, 2: 4, 3: 9, -1: 1, -2: 4}
print("The smallest key:", min(square))
key2 = min(square, key= lambda k: square[k])
print("The smallest value: ", square[key2])
#-----------------------------------------------------
print(min([], default= "No Elements"))
print("---------------------->>", min([2,3,1,4,1]))
print(min((5,3,9,1)))         # Tuples
print(min({7, 2, 8, 3}))      # Sets
print("-------------------------------------------------------------")

# Define a Class
class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def __lt__(self, other):
        return self.age < other.age 

    def __repr__(self):
        return f"{self.name} ({self.age})"

p1 = Person("Alive", 30) 
p2 = Person("bob", 45)
p3 = Person("mete", 200) 

print(min(p1, p2, p3))
#----------------------------------------------------------------
arr = [1, 5, 2, 10]
print(sum(arr))
#-----------------------------------------
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
Sum = sum(numbers)
print(Sum)

Sum = sum(numbers, 100)
print(Sum)

myDict = {"a": 100, "b": 20, "c": 20}
total = sum(myDict.values())
print(total)

#------------------------------------------------------------------
print("-----------------------------------")
mySet = {1, 2, 3, 4, 5}    # set
total = sum(mySet)
print(total)
print("--------------------------------")
myTuple = (1,2,3,4,5)     # tuple
total = sum(myTuple)
print(total)
print("----------------------------------------------")

# Define a list of numbers
def totalNumber():
    numbers = [10, 20, 30, 40, 50]

    # Initialize a variable to store the sum 
    total = 0 

    # Iterate through the list and add each number to the total 
    for num in numbers:
        total += num
    return total

total = totalNumber()
print("Sum of the given numbers:", total)
print("------------------------------------------")
arr = [10, 20]

# Start parameter is not provided 
Sum = sum(arr)
print(Sum)

# Start 10
Sum = sum(arr, 10)
print(Sum)

# Problems where we require to be calculated to de further operations such as finding out the average of numbers

numbers = [1, 1, 1, 1, 1, 1, 1]

Sum = sum(numbers)
average = Sum / len(numbers)
print("The average of the given list:", average)

a = [4, 1, 3, 2]

# using sorted function to modify list in-place
b = sorted(a)
print(b)

a = [5, 2, 9, 1, 3]

# "reverse= True" helps sorted() to arrange the element from largest to smallest elements 
res = sorted(a, reverse=True)
print(res)
print("-------------------------------------------------")
a = ["apple", "banana", "cherry", "date"]
res = sorted(a, key=len)
print(res)
#-----------------------------------------------------------------
a = [
    {"name": "Mete", "score": 78},
    {"neme": "Bob", "score": 52},
    {"name": "ali", "score": 45}
]

# Use sorted() to sort the list 'a' based on the "score" key
# sorted() returns a new list with the dictionaries sorted by the "score"
b = sorted(a, key=lambda x: x['score'], reverse=True)
print(b)
#-------------------------------------------------------
l = [1,2,3]
print(tuple(l))
#------------------------------
# When parameter in not passed 
tuple1 = tuple()
print("empty tuple:",tuple1)

# when an iterable (e.g., list) is passed 
list1 = [1,2,3,4,5]
tuple2 = tuple(list1)
print("list to tuple:", tuple2)

# When an iterable (e.g., string) is passed 
string = "metehangencer is an Embedded system Engineer"
tuple3 = tuple(string)
print("str to tuple:", tuple3)
print("-----------------------------------------")

myDict = {"apple": 1, "banana": 2, "cherry": 3}
myTuple = tuple(myDict.items())
print(myTuple)
#-------------------------------------------------------
myTuple = tuple((1,2,3))
print(myTuple)
print("min= ", min(myTuple))
#------------------------------------------------------
myTuple = tuple((1,2,3))
print(sum(myTuple))
print("-----------------------------------------")
myTuple = tuple((37,25,14))
sortedTuple = tuple(sorted(myTuple, reverse=True))
print(sortedTuple)
print("------------------------------------------------")
myDict = {"a": 1, "b": 2, "c": 3}
myTuple = tuple(myDict)
print(myTuple)
originalTuple = (1,2,3,4,5)
newTuple = tuple(originalTuple)
print(newTuple)
#------------------------------------------------------------------------------

# Python program to Print unique rows in a
# given boolean matrix using Set with tuples

# Function to print unique rows in a given boolean matrix

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






















































































































