#!/usr/bin/python3

def spaced_string(char_list):
    return " ".join(char_list)

def players_char(prompt_string):
    message = prompt_string
    while (message !=""):
        character = input(message)
        if (len(character)!=1):
            message = "One letter only, please.\n" + prompt_string
        elif ((ord(character) not in range(65,90)) and (ord(character) not in range(97,122))):
            message = "Ony alphabetic characters, please.\n" + prompt_string
        else:
            message = ""
    return character.upper()

target_word = "calumny".upper()
print(target_word)
wsf = '_'* len(target_word)
list_wsf = list(wsf)
print(list_wsf)
letters_not_in = []
print(letters_not_in)
msg = ["","Had it already","Sorry, not in","Well done","You won","You lost"]

msg_number = 0;
while (msg_number < 4):
    print(spaced_string(list_wsf))
    ch = players_char("Your choice of letter?: ")
    if ch in letters_not_in:
        msg_number = 1
    elif ch not in target_word:
        letters_not_in.append(ch)
        if (len(letters_not_in) < 12):
            msg_number = 2
        else:
            msg_number = 5
    else:
        for index in range (0,len(target_word)):
            if target_word[index]==ch:
                list_wsf[index]=ch
        msg_number = 3
        if ("".join(list_wsf)==target_word):
            msg_number = 4
          
    print(msg[msg_number])
print("END OF GAME")
                
    
