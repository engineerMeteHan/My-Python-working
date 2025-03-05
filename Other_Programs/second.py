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

# Simple list of integer 
list = [1, 2, 3, 4]

# iterable as source
array = bytearray(list)

print(array)
print("Count of bytes: ", len(array))

# Array of size 
 # will be creates
                                                # Metehan GENCER 

array = bytearray()
print(array)
















































