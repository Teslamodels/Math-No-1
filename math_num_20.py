# I solve it from the site that created for python developers. In this site have lots of examples and no answer there. I mean when i solved it, i was alone!  
# 👆


# The question 👇
# Calculate the expression.

# The answer 👇

from math import *

x1, x2, c, d = input("Enjoy life\n").split()

x1, x2, c, d = float(x1), float(x2), int(c), int(d)

F = abs((sin(abs(c * x2 ** 3 + d * x1 ** 3 - c * d)) ** 2) / ((c * x1 ** 2 + d * x2 ** 2 + 7) ** (1 / 2))) + tan(x1 * x2 ** 2 + d ** 3)

print("%.2f" % F)    
