# The question 👇
# If the height of the cone is h and the radius is r, what is its volume?

# The answer 👇

from math import *

h, r = map(int, input("Have a long patience\n").split())

V = 1 / 3 * pi * h ** 2 * r

print("%.2f" % V) 
