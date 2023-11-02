# The question 👇
# Initialize the given sequence Find the sum of n terms: S = (sin(1 ** 1)) / (2 ** 1) - (sin(2 ** 2)) / (2 ** 2) + ... + (-1) ** (n - 1) * (sin(n ** n)) / (2 ** n).

# The answer 👇

from math import *

n = int(input("No love\n"))

s = 0

while n > 0:

    s += ((-1) ** (n - 1)) * ((sin(n ** n)) / (2 ** n))

    n -= 1
    
print("%.2f" % s)    
