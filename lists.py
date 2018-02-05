import random

#LISTS (31PTS TOTAL)
#In these exercises you should should use functions as needed.  All functions should have comments to describe their purpose.

# PROBLEM 1 (Using List Comprehensions - 6pts)
# Use the list comprehension method to do the following:
# a) Make a list of numbers from 1 to 100
# b) Make a list of even numbers from 20 to 40
# c) Make a list of squares from 1 to 100 (1 ** 2 to 100 ** 2)

list_a = [i for i in range(1, 101)]
print(list_a)
intermed_list = [i for i in range(20, 41)]
list_b = [i for i  in intermed_list if i%2 == 0]

#PROBLEM 2 (8-ball - 5pts)
# A magic 8-ball, when asked a question, provides a random answer from a list.
# The code below contains a list of possible answers. Create a magic 8-ball program that
# prints a random answer.
answer_list = [ "It is certain", "It is decidedly so", "Without a \
doubt", "Yes, definitely", "You may rely on it", "As I see it, \
yes", "Most likely", "Outlook good", "Yes", "Signs point to yes",
"Reply hazy try again", "Ask again later", "Better not tell you \
now", "Cannot predict now", "Concentrate and ask again", "Don ' t \
count on it", "My reply is no", "My sources say no", "Outlook \
not so good", "Very doubtful" ]
def shake_eight_ball():
    print(answer_list[random.randrange(len(answer_list))])

# PROBLEM 3 (Shuffle - 5pts)
# A playing card consists of a suit (Heart, Diamond, Club, Spade) and a value (2,3,4,5,6,7,8,9,10,J,Q,K,A).
# Create a list of all possible playing cards, which is a deck.
# Then create a function that shuffles the deck, producing a random order.

suits = ["heart", "diamond", "club", "spade"]
values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
deck = []
for suit in suits:
    for value in values:
        deck.append("{} of {}s".format(value, suit))

# PROBLEM 4 (Tic-Tac-Toe - 15pts)
# Write a Tic-Tac-Toe program that allows two people to play the game against each other.
# In turn, ask each player which row and column they want to play.
# Make sure that the program checks if that row/column combination is empty.
# When a player has won, end the game.
# When the whole board is full and there is no winner, announce a draw.
# This is a fairly long program to write (60 lines or so).
# It will definitely help to use some functions.
# I recommend that you create a function display_board() that gets the board
# as parameter and displays it,
# a function get_row_column() that asks for a row or a column (depending on a parameter)
# and checks whether the user entered a legal value,
# and a function winner() that gets the board as argument and checks if there is a winner.
# Keep track of who the current player is using a global variable player that you can
# pass to a function as an argument if the function needs it.
# I also use a function opponent(), that takes the player as argument and returns
# the opponent. I use that to switch players after each move.

def all_same(items):
    return all(i == items[0] for i in items)

done = False
is_p1_turn = True
row1 = ["_" for i in range(3)]
row2 = ["_" for i in range(3)]
row3 = ["_" for i in range(3)]
board = [row1, row2, row3]
print(row1, row2, row3, sep="\n")

def out_of_range(n):
    return n > 3

def check_winner():
    global done

    # logic to see if there's a horizontal winner
    if all_same(row1) and row1[0] == "X":
        print("Player one wins!")
        done = True
    elif all_same(row1) and row1[0] == "O":
        print("Player two wins!")
        done = True

    if all_same(row2) and row2[0] == "X":
        print("Player one wins!")
        done = True
    elif all_same(row2) and row2[0] == "O":
        print("Player two wins!")
        done = True

    if all_same(row3) and row3[0] == "X":
        print("Player one wins!")
        done = True
    elif all_same(row3) and row3[0] == "O":
        print("Player two wins!")
        done = True

    # logic to see if there's a vertical winner

    if row1[0] == "X" and row2[0] == "X" and row3[0] == "X":
        print("Player one wins!")
        done = True
    elif row1[1] == "X" and row2[1] == "X" and row3[1] == "X":
        print("Player one wins!")
        done = True
    elif row1[2] == "X" and row2[2] == "X" and row3[2] == "X":
        print("Player one wins!")
        done = True

    if row1[0] == "O" and row2[0] == "O" and row3[0] == "O":
        print("Player two wins!")
        done = True
    elif row1[1] == "O" and row2[1] == "O" and row3[1] == "O":
        print("Player two wins!")
        done = True
    elif row1[2] == "O" and row2[2] == "O" and row3[2] == "O":
        print("Player two wins!")
        done = True

    # logic to see if there's a diagonal winner

    if row1[0] == "X" and row2[1] == "X" and row3[2] == "X":
        print("Player one wins!")
        done = True
    elif row1[2] == "X" and row2[1] == "X" and row3[0] == "X":
        print("Player one wins!")
        done = True

    if row1[0] == "O" and row2[1] == "O" and row3[2] == "O":
        print("Player two wins!")
        done = True
    elif row1[2] == "O" and row2[1] == "O" and row3[0] == "O":
        print("Player two wins!")
        done = True

