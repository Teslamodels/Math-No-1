# I solve it from the site that created for python developers. In this site have lots of examples and no answer there. I mean when i solved it, i was alone!  
# 👆


# The question 👇
# Calculate the expression.

# The answer 👇

from math import *

a, x, y = input("Work hard and work smart\n").split()

a, x, y = int(a), float(x), float(y)

W2 = (e ** (x * y) - x * sin(a * x) - ((x ** 2 + 2) / (abs(x) + 5))) ** (1 / 2) + (log(x ** 2 + 2) + 5) ** (1 / 2)

print("%.2f" % W2)    
