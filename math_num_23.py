# I solve it from the site that created for python developers. In this site have lots of examples and no answer there. I mean when i solved it, i was alone!  
# 👆


# The question 👇
# Calculate the expression.

# The answer 👇

from math import *

a, x = input("Work hard\n").split()

a, x = int(a), float(x)

TT = ((x - 1) ** (1 / 2) + (x + 2) ** (1 / 2) + log10((a * x ** 2) ** (1 / 2) + 2)) / (((x + 2) ** (1 / 2) + (x + 24) ** (1 / 2) + x ** 5) ** (1 / 2))

print("%.2f" % TT)    
