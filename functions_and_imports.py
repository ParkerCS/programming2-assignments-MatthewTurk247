import math
import import_me

#FUNCTIONS AND IMPORTS (20PTS TOTAL)
# Be sure to comment all your functions as shown in notes

#PROBLEM 1 (how many upper case - 4pts)
# Make a function takes a string as a parameter, then prints how many upper case letters are contained in the string.
# A loop that compares each letter to the .upper() or .lower() of itself will suffice.

def string_contents(input_string):
    '''
    Prints string info
    :param input_string:
    :return:
    '''
    n_uppercase = 0
    for letter in input_string:
        if letter == letter.upper():
            n_uppercase += 1
    print(n_uppercase)

# PROBLEM 2 (Biggest, smallest, average - 4pts)
# Make a function which takes 3 numbers as parameters.
# The function then prints the largest, the smallest, and their average, rounded to 2 decimals.
# Display the answers in a "nicely" formatted way.

def num_info(n1, n2, n3):
    '''
    Prints number set info
    :param n1:
    :param n2:
    :param n3:
    :return:
    '''
    print("Minimum = {}, maximum = {}, and average = {:.2f}".format(min(n1, n2, n3), max(n1, n2, n3), (n1 + n2 + n3)/3))

# PROBLEM 4 (add me, multiply me - 4pts)
# Make a function which takes in two integers and RETURNS their sum AND their product.

def product_sum(n1, n2):
    '''
    Returns product and sum of two numbers as a tuple
    :param n1:
    :param n2:
    :return:
    '''
    return n1 + n2, n1*n2

# PROBLEM 5 (Login - 4pts)
# Make a file called import_me.py in this same project
# Inside this new module/file, make a login function which works according to the flow diagram PasswordFlowchart.png in this folder
# Substitute your name for Rowan's, and use whatever generic password you want.

# PROBLEM 6 (main - 4pts)
# import the file import_me from Problem 5
# Create a main program using the format if __name__ == "__main__": 
# Place every call from problems 1 through 5 into this program.

if __name__ == "__main__":
    string_contents("Elon Musk")
    num_info(3, 5, 1)
    import_me.login_user("Rowan", "badpassword123")
    print(product_sum(4, 6))

# exceptions, recursion, mathplot library, numpi, bs4, spell check alice in wonderland, tkinter, desktop apps, libraries