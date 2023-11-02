# I solve it from the site that created for python developers. In this site have lots of examples and no answer there. I mean when i solved it, i was alone!  
# 👆


# The question 👇
# Calculate the expression.

# The answer 👇

from math import *

x, y = map(int, input("I'm genius in math!\n").split())

a = log(abs((x + y) ** 2 + (abs(y) + 2) ** (1 / 2) - (x - (x * y) / ((x ** 2 / 2) - 5)))) + cos(x + y) ** 2 / (x + y) ** (1 / 3)

print("%.2f" % a)
