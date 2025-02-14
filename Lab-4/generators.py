import math

# TASK 1
'''
def gen_num(n):
    value = 1
    while value * value <= n:
        yield value * value
        value += 1


n = int(input("Input n : "))

for value in gen_num(n):
    print(value)
'''

# TASK 2
'''
def gen_even_num(n):
    value = 0
    while value <= n:
        yield value
        value += 2


n = int(input("Input n : "))

for value in gen_even_num(n):
    print(f"{value}, ", end="")
'''

# TASK 3
'''
def gen_div_num(n):
    value = 1
    while value <= n:
        if value % 3 == 0 and value % 4 == 0:
            yield value
        value += 1


n = int(input("Input n : "))

for value in gen_div_num(n):
    print(value)
'''

# TASK 4
'''
def squares(a, b):
    value = a
    while value <= b:
        yield value * value
        value += 1


a = int(input("Input a : "))
b = int(input("Input b : "))

for value in squares(a, b):
    print(value)
'''

# TASK 5
def gen_num(n):
    value = n
    while value >= 0:
        yield value
        value -= 1


n = int(input("Input n : "))

for value in gen_num(n):
    print(value)