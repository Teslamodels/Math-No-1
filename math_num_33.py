# The question 👇
# a, b and c an integer is given. If c <= b <= a if the inequality holds, then double the numbers, otherwise replace them with their module.

# The answer 👇

from math import *

a, b, c = map(int, input("Focus on your Goals\n").split())

if c <= b <= a:

    print(a + a, b + b, c + c)
    
else:
    print(abs(a), abs(b), abs(c))    
