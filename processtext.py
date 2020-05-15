#!/usr/bin/python3

filename = "/home/peter/Downloads/alice29.txt"

with open(filename,'r') as reader:
    # Further file processing goes here
    a = reader.read()
    
print(len(a))
words = a.split()
print(len(words))
count = 0
for word in words:
    if word == "Alice": count += 1

print(count)

# Return the characters space, tab, linefeed, return, formfeed, and vertical tab.
import string
import unicodedata
ws = string.whitespace
for char in ws:
    print(char.encode("utf-8"))

