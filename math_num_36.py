# The question 👇
# Given three real numbers. Of them Select those that belong to the interval [1, 3].

# The answer 👇

def belong_to_the_interval(numbers, interval):
    
    are_related = []

    for number in numbers:

        if number >= interval[0] and number <= interval[1]:

            are_related.append(number)

    return are_related

numbers = map(float, input("Too long, yeah?\n").split())

interval = (1, 3)

are_related = belong_to_the_interval(numbers, interval)

print(*are_related)    
