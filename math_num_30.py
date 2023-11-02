# The question 👇
# x, y and z given a real number. Calculate: max(x, y, z) and min(x, y, z).

# The answer 👇

from math import *

x, y, z = map(float, input("Gigant brain!\n").split())

a = max(x, y, z)

b = min(x, y, z)

print(a, b)    
