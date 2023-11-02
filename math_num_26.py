# I solve it from the site that created for python developers. In this site have lots of examples and no answer there. I mean when i solved it, i was alone!  
# 👆


# The question 👇
# Calculate the expression.

# The answer 👇

from math import *

a, x = input("Python is so good\n").split()

a, x = int(a), float(x)

BB1 = x * sin(x / 2 + x / 3 + x / 4) + (log10(x ** 2 - 2) + 3 ** a) / (cos(x + 3) * sin(x + 3) + 8)

print("%.2f" % BB1)    
