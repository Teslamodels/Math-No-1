# I solve it from the site that created for python developers. In this site have lots of examples and no answer there. I mean when i solved it, i was alone!  
# 👆


# The question 👇
# Calculate the expression.

# The answer 👇

from math import *

x, y = map(float, input("Never give up!\n").split())

numerator_and_denominator = 2 * tan(x + pi / 6) / 1 / 3 + cos(y + x ** 2) ** 2 + log2(x ** 2 + 2)

print("%.2f" % numerator_and_denominator)    

