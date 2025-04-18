# 3. Create a program that prompts for the side lengths of a triangle and computes the area using Heron's formula. (https://en.wikipedia.org/wiki/Heron%27s_formula)
import math
a = float(input("What is the length of side A? "))
b = float(input("What is the length of side B? "))
c = float(input("What is the length of side C? "))
semi = (a+b+c)/2
area = math.sqrt(semi * (semi-a) * (semi-b) * (semi-c))
print(f"The area of this triangle is: {area}")
