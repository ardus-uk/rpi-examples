#!/usr/bin/python3

import random

filename = "./nouns.txt"
with open(filename,'r') as reader:
    whole_text = reader.read()

words_list = whole_text.split()
index  = random.randint(0, len(words_list)-1)
print(words_list[index])



