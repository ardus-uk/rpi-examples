#!/usr/bin/python3

acceptable_fruits = []
filehandle = open("./fruits.txt","r")
for fruit in filehandle:
    acceptable_fruits.append(fruit.strip().lower())

print(acceptable_fruits)
