import math

def sphere_volume(radius):
    volume = (4/3) * math.pi * radius**3
    print(f"Volume of sphere with radius {radius}: {volume:.2f}")

sphere_volume(5)