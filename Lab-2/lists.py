# --- List ---

# Allow duplicates
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)


# Access Items
print(thislist[1])

print(thislist[-1])

print(thislist[2:5])

#not including fourth
print(thislist[:4])

#include second (third)
print(thislist[2:])


# Change Item Value
thislist[1] = "blackcurrant"
print(thislist)

thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#replacing with TWO new values
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#replacing to ONE value
thislist[1:3] = ["watermelon"]
print(thislist)


# --- Add List Items ---
thislist.append("orange")
print(thislist)

thislist.insert(1, "orange")
print(thislist)

usual = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
usual.extend(tropical)
print(usual)

list = ["apple", "banana", "cherry"]
tuple = ("kiwi", "orange")
list.extend(tuple)
print(list)


# --- Remove List Items ---

# Remove the first occurrence of "banana"
thislist.remove("banana")
print(thislist)

thislist.pop(1)
print(thislist)

# Remove the last item
thislist.pop()
print(thislist)

del thislist[0]
print(thislist)

# Delete the entire list
'''del thislist'''

# Clear the list content
thislist.clear()
print(thislist)

# newlist = [expression for item in iterable if condition == True]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
newnewlist = [x.upper() for x in fruits]
newnewnewlist = ['hello' for x in fruits]

numlist = [x for x in range(10) if x < 5]


# Sort Lists
thislist.sort()
print(thislist)

thislist.sort(reverse = True)
print(thislist)

# Copy Lists
mylist = thislist.copy()
print(mylist)

mylist = list(thislist)
print(mylist)

mylist = thislist[:]
print(mylist)

# Join Two Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
'''list1.extend(list2)'''
print(list3)

# --- List Methods ---

#append()	    Adds an element at the end of the list
#clear()	    Removes all the elements from the list
#copy()	        Returns a copy of the list
#count()	    Returns the number of elements with the specified value
#extend()	    Add the elements of a list (or any iterable), to the end of the current list
#index()	    Returns the index of the first element with the specified value
#insert()	    Adds an element at the specified position
#pop()	        Removes the element at the specified position
#remove()	    Removes the item with the specified value
#reverse()	    Reverses the order of the list
#sort()	        Sorts the list