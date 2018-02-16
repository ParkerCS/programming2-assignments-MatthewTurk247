import random

'''
Grid Printer Exercise
Printing a Grid (adapted from Downey, “Think Python”, ex. 3.5)
Goal:
Write a function that draws a grid like the following:
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
hints
A couple features to get you started...
use print("+", end = " ") to print continuous line without carriage return
A print function with no arguments ends the current line and goes to the next line:
Simple string manipulation:
You can put two strings together with the plus operator:
"this" + "that" ===>  'thisthat'
Particularly useful if they have been assigned names:
plus = '+'
minus = '-'
You can also multiply strings:
'+' * 10 ===> '++++++++++'

'''

for row in range(11):
    if row % 5 != 0:
        for column in range(1):
            print("|            |            |")
    else:
        print("+" + " - "*4 + "+" + " - "*4 + "+")

'''
Part 2
Making it more general
Make it a function
One of the points of writing functions is so you can write code that does similar things, but customized to input parameters. So what if we want to be able to print that grid at an arbitrary size?
Write a function print_grid(n) that takes one integer argument and prints a grid just like before, BUT the size of the grid is given by the argument.
For example,
print_grid(3) would print a small grid:
+ - + - +
|   |   |
+ - + - +
|   |   |
+ - + - +
print_grid(15) prints a larger grid:
+ - - - - - - - + - - - - - - - +
|               |               |
|               |               |
|               |               |
|               |               |
|               |               |
|               |               |
|               |               |
+ - - - - - - - + - - - - - - - +
|               |               |
|               |               |
|               |               |
|               |               |
|               |               |
|               |               |
|               |               |
+ - - - - - - - + - - - - - - - +
'''

'''def print_grid(n):
    for row in range(n):
        if row % 2*n != 0:
            for column in range(n):
                print("|" + " "*3*n + "|" + " "*3*n + "|")
        else:
            print("+" + " - " * n + "+" + " - " * n + "+")

print_grid(4)'''

def print_grid(n):
    for row in range(round(n/4) - 1):
        print("+", end="")
        print(" - " * (round(n/8)), end="")
        print("+", end="")
        print(" - " * (round(n/8)), end="")
        print("+")
        print("|" + " " * round(n/2.5) + "|", end="")
        print(" " * round(n / 2.5) + "|")
    print("+", " - " * (round(n/8)), "+", " - " * round(n/8), "+", sep="")

# searching and sorting

print_grid(50)

'''
Part 3:
Even more general...
A function with two parameters
Write a function that draws a similar grid with a specified number of rows and columns, and each cell a given size.
for example, print_grid2(3,4) results in:
+ - - - - + - - - - + - - - - +
|         |         |         |
|         |         |         |
|         |         |         |
|         |         |         |
+ - - - - + - - - - + - - - - +
|         |         |         |
|         |         |         |
|         |         |         |
|         |         |         |
+ - - - - + - - - - + - - - - +
|         |         |         |
|         |         |         |
|         |         |         |
|         |         |         |
+ - - - - + - - - - + - - - - +
What to do about rounding? – you decide.
Another example: print_grid2(5,3):
+ - - - + - - - + - - - + - - - + - - - +
|       |       |       |       |       |
|       |       |       |       |       |
|       |       |       |       |       |
+ - - - + - - - + - - - + - - - + - - - +
|       |       |       |       |       |
|       |       |       |       |       |
|       |       |       |       |       |
+ - - - + - - - + - - - + - - - + - - - +
|       |       |       |       |       |
|       |       |       |       |       |
|       |       |       |       |       |
+ - - - + - - - + - - - + - - - + - - - +
|       |       |       |       |       |
|       |       |       |       |       |
|       |       |       |       |       |
+ - - - + - - - + - - - + - - - + - - - +
|       |       |       |       |       |
|       |       |       |       |       |
|       |       |       |       |       |
+ - - - + - - - + - - - + - - - + - - - +
'''
def print_grid2(x):
    for row in range(x):
        print()
        if x % (row + 1) == 0:
            print("+")
        print("|")
print_grid2(10)

a = []
for i in range(100):
    rand_num = random.randrange(11)
    if rand_num not in a:
        a.append(rand_num)
    if len(a) == 10:
        break
print(a)

# calculate pi with Python (polygon with lots of sides and then do perimeter/d)
# recursive function (function calls itself)
# search algorights
# NXT slice and dice was how I got into programming
# robotics
# where's the prime

def print_grid3(width, cells):
    for i in range(width):
            for j in range(cells):
                print("+", "- " * width, end="")
                print("", end="")
            print("+")

            for i in range(width):
                for j in range(cells):
                    print("|", end=" ")
                    print("  " * width, end="")
                print("|")
    for j in range(cells):
        print("+", "- " * width, end="")
        print("", end="")
    print("+")

print_grid3(5, 5)