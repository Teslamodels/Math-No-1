# The question 👇
# a, b and c are given integers. Check: a < b < c does the inequality hold? "YES" if the inequality holds otherwise "NO" say the word.

# The answer 👇

from math import *

a, b, c = map(int, input("The life is good\n").split())

if a < b < c:
    
    print("YES")
    
else:
    print("NO")    
