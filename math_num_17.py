# I solve it from the site that created for python developers. In this site have lots of examples and no answer there. I mean when i solved it, i was alone!  
# 👆


# The question 👇
# Calculate the expression.

# The answer 👇

from math import *

x, y = map(float, input("Solve it in Silence!\n").split())

f2 = (((1) / (x + (2 / x ** 2) + (3 / x ** 3)) + e ** (x ** 2 + 3 * x)) / (atan(x + y) + abs(5 + x) ** 2)) - cos(y ** 2 + (x ** 2 / 2)) ** 2

print("%.2f" % f2)    

