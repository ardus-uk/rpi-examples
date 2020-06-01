#!/usr/bin/python3

in_filename = "./nouns.txt"
with open(in_filename,'r') as reader:
    whole_text = reader.read()

words_list = whole_text.split()

long_words = []
for word in words_list:
    if len(word) > 6:
        long_words.append(word)

long_words_in_string = "\n".join(long_words)

out_filename = "./longwords.txt"
with open(out_filename, 'w') as writer:
    writer.write(long_words_in_string)