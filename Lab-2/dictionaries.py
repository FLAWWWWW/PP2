thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}

x = thisdict.get("model")
y = thisdict.keys()
z = thisdict.values()
a = thisdict.items()

print(thisdict)

thisdict["model"] = "Not Mustang"
thisdict.update({"year": 2020})

print(thisdict["brand"])

# Adding Items
thisdict["color"] = "red"

thisdict.update({"color": "red"})

# Removing Items
thisdict.pop("model")
print(thisdict)

thisdict.popitem()
print(thisdict)

del thisdict["model"]
print(thisdict)

thisdict.clear()
print(thisdict)

# Copy a Dictionary
mydict = thisdict.copy()
print(mydict)

'''
mydict = dict(thisdict)
print(mydict)
'''

# Nested Dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

'''
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
'''

#clear()	      Removes all the elements from the dictionary
#copy()	        Returns a copy of the dictionary
#fromkeys()	    Returns a dictionary with the specified keys and value
#get()	        Returns the value of the specified key
#items()	      Returns a list containing a tuple for each key value pair
#keys()	        Returns a list containing the dictionary's keys
#pop()	        Removes the element with the specified key
#popitem()	    Removes the last inserted key-value pair
#setdefault()	  Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
#update()	      Updates the dictionary with the specified key-value pairs
#values()	      Returns a list of all the values in the dictionary