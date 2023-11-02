# The question 👇
# Given three integers. Replace their positive with its square.

# The answer 👇

x, y, z = map(int, input("Work in Amazon\n").split())

if x > 0:

    a = x ** 2

else:

    a = x

if y > 0:

    b = y ** 2

else:

    b = y

if z > 0:

    c = z ** 2

else:
    
    c = z

print(a, b, c)    
