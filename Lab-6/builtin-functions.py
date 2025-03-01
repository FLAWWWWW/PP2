from functools import reduce
import operator
from operator import eq
import time
import math

# TASK 1

print(reduce(operator.mul, (6, 4, 5))) # operator.mul - оператор умножения, reduce берёт первые два элемента листа, работает с ними и потом с этим значением переходит к третьему элементу и тд

# TASK 2

str = "HeLLo"
print("Num of Upper Case Letters :", sum(map(lambda x: x.isupper(), str)),  
      "\nNum of Lower Case Letters :", sum(map(lambda x: x.islower(), str)))

# TASK 3

str_2 = "abba"

print("Is palindrome : ", reduce(lambda x, y : x and y, (map(eq, str_2, reversed(str_2)))))

# TASK 4

print("Sample Input : ") 
number = int(input()) # 25100

ms = int(input()) # 2123

time.sleep(ms / 1000) # конвертируем в секунды для функциии

result = math.sqrt(number)

print(f"Square root of {number} after {ms} milliseconds is {result}")

# TASK 5

tup = (1, True, 0, False)
print("Is all True in Tuple : ", all(tup))