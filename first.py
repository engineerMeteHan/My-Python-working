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



































































































    










































































