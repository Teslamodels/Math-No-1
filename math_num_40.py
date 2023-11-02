# The question 👇
# a, b, c and d real numbers are given. If a <= b <= c <= d if the inequality holds, then replace each of them with their greater, otherwise replace each of them with their lesser.

# The answer 👇

a, b, c, d = map(float, input("And i achive it\n").split())

f = (a, b, c, d)

x = max(a, b, c, d)

y = min(a, b, c, d)

for i in f:
    
    if a <= b <= c <= d:

        print(x, end=' ')
    
    else:        
        
        print(y)    
