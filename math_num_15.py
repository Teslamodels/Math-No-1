# I solve it from the site that created for python developers. In this site have lots of examples and no answer there. I mean when i solved it, i was alone!  
# 👆


# The question 👇
# Calculate the expression.


# The answer 👇

from math import *

x, y = map(float, input("Math is real\n").split())

c1 = (x + y) / (y ** 2 + abs((y ** 2 + 2) / (x + (x ** 3) / (5)))) + e ** (y + 2)

print("%.2f" % c1)    
