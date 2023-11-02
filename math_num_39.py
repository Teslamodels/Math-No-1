# The question 👇
# If mutually different x, y, z if the real numbers are less than one, then replace the smallest of these three numbers with half the sum of the other two. Otherwise, leave it unchanged.

# The answer 👇

x, y, z = map(float, input("I have a big dream!\n").split())

if x < 1 and y < 1 and z < 1:

    mn = min(x, y, z)

    if x == mn:

        x = (y + z) / 2

    elif y == mn:

        y = (x + z) / 2

    else:

        z = (x + y) / 2

print(x, y, z)    
