# The question 👇
# Initialize the given sequence Find the sum of n terms: S = (1) / (1!) - (1) / (3!) + (1) / (5!) - (1) / (7!) + ... + (-1) ** (n - 1) * (1) / (2 * n - 1)!

# The answer 👇

from math import *

n = int(input("That was the last. I will back again!\n"))

s = 0

while n > 0:

    s += ((-1) ** (n - 1)) * ((1) / (factorial(2 * n - 1)))
    
    n -= 1

print("%.4f" % s)    
