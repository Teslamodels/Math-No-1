# The question 👇
# x, y real numbers are given. If x and y if negative, replace each of them with their modules; if only one is negative, each of the two numbers is 0.5 if both are positive, leave it unchanged.

# The answer 👇

x, y = map(float, input("Fight Night\n").split())

if x < 0 and y < 0:

    print(abs(x), abs(y))

elif x < 0 or y < 0:

    print(x + 0.5, y + 0.5)

else:

    print(x, y)    
