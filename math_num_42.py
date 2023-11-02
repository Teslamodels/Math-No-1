# The question 👇
# x, y, z are given positive integers. Is there a triangle with sides of length x,y,z? YES if applicable otherwise "NO" say the word.

# The answer 👇

x, y, z = map(int, input("Don't be scared! Just do it\n").split())

if x + y > z and y + z > x and x + z > y:

    print("YES")

else:

    print("NO")    

