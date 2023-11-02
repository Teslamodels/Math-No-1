# The question 👇
# R1, R2 and R3 of the circuit resistors are connected in parallel. Find their total resistance.

# The answer 👇

R1, R2, R3 = map(int, input("It's just a radius\n").split())

x = (R1 * R2 * R3) / ((R1 * R2) + (R1 * R3) + (R2 * R3))

print("%.2f" % x)    
