#!/usr/bin/python3

#import random

in_filename = "./nouns.txt"
with open(in_filename,'r') as reader:
    whole_text = reader.read()

words_list = whole_text.split()
# index  = random.randint(0, len(words_list)-1)
# print(words_list[index])

long_words = []
for word in words_list:
    if len(word) > 6:
        long_words.append(word)

print(long_words)
long_words_in_string = "\n".join(long_words)
print(long_words_in_string)

out_filename = "./longwords.txt"
with open(out_filename, 'w') as writer:
    writer.write(long_words_in_string)