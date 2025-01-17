# --- Python Variables ---
'''
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

str_1 = "John"
# is the same as
str_2 = 'John'

print(type(y))

a = 4
A = "Sally"
#A will not overwrite a
'''

'''
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
'''

# Camel Case
myVariableName = "John"

# Pascal Case
MyVariableName = "John"

# Snake Case
my_variable_name = "John"

# Many Values to Multiple Variables
'''
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
'''

# One Value to Multiple Variables
'''
x = y = z = "Orange"
print(x)
print(y)
print(z)
'''

# Unpack a Collection
'''
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
'''

# --- Output Variables ---

'''
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
'''

'''
x = 5
y = 10
print(x + y)
'''

'''
x = 5
y = "John"
print(x, y)
'''

# --- Global Variables ---
'''
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
'''

'''
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
'''


