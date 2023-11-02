# The question 👇
# The first n of the given sequence find the sum of the: S = (sin(1)) / (2 ** 1) + (sin(2)) / (2 ** 2) + ... + (sin(n)) / (2 ** n).

# The answer 👇

from math import *

n = int(input("My dream is too big\n"))

s = 0

while n > 0:

    s += (sin(n)) / (2 ** n)

    n -= 1

print("%.2f" % s)    
