#problem3, this one took me so long! Turns out I multiplied instead of subtracted lol.
import math
a = float(input("What is the length of side A? "))
b = float(input("What is the length of side B? "))
c = float(input("What is the length of side C? "))
semi = (a+b+c)/2
area = math.sqrt(semi * (semi-a) * (semi-b) * (semi-c))
print(f"The area of this triangle is: {area}")
