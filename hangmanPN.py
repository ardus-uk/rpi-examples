#!/usr/bin/python3

import random

def players_char(prompt_string):
    message = prompt_string
    while (message !=""):
        character = input(message)
        if (len(character)!=1):
            message = "One letter only, please.\n" + prompt_string
        elif ((ord(character) not in range(65,91)) and (ord(character) not in range(97,123))):
            message = "Only alphabetic characters, please.\n" + prompt_string
        else:
            message = ""
    return character.upper()
    
def word_from_wordlist(filename):
    with open(filename,'r') as reader:
        whole_text = reader.read()
    words_list = whole_text.split()
    random_index  = random.randint(0, len(words_list)-1)
    return words_list[random_index].upper()
    
# Specify the various responses
msg = ["Had it already","Sorry, not in","Well done","You won!","You lost!"]
# Number of wrong guesses allowed
MAX_WRONG_GUESSES = 12
    
# THE GAME STARTS HERE
# Get a word
target_word = word_from_wordlist("longwords.txt")
# Prepare the list to keep track of the guessed letters in the word so far ("wsf")
row_of_dashes = '_' *  len(target_word)
wsf = list(row_of_dashes)
# List of letters not in the target word
fails = [] # type: list

msg_number = 0
while (msg_number < 3):
    print(" ".join(wsf))
    ch = players_char("Your choice of letter?: ")
    if ((ch in fails) or (ch in wsf)):
        msg_number = 0
    elif ch not in target_word:
        fails.append(ch)
        msg_number = 1 if (len(fails) < MAX_WRONG_GUESSES) else 4
    else:
        for index in range (0,len(target_word)):
            if target_word[index]==ch:
                wsf[index]=ch
        msg_number = 2 if ("".join(wsf)!=target_word) else 3
    print(msg[msg_number])
print("The word was", target_word)
print("END OF GAME")