# The question 👇
# Three angles with sides a, b and c are given. Find the half perimeter of the triangle.

# The answer 👇

from math import *

a, b, c = map(int, input("Use your brain\n").split())

P = (a + b + c) * 0.5

print("%.2f" % P)

