'''
Complete the following 3 searching problems using techniques
from class and from Ch15 of the textbook website
'''
import re

# This function takes in a line of text and returns a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

#1.  (7pts) Write code which finds and prints the longest
# word in the provided dictionary.  If there are more
# than one longest word, print them all.  (read the file line by line to accomplish this task)

dictionary = open('search_files/dictionary.txt')
all_positions = []
all_words = []
position = 0
for word in dictionary:
    print(len(word))
    all_positions.append(len(word))
    all_words.append(word)
    position += 1

print(max(all_positions))

dictionary.close()
dictionary = open('search_files/dictionary.txt')
for word in dictionary:
    if len(word) == 29:
        print("Longest word:", word)

#2.  (7pts)  Write code which finds
#  The total word count AND average word length of "AliceInWonderLand.txt"

word_count = 0
letter_count = 0
alice = open('search_files/AliceInWonderLand.txt')
for line in alice:
    for word in split_line(line):
        word_count += 1
        letter_count += len(word)
print("Word count:", word_count)
print("Average word:", letter_count/word_count, "letters")

# CHOOSE ONE OF THE FOLLOWING TWO PROBLEMS

#3 (13pts)  How many times does "Cheshire" occur in"AliceInWonderLand.txt"?
# How many times does "Cat" occur?
# How many times does "Cheshire" immediately followed by "Cat" occur?
times_cat_occurs = 0
for line in alice:
    for word in split_line(line):
        if word == "Cat".upper():
            times_cat_occurs += 1
print(times_cat_occurs)

alice.close()

alice = open('search_files/AliceInWonderLand.txt')

words = []
for line in alice:
    for word in split_line(line):
        words.append(word)

# [y for y in [split_line(line)] for line in alice]

cheshire_cat = 0

for i in range(len(words)):
    print(words[i - 1], words[i])
    if words[i - 1].upper() == "CHESHIRE" and words[i].upper() == "CAT":
        cheshire_cat += 1

print('\"Cheshire Cat\" appears', cheshire_cat, 'times')

#### OR #####

#3  (13pts)Find the most frequently occurring 
#  seven letter word in "AliceInWonderLand.txt"




# CHALLNENGE PROBLEM  (for fun, not for credit).  
#  What words appear in the text of "Alice in Wonderland" that DO NOT occur in "Alice Through the Looking Glass".  Make a list.  You can substitute this for any of the above problems.
def binary_search(key, arr):

    lower_bound = 0
    upper_bound = len(arr) - 1

    found = False
    middle_pos = 0

    while not found and lower_bound <= upper_bound:
        middle_pos = (upper_bound - lower_bound) // 2
        if arr[middle_pos] < key:
            lower_bound = middle_pos + 1
        elif arr[middle_pos] > key:
            upper_bound = middle_pos - 1
        else:
            found = True

    if found:
        print("Found", key, "at position", middle_pos)
    else:
        print(key, "not found")

looking_glass = open('search_files/AliceThroughTheLookingGlass.txt')
looking_words = []


for line in looking_glass:
    for word in split_line(line):
        looking_words.append(word.upper())

for word in words:
    binary_search(word, looking_words)

# binary search each unique word in the array if in alice through the looking glass