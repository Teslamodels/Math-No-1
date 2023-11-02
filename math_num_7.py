# The question 👇
# How long does it take a car with speed v to cover distance s?

# The answer 👇

from math import *

v, s = map(int, input("Be Bill Gates in Math\n").split())

T = v / s

print("%.2f" % T)
