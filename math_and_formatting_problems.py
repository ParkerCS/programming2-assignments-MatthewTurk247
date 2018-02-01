# MATH AND FORMATTING (34PTS TOTAL)

# FORMATTING

# PROBLEM 1 (2pts)
# Use {}.format() to print 0.000321192 in scientific notation to two decimals
print("{:.2e}".format(0.000321192))

# PROBLEM 2 (2pts)
# You get 8 out of 9 on a quiz.
# Print 8/9 using {}.format() so that it appears as 88.9%
print("{:.1%}".format(8/9))

# PROBLEM 3 (3pts)
# Take the following program:

score = 41237
highscore = 1023407
print("Score:      " + str(score) )
print("High score: " + str(highscore) )

# Which right now outputs:
# Score:      41237
# High score: 1023407

# Use print formatting so that the output instead looks like:
# Score:          41,237
# High score:  1,023,407
# Make sure the print formatting works for any integer from zero to nine million. Do not use any plus sign (+) in your code.
# You should only have two double quotes in each print statement.

print("Score:      {:,}".format(score))
print("High score: {:,}".format(highscore))

# PROBLEM 4 (5 pts)
# Create a program that loops from 1 to 20 and lists the decimal equivalent of their inverse.
# Use print formatting to exactly match the following output:
# 1/1  = 1.0
# 1/2  = 0.5
# 1/3  = 0.333
# 1/4  = 0.25
# 1/5  = 0.2
# 1/6  = 0.167
# 1/7  = 0.143
# 1/8  = 0.125
# 1/9  = 0.111
# 1/10 = 0.1
# 1/11 = 0.0909
# 1/12 = 0.0833
# 1/13 = 0.0769
# 1/14 = 0.0714
# 1/15 = 0.0667
# 1/16 = 0.0625
# 1/17 = 0.0588
# 1/18 = 0.0556
# 1/19 = 0.0526
# 1/20 = 0.05

for i in range(1, 21):

    if i in [1, 2, 5, 10]:
        print("1/{} = {:.1f}".format(i, 1/i))
    elif i in [4, 20]:
        print("1/{} = {:.2f}".format(i, 1/i))
    elif i in [3, 6, 7, 8, 9]:
        print("1/{} = {:.3f}".format(i, 1/i))
    elif i in [11, 12, 13, 14, 15, 16, 17, 18, 19]:
        print("1/{} = {:.4f}".format(i, 1/i))
    else:
        print("Missed {}".format(i))

# PROBLEM 5 (From Math Class to Code - 5pts)
# Print the answer to the math question:
# 3(60x^2 + 3x/9) + 2x - 4/3(x) - sqrt(x)
# where x = 12.83

x = 12.83
your_answer = 3*(60*x**2 + 3*x/9) + 2*x - 4/3*x - x**1/2  # Substitute your equation for the zero
print(your_answer)

# PROBLEM 2 (Wholesale Books - 5pts)
# The cover price of a book is $27.95, but bookstores get a 50 percent discount.
# Shipping costs $4 for the first copy and 75 cents for each additional copy.
# Calculate the total wholesale costs for 68 copies formatted (using {}.format()) to the nearest penny.

copies = 68
cover_price = 27.95 # dollars
discount = 0.5
shipping = 0.75*(copies - 1) + 4
total = cover_price*(1 - discount)*copies + shipping
print("{:.2f}".format(total))

# PROBLEM 3 (What is this, the ACT? - 5pts)
# You purchase eight chairs for your dining room.
# You pay for the chairs plus sales tax at 9.5%
# Make a program that prints the amount to the nearest penny using the variables below
# Use the round(float, digits) function to get to nearest penny.

chair_price = 189.99
tax_percent = 0.095
units = 8
print(round((1 + tax_percent)*units*chair_price, 2))

# PROBLEM 4 (Variable Swap Logic Problem- 2pts)
# Can you think of a way to swap the values of two variables that does not
# need a third variable as a temporary storage?
# In the code below, try to implement the swapping of the values of 'a' and 'b' without using a third variable.
# To help you out, the first step to do this is already given.
# You just need to add two more lines of code.
# Python has a super simple way to do it as well, but that's not the intention here.  

a = 17
b = 23
print( "a =", a, "and b =", b)
a += b # this is the first line to help you out
# add two more lines of code here to cause swapping of a and b
b = a - b
a -= b
print( "a =", a, "and b =", b)

# PROBLEM 5 (Coin counter - 5pts)
# Write code that classifies a given amount of money (which you store in a variable named count),
# as greater monetary units. Your code lists the monetary equivalent in dollars, quarters,
# dimes, nickels, and pennies.
# Your program should report the maximum number of dollars that fit in the amount,
# then the maximum number of quarters that fit in the remainder after you subtract the dollars,
# then the maximum number of dimes that fit in the remainder after you subtract the dollars and quarters,
# and so on for nickels and pennies.
# The result is that you express the amount as the minimum number of coins needed.

# if put in 1.75, says one dollar, three quarters
count = 103.21
dollars = count//1
print(dollars)
quarters = (count - dollars)//0.25
print(quarters)
dimes = (count - dollars - 0.25*quarters)//0.1
print(dimes)
nickels = (count - dollars - 0.25*quarters - 0.1*dimes)//0.05
print(nickels)
pennies = (count - dollars - 0.25*quarters - 0.1*dimes - 0.05*nickels)//0.01 + 1
print(pennies)
print("You need {} coin(s). {} dollar(s), {} quarter(s), {} dime(s), {} nickels, and {} penny(s).".format(int(quarters + dimes + pennies + nickels), int(dollars), int(quarters), int(dimes), int(nickels), int(pennies)))