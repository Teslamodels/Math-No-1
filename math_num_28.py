# I solve it from the site that created for python developers. In this site have lots of examples and no answer there. I mean when i solved it, i was alone!  
# 👆


# The question 👇
# Calculate the expression.

# The answer 👇

from math import *

x, y, z = input("This is Elon Musk!\n").split()

x, y, z = int(x), float(y), float(z)

AF = pow(2, -x) * (x + (abs(y) + 2) ** (1 / 4)) ** (1 / 2) * (e ** (x - 1) / sin(z + 2) + 2) ** (1 / 3)

print("%.2f" % AF)    

