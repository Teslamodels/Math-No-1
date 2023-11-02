# The question 👇
# x, y and z float numbers is given. Calculate: max(x + y + z, x, y, z) and min ** 2(x + y / 2, x, y, z)

# The answer 👇

from math import *

x, y, z = map(float, input("Be 100% productive!").split())

a = max(x + y + z, x, y, z)

b = min(x + y / 2, x, y, z) ** 2

print("%.2f %.2f" % (a, b))    
