import re

# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

dictionary_list = [x for line in open('search_files/dictionary.txt') for x in split_line(line)]

file = open('search_files/AliceInWonderLand200.txt')
alice_array = []
line_list = []
l = 1
for line in file:
    for word in split_line(line):
        alice_array.append(word.upper())
        line_list.append(l)
    l += 1

print(len(line_list), len(alice_array))

print('--- Linear Search ---')

def linear_search(key, arr):
    i = 0
    while i < len(arr) and arr[i] != key:
        i += 1

    if i < len(arr):
        pass
    else:
        print('Line', line_list[alice_array.index(key)], 'possible misspelled word:', key)

for word in alice_array:
    linear_search(word, dictionary_list)

print('--- Binary Search ---')
def binary_search(key, arr):
    lower_bound = 0
    upper_bound = len(arr) - 1

    found = False
    middle_pos = 0

    while not found and lower_bound <= upper_bound:
        middle_pos = (upper_bound + lower_bound) // 2
        if arr[middle_pos] < key:
            lower_bound = middle_pos + 1
        elif arr[middle_pos] > key:
            upper_bound = middle_pos - 1
        else:
            found = True

    if found:
        pass

    else:
        print('Line', line_list[alice_array.index(key)], 'possible misspelled word:', key)

for word in alice_array:
    binary_search(word, dictionary_list)