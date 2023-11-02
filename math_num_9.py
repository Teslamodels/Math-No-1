# The question 👇
# If 1 milliliter of water drips from the tap in 1 s, how many liters of water drips in x years.

# The answer 👇

x = int(input("Be Careful\n"))

s = (x * 365 * 24 * 60 * 60) * (1 / 1000)

print("%.0f" % s) 
