# Unchangeable!

# Allow duplicates
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# Access is the same as in lists 
print(thistuple[1])

# --- Update Tuples ---

# Convert to list

# Change
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# Add
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

# Tuple to tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

# --- Unpack Tuples ---
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

# Using Asterisk
(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)


# --- Join Tuples ---

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)



fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)


# --- Methods ---

#count()	Returns the number of times a specified value occurs in a tuple
#index()	Searches the tuple for a specified value and returns the position of where it was found