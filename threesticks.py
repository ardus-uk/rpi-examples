#!/usr/bin/python3
print("Don't try to be clever...I'm only going to accept positive whole numbers...")
try:
    a=int(input('length of stick #1: '))
    b=int(input('length of stick #2: '))
    c=int(input('length of stick #3: '))
except ValueError:
    print("You're a very naughty boy. Stop it!")
    exit(0)

if a >= b:
    longest = a
    shortest = b
    middle = c
    if c >= a:
        longest = c
        middle = a
    elif c <= b:
        shortest = c
        middle = b
else:
    longest = b
    shortest = a
    middle = c
    if c >= b:
        longest = c
        middle = b
    elif c <= a:
        shortest = c
        middle = a
print(shortest,middle,longest)
if longest < (middle + shortest):
    print("You have a triangle")
    if (longest*longest == ((shortest*shortest) + (middle*middle))):
        print("...and it's right-angled!")
else:
    print("No triangle possible")
    
print("--------------------------------------")

ordered_list_of_sticks = sorted([a,b,c])
print(ordered_list_of_sticks)
print("I told you,", end = ' ')
if (ordered_list_of_sticks[2] < (ordered_list_of_sticks[1]+ordered_list_of_sticks[0])):
    print("you have a triangle")
else:
    print("no triangle possible")
    
