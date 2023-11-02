# The question 👇
# given a real number. y(x) shown in the figures below for the function y(a) calculate the.

# The answer 👇

a = float(input("Work in ebay\n"))

if a >= 2:
    
    y = 4

elif -1 < a < 2:

    y = a ** 2

elif a <= -1:

    y = 1 / (a ** 2)
    
print("%.2f" % y)    
