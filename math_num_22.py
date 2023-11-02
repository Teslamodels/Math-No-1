# I solve it from the site that created for python developers. In this site have lots of examples and no answer there. I mean when i solved it, i was alone!  
# 👆


# The question 👇
# Calculate the expression.

# The answer 👇

from math import *

a, b, c, x = input("Work smart\n").split()

a, b, c, x = int(a),int(b),int(c), float(x)

W1 = 0.75 +(8.2 * x ** 2 + (abs(x ** 3 + 3 * x) + cos(x - 2)) ** (1 / 2)) / ((a / 4) + (b / 3) + (c / 2) + 1)

print("%.2f" % W1)
