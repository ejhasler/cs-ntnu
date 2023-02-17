# Python Indentation
if 5 > 2:
    print("Five is greater than two!")

# Variables
x = 5
y = "Hello world!"

# Creating variables
x = 5
y = "John"
print(x)
print(y)

x = 4       # x is o type int
x = "Sally" # x is now of type string

# Casting
x = str(3)      # x will be '3'
y = int(3)      # y will be 3
z = float(3)    # z will be 3.0

# Get the type
x = 5
y = "John"
print(type(x))
print(type(y))

# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Global Variables
x = "awesome"

def myFunc():
    print("Python is " + x)

myFunc()

print("Python is " + x)

# The global Keyword
def myFunc():
    global x
    x = "fantastic"

myFunc()

print("Python is " + x)

# Python numbers
x = 1       # int
y = 2.8     # float
z = 1j      # complex

print(type(x))
print(type(y))
print(type(z))

# Convert from one type to another
# ------------------------------
x = 1
y = 2.8
z = 1j

# Convert from int to float:
a = float(x)

# Convert from float to int:
b = int(y)

# Convert from int to complex
c = complex(x)

# String are Arrays
a = "Hello World!"
print(a[1])

# Looping Through a String
for x in "banana":
    print(x)

# String length
a = "Hello World"
print(len(a))

# Check String
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

# Check if not
txt = "The best things in life are free!"
print("expensive" not in txt)


