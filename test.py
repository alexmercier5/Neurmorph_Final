###This is a test file for my final project - used for python testing mostly.


Morse = {
    # codes from https://www.itu.int/rec/R-REC-M.1677-1-200910-I/en
    "A": "10111",
    "B": "111010101",
    "C": "11101011101",
    "D": "1110101",
    "E": "1",
    "F": "101011101",
    "G": "111011101",
    "H": "1010101",
    "I": "101",
    "J": "1011101110111",
    "K": "111010111",
    "L": "101110101",
    "M": "1110111",
    "N": "11101",
    "O": "11101110111",
    "P": "10111011101",
    "Q": "1110111010111",
    "R": "1011101",
    "S": "10101",
    "T": "111",
    "U": "1010111",
    "V": "101010111",
    "W": "101110111",
    "X": "11101010111",
    "Y": "1110101110111",
    "Z": "11101110101",
    " ": "0",  # space
    "1": "10111011101110111",
    "2": "101011101110111",
    "3": "1010101110111",
    "4": "10101010111",
    "5": "101010101",
    "6": "11101010101",
    "7": "1110111010101",
    "8": "111011101110101",
    "9": "11101110111011101",
    "0": "1110111011101110111",
    ".": "10111010111010111",  # period
    ",": "1110111010101110111",  # comma
    ":": "11101110111010101",  # colon
    "?": "101011101110101",  # question
    "'": "1011101110111011101",  # apostrophe
    "-": "111010101010111",  # dash or minus
    "/": "1110101011101",  # slash
    "(": "111010111011101",  # left parenthesis
    ")": "1110101110111010111",  # right parenthesis
    '"': "101110101011101",  # quote
    "=": "1110101010111",  # equals
    "+": "1011101011101",  # plus
    "@": "10111011101011101",  # at sign (@)
    # these punctuation marks are not included in the ITU recommendation,
    # but are found in https://en.wikipedia.org/wiki/Morse_code
    "!": "1110101110101110111",  # exclamation point
    "&": "10111010101",  # ampersand (also prosign for 'WAIT')
    ";": "11101011101011101",  # semicolon
    "_": "10101110111010111",  # underscore
    "$": "10101011101010111",  # dollar sign
}


print(len(Morse))
# #take user input
# msg = input("Type phrase to translate here: ")
# #convert to all uppercase
# msg = msg.upper()
# #transform from string to an array with each character a separate element
# msg = list(msg)
# print('\n', msg)
# my_morse = []
# #evaluate each character in the list and convert to morse
# for i in msg:
#     my_morse.append(Morse.get(i))

# print('\n', my_morse, '\n')


# temp_inputs = ['1','0','1','1','1']
# send_inp = [] #1 for dot; 2 for dash
# count = 0
# for i in range(len(temp_inputs)):
#     if temp_inputs[i] == '1':
#         print("test")
#         count += 1
#         if count == 3:
#             send_inp.append(2)
#             count = 0
#     if temp_inputs[i] == '0' and count == 1:
#         send_inp.append(1)
#         count = 0
# print(send_inp)
