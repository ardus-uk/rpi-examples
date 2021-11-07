#!/usr/bin/env python3
import json
import os
from itertools import combinations

script_directory = os.path.dirname(os.path.abspath(__file__))

test = False
jw = os.path.join(script_directory, "words_dictionary.json")

with open(jw) as words_file:
    english_words = json.load(words_file)

print('frzate' in english_words)
print(len(english_words))

anag = sorted('liquorice')
print(anag)
for word in english_words:
    if sorted(word)==anag:
        print(word)

set = "abcde"
for l in range(0, len(set) + 1):
    for subset in itertools.combinations(letters, l): #all combinations in subset
        list_comb.append(subset)
