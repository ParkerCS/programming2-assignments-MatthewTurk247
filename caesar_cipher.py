# print with different secret number/shift each time

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

sentence = 'Qexxlia Xyvo ampp riziv kix xlmw sri. Lelele.'.upper()

for character in sentence:
    if character == ' ' or character == ".":
        pass
    else:
        for i in range(27):
            print(alphabet[alphabet.index(character) + i], end='')
        print()