# The question 👇
# a, b, c are given integers (a not zero). Obviously, a * x ** 2 + b * x + c = 0 whether the quadratic equation has a real solution. If there are real solutions, find them. Otherwise "NO" say the word.

# The answer 👇

import math

a, b, c = map(int, input("USA is a dream!\n").split())

a != 0

D = (b ** 2) - (4 * a * c)

if D < 0:
    
    print("NO")

else:
    
    x1 = (-b + math.sqrt(D)) / (2 * a)
    
    x2 = (-b - math.sqrt(D)) / (2 * a)
    
    print("%.2f %.2f" % (x1, x2))    
