#!/usr/bin/python3

def printheading(heading):
    print(heading)
    print("-" * len(heading))

filename = "./alice29.txt"

with open(filename,'r') as reader:
    wholetext = reader.read()
    
printheading("Analysing Alice")
    
print("Number of characters =",len(wholetext))
words = wholetext.split()
print("Number of 'words' =",len(words))
interestingword = "Alice"
count = 0
for word in words:
    if word == interestingword: count += 1

print("Number of occurrences of the word '"+interestingword+"' =",count)
print("\n" * 2)

# Return the characters space, tab, linefeed, return, formfeed, and vertical tab.
import string
ws = string.whitespace
printheading("Whitespace in Python")
for char in ws:
    decimal =  ord(char)
    print(char.encode("utf-8"), end = "\t")
    print(str(decimal), end = "\t")    
    print(hex(decimal))
