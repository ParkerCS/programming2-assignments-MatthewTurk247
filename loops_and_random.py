import random

# LOOPS (16pts TOTAL)

# PROBLEM 1 (Fibonacci - 4pts)
# The Fibonacci sequence is a sequence of numbers that starts with 1, followed by 1 again.
# Every next number is the sum of the two previous numbers.
# I.e., the sequence starts with 1, 1, 2, 3, 5, 8, 13, 21,...
# Write a program that calculates and prints the Fibonacci sequence
# until the numbers get higher than 1000.
# n = 1

previous_number = -1
current_number = 0

for i in range(1, 1001):
    n = current_number
    current_number += previous_number
    previous_number = n
    # also check out this neat formula that works too!
    fib = (((1 + 5 ** (1 / 2)) / 2) ** i - ((1 - 5 ** (1 / 2)) / 2) ** i) / 5 ** (1 / 2)
    # print(round(fib))
    print(-current_number)

# PROBLEM 2 (Dice Sequence - 6pts)
# You roll five six-sided dice, one by one.
# What is the probability that the value of each die
# is greater than OR EQUAL TO the value of the previous die that you rolled?
# For example, the sequence “1, 1, 4, 4, 6” is a success,
# but “1, 1, 4, 3, 6” is not. Determine the
# probability of success using a simulation of a large number of trials.

a = 0
b = 500
die = random.randrange(6)
f = 0
while f <= 100:
    for i in range(6):
        new_die = random.randrange(6)
        if new_die >= die:
            a += 1
        die = new_die
    if f == 0:
        print("Probability: {}%".format(10000*a/b))
    f += 1

print("Probability after many trials: {}%".format(100*a/b))

# PROBLEM 3 (Number Puzzler - 6pts)
# A, B, C, and D are all different digits.
# The number DCBA is equal to 4 times the number ABCD.
# What are the digits?
# Note: to make ABCD and DCBA conventional numbers, neither A nor D can be zero.
# Use a quadruple-nested loop to solve.

digit_1 = 0
digit_2 = 0
digit_3 = 0
digit_4 = 0


def is_unique(x):
    seen = set()
    return not any(i in seen or seen.add(i) for i in x)


for a in range(1000):
    digit_1 = random.randrange(10)
    for b in range(10):
        digit_2 = random.randrange(10)
        for c in range(10):
            digit_3 = random.randrange(10)
            for d in range(10):
                digit_4 = random.randrange(10)
                if is_unique([digit_1, digit_2, digit_3, digit_4]):
                    if digit_1 != 0 and digit_4 != 0:
                        ABCD = 1000*digit_1 + 100*digit_2 + 10*digit_3 + digit_4
                        DBCA = 1000*digit_4 + 100*digit_3 + 10*digit_2 + digit_1
                        print(ABCD)
                        print(DBCA)
                        if DBCA == 4*ABCD:
                            print("Found it. A = {}, B = {}, C = {}, and D = {}".format(digit_1, digit_2, digit_3, digit_4))
                            # Eventually prints "Found it. A = 2, B = 1, C = 7, and D = 8"