# I solve it from the site that created for python developers. In this site have lots of examples and no answer there. I mean when i solved it, i was alone!  
# 👆


# The question 👇
# Calculate the expression.

# The answer 👇

from math import cos

a, b, c, d, x = input("Have a smart brain\n").split()

a, b, c, d = int(a), int(b), int(c), int(d)

x = float(x)

try:
  y2 = (a * x ** 2 + b * x + c) / (x * a ** 3 + a ** 2 + a ** (b - c)) + cos(abs((a * x + b) / (c * x + d + 2 ** c)))
  
  print("%.2f" % y2) 

except ZeroDivisionError:
  print("%.2f" % 1) 
