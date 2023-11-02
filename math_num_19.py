# I solve it from the site that created for python developers. In this site have lots of examples and no answer there. I mean when i solved it, i was alone!  
# 👆


# The question 👇
# Calculate the expression.

# The answer 👇

from math import *

a, b = map(float, input("Belive in yourself\n").split())

T = ((a) ** (1 / 5)) + (b * (a + b) / (2 * b + a * b)) ** (1 / 4) * (a ** 2 + b ** 2 + 2)

print("%.2f" % T)
