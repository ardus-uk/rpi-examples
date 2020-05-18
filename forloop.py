#!/usr/bin/python3

charlist = ['*','!','@','#','£']

for char in charlist:
    print(char)

for char in charlist:
    print(char,end = "\t")
print()

numberlist = list(range(1,4))

for number in numberlist:
    print(number)


for number in numberlist:
    print(number,end = "\t")
print()

for number in numberlist:
    print('@' * number)


for number in numberlist:
    for char in charlist:
        print(char * number)

for char in charlist:
    for number in numberlist:
        print(char * number)
