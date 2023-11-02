# The question 👇
# given an integer. Replace the first number with zero, if it is less than or equal to the second, otherwise leave it unchanged.

# The answer 👇

a, b = map(int, input("Senior\n").split())

if a <= b:

    print(0, b)
    
else:
    print(a, b)    

