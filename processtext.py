#!/usr/bin/python3

def print_heading(heading):
    """Underlines a string"""
    print(heading)
    print("-" * len(heading))

filename = "./alice29.txt"

with open(filename,'r') as reader:
    whole_text = reader.read()
    
print_heading("Analysing Alice")
    
print('Number of characters = %s' % (len(whole_text)))
words = whole_text.split()
print('Number of \'words\' = %s' % (len(words)))
interesting_words = [
    'Alice',
    'cat',
]
interesting_words_count = 0
for word in words:
    if word in interesting_words: interesting_words_count += 1

print(f'Number of occurrences of the words in the list {interesting_words} = {interesting_words_count}')
print("\n" * 2)

# Return the characters space, tab, linefeed, return, formfeed, and vertical tab.
import string
ws = string.whitespace
print_heading("Whitespace in Python")
print("UTF-8\tDecimal\tHex")
for char in ws:
    decimal =  ord(char)
    print(char.encode("utf-8"), end = "\t")
    print(str(decimal), end = "\t")    
    print(hex(decimal))
