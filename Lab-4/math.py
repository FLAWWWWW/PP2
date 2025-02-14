import math

# TASK 1
'''
degree = int(input("Input degree: "))
print("Output radian: ", math.radians(degree))
'''

# TASK 2
'''
def trapezoid_area(b1, b2, h):
    return ((b1 + b2) / 2) * h

height = int(input("Height: "))
first_base = int(input("Base, first value: "))
second_base = int(input("Base, second value: "))
print("Expected Output: ", trapezoid_area(first_base, second_base, height))
'''

# TASK 3
'''
num_sides = int(input("Input number of sides: "))
length = int(input("Input the length of a side: "))
print("The area of the polygon is: ", math.floor((num_sides * length * length) / (4 * math.tan(math.radians(180 / num_sides)))))
# floor - к наименьшему
# ceil - к ближайшему
'''

# TASK 4
'''
def parallelogram_area(len, hei):
    return len * hei

len = int(input("Length of base: "))
hei = int(input("Height of parallelogram: "))
print("The area of the polygon is: ", parallelogram_area(len, hei))
'''