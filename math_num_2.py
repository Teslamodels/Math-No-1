# The question 👇
# The radii of 3 circles with radii r1, r2, r3 are given. Count the faces of the circles.

# The answer 👇

from math import *

r1, r2, r3 = map(int, input("It's so easy, bro\n").split())

formula_1 = pi * r1 ** 2
formula_2 = pi * r2 ** 2
formula_3 = pi * r3 ** 2

print("%.2f %.2f %.2f" % (formula_1, formula_2, formula_3))

