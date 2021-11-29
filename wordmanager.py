#!/usr/bin/env python3
import json
import string
import enchant
import sys

given_word = str(sys.argv[1])
d = enchant.Dict("en_GB")

def check_count(gw,k):
    c = True
    for char in set(gw):
        c = c and gw.count(char) >= k.count(char)
    return c

jw = "/home/peter/Coding/rpi-examples/words_dictionary.json"

with open(jw) as words_file:
    eng_words = json.load(words_file)

alphabet_list = list(string.ascii_lowercase)

residue_set = set(alphabet_list)-set(list(given_word))
c1 = {k: v for k, v in eng_words.items() if len(k)>=3 and len(k)<=len(given_word)}
c2 = {k: v for k, v in c1.items() if len(set(list(k)).intersection(residue_set))==0}
c3 = {k: v for k, v in c2.items() if given_word[0] in list(k)}
c4 = {k: v for k, v in c3.items() if check_count(given_word,k)}
l_c4 = sorted(sorted(list(c4.keys())),key=len)
for a in l_c4:
    if d.check(a):
        print(a)
