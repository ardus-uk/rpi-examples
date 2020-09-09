#!/usr/bin/python3
with open("nouns.txt") as givenfile:
     contents = givenfile.read()

# Write a program to find out how many words there are.  
# The output should be "There are <n> words in the file", with the correct number in place of <n>.

words = contents.split('\n')
print('There are ',len(words),' words in the file')

# Write a program to create a new text file which consists of all the words in the original file, 
# but in alphabetic order with no line breaks (ie the words all on the same line), 
# separated by single spaces.

outputfilename = "ex2.txt"
with open(outputfilename,'w') as outputfile:
     outputfile.write(' '.join(sorted(words)))
print("File '"+outputfilename+"' now contains the words in alphabetic order")

# Write a program to find the longest word in the file.
# (If there are two or more of the same length, choose the first in alphabetic order).

longest_word = ''
for word in sorted(words):
     if len(word) > len(longest_word):
          longest_word = word
print ("The longest word is ", longest_word)

# Write a program to create a new text file which consists of 
# those words in the original file which contain 6 or more letters.

outputfilename = "ex4.txt"
with open(outputfilename,'w') as outputfile:
     for word in words:
          if len(word) >= 6:
               outputfile.write(word + '\n')
print("File '"+outputfilename+"' now contains the words of length 6 or greater")

# Write a program to find out the mean (average) length of the words in the file.   
# The output should be of the form
# "The average number of letters in these words is <x>"  
# where <x> is given to 2 decimal places accuracy.

total_chars = sum(len(word) for word in words)
average_word_length = total_chars/len(words)
print(f'The average number of letters in these words is {average_word_length:.2f}')

#  Write a program to find all those words in the file which are palindromes

palindromes = []
for word in words:
     if word == word[::-1]: palindromes.append(word)
print("The list of palindromes, in alphabetical order, is ",sorted(palindromes))

# Write a program to create a new text file which consists 
# only of those words in the original file which contain 
# any letter no more than once.

outputfilename = "ex7.txt"
with open(outputfilename,'w') as outputfile:
     for word in words:
          if sorted(list(word))==sorted(list(set(word))):
               outputfile.write(word + '\n')
print("File '"+outputfilename+"' now contains the words with no repeating letters")

# Write a program to create a number of text files, 
# named file<n>.txt where <n> is a whole number, 
# and the contents of file<n>.txt are the words 
# from the given file which have exactly <n> letters.

for word in words:
     outputfilename = 'file'+str(len(word))
     with open(outputfilename,'a') as outputfile:
          outputfile.write(word + '\n')

# Write a program to find all words in the file 
# which are anagrams of other words in the file.

anagrams = {}
for word in words:
     anagram_key = ''.join(sorted(word))
     if anagram_key not in anagrams:
          anagrams[anagram_key] = []
     anagrams[anagram_key].append(word)

for anagram_key, anagrams_list in anagrams.items():
     if len(anagrams_list) > 1:
          print(anagrams_list)
