# The question 👇
# Given an integer x, y (x and y are not equal). Replace the smaller one with their half sum, and the bigger one with their double product.

# The answer 👇

x, y = map(float, input("Work in Google!\n").split())

x != y

if x > y:

    print(x * 2 * y * 2 , (x + y) / 2)

elif x < y:

    print((x + y) / 2, x * 2 * y * 2)    
