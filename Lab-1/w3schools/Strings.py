
# --- Python Strings ---

# Quotes Inside Quotes
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

# Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.""" # or three single quotes
print(a)
#Note: in the result, the line breaks are inserted at the same position as in the code.


# --- Slicing Strings ---

b = "Hello, World!"
print(b[2:5])

# Slice From the Start
b = "Hello, World!"
print(b[:5])

# Slice To the End
b = "Hello, World!"
print(b[2:])

# Negative Indexing
b = "Hello, World!"
print(b[-5:-2])


# --- Modify Strings ---

# Upper Case
a = "Hello, World!"
print(a.upper())

# Lower Case
a = "Hello, World!"
print(a.lower())

# Remove Whitespace
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# Replace String
a = "Hello, World!"
print(a.replace("H", "J"))

# Split String
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

# String Concatenation
a = "Hello"
b = "World"
c = a + " " + b
print(c)

# F-Strings

age = 36
txt = f"My name is John, I am {age}"
print(txt) 

# A placeholder can contain variables, operations, functions, and modifiers to format the value.

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)

# --- Escape Character ---

txt = "We are the so-called \"Vikings\" from the north."

txt = 'It\'s alright.' #Single Quote

txt = "This will insert one \\ (backslash)." #Backslash

txt = "Hello\nWorld!" #New Line

txt = "Hello\rWorld!" #Carriage Return

txt = "Hello\tWorld!" #Tab

txt = "Hello \bWorld!" #Backspace

txt = "\110\145\154\154\157" #Octal value

txt = "\x48\x65\x6c\x6c\x6f" #Hex value


# --- String Methods ---

name = "Flaw"

name.capitalize()	#Converts the first character to upper case

name.casefold()	#Converts string into lower case

name.center()	#Returns a centered string

name.count()	#Returns the number of times a specified value occurs in a string

name.encode()	#Returns an encoded version of the string

name.endswith()	#Returns true if the string ends with the specified value

name.expandtabs()	#Sets the tab size of the string

name.find()	#Searches the string for a specified value and returns the position of where it was found

name.format()	#Formats specified values in a string

name.format_map()	#Formats specified values in a string

name.index()	#Searches the string for a specified value and returns the position of where it was found

name.isalnum()	#Returns True if all characters in the string are alphanumeric

name.isalpha()	#Returns True if all characters in the string are in the alphabet

name.isascii()	#Returns True if all characters in the string are ascii characters

name.isdecimal()	#Returns True if all characters in the string are decimals

name.isdigit()	#Returns True if all characters in the string are digits

name.isidentifier()	#Returns True if the string is an identifier

name.islower()	#Returns True if all characters in the string are lower case

name.isnumeric()	#Returns True if all characters in the string are numeric

name.isprintable()	#Returns True if all characters in the string are printable

name.isspace()	#Returns True if all characters in the string are whitespaces

name.istitle()	#Returns True if the string follows the rules of a title

name.isupper()	#Returns True if all characters in the string are upper case

name.join()	#Joins the elements of an iterable to the end of the string

name.ljust()	#Returns a left justified version of the string

name.lower()	#Converts a string into lower case

name.lstrip()	#Returns a left trim version of the string

name.maketrans()	#Returns a translation table to be used in translations

name.partition()	#Returns a tuple where the string is parted into three parts

name.replace()	#Returns a string where a specified value is replaced with a specified value

name.rfind()	#Searches the string for a specified value and returns the last position of where it was found

name.rindex()	#Searches the string for a specified value and returns the last position of where it was found

name.rjust()	#Returns a right justified version of the string

name.rpartition()	#Returns a tuple where the string is parted into three parts

name.rsplit()	#Splits the string at the specified separator, and returns a list

name.rstrip()	#Returns a right trim version of the string

name.split()	#Splits the string at the specified separator, and returns a list

name.splitlines()	#Splits the string at line breaks and returns a list

name.startswith()	#Returns true if the string starts with the specified value

name.strip()	#Returns a trimmed version of the string

name.swapcase()	#Swaps cases, lower case becomes upper case and vice versa

name.title()	#Converts the first character of each word to upper case

name.translate()	#Returns a translated string

name.upper()	#Converts a string into upper case

name.zfill()	#Fills the string with a specified number of 0 values at the beginning

#Note: All string methods return new values. They do not change the original string.