def check_draw():
    global done
    if "_" not in row1 and "_" not in row2 and "_" not in row3:
        print("Tie!")
        done = True

while not done:
    if is_p1_turn:
        print("Player one, choose a spot to mark. (1, 1) is the top left.")
        x_component = int(input("Row (enter an integer): "))
        y_component = int(input("Column (enter an integer): "))
        # print(x_component, y_component)
        # make changes based on x and y components given

        # get_row_column
        if x_component <= 3 and x_component >=1 and y_component <= 3 and y_component >= 1:
            if board[x_component - 1][y_component - 1] == "_":
                board[x_component - 1][y_component - 1] = "X"
            else:
                print("That is taken. Try again.")
                is_p1_turn = not is_p1_turn
        else:
            print("Choose feasible numbers. Try again.")
            is_p1_turn = not is_p1_turn

    else:
        print("Player one, choose a spot to mark. (1, 1) is the top left.")
        x_component = int(input("Row (enter an integer): "))
        y_component = int(input("Column (enter an integer): "))
        # print(x_component, y_component)
        # make changes based on x and y components given

        if x_component <= 3 and x_component >= 1 and y_component <= 3 and y_component >= 1:
            if board[x_component - 1][y_component - 1] == "_":
                board[x_component - 1][y_component - 1] = "O"
            else:
                print("That is taken. Try again.")
                is_p1_turn = not is_p1_turn
        else:
            print("Choose feasible numbers. Try again")
            is_p1_turn = not is_p1_turn

    print(row1, row2, row3, sep="\n")
    is_p1_turn = not is_p1_turn

    #check if there's a winner
    check_winner()

    # check draw
    check_draw()

# The main program will be something along the lines of (in pseudo-code):
# display board
# while True:
#   ask for row
#   ask for column
#       if row/column already occupied:
#           display error
#   place player marker in row/col
#   display board
#   check for winner:
#       announce winner
#       break
#   check board full:
#       announce draw
#       break
#   switch player

# CHALLENGE PROBLEM 5 (MAY DO AS SUBSTITUTE FOR PROBLEM 4, NO ADDITIONAL CREDIT)
# Create a program that is a simplified version of the game “Battleship.”
# The computer creates (in memory) a grid that is 4 cells wide and 3 cells high.
# The rows of the grid are numbered 1 to 3, and the columns of the grid are labeled A to D.
# The computer hides a battleship in three random cells in the grid.
# Each battleship occupies exactly one cell.
# Battleships are not allowed to touch each other horizontally or vertically.
# Make sure that the program places the battleships randomly, so not pre-configured.
# The computer asks the player to “shoot” at cells of the grid.
# The player does so by entering the column letter and row number of the cell
# which she wants to shoot at (e.g., "D3").
# If the cell which the player shoots at contains nothing, the computer responds with “Miss!”
#  If the cell contains a battleship, the computer responds with “You sunk my battleship!”
# and removes the battleship from the cell (i.e., a second shot at the same cell is a miss).
# As soon as the player hits the last battleship, the computer responds with displaying
# how many shots the player needed to shoot down all three battleships, and the program ends.
# To help with debugging the game, at the start the computer should display the grid with
# O's marking empty cells and X's marking cells with battleships.
# Hint: If you have troubles with this exercise, start by using a board which has the
# battleships already placed.
# Once the rest of the code works, add a function that places the battleships at random,
# at first without checking if they are touching one another.
# Once that works, add code that disallows battleships touching each other.
