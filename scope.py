#!/usr/bin/env python3

# An example to illustrate global and local variables
# Peter Normington
# 2021-11-15

# the id() function returns the identity of the object; 
# this is an integer that is unique for the given object
# and remains constant during its lifetime. 

# EVERYTHING IS AN OBJECT
# even simple integers like 0, 1, 2 ...
print("Id of 0 is", id(0))
print("Id of 1 is", id(1))
print("Id of 3 is", id(3))
print("------------------------")
print()

counter = 0
# now, the variable "counter" refers to the object "0"

def fn_use_global():
    global counter
    print("In fn_use_global, counter =",counter) 
    print ("id of counter",id(counter)) 
    counter += 1
    print("In fn_use_global, counter =",counter) 
    print ("id of counter",id(counter))   

def fn_use_param(counter):
    print("In fn_use_param, counter =",counter) 
    print ("id of counter",id(counter)) 
    counter += 2
    print("In fn_use_param, counter =",counter)    
    print ("id of counter",id(counter))

def fn_displaycounter():
    print("In fn_displaycounter, counter =",counter)
    print ("id of counter",id(counter))


print("Outside any function, counter =",counter)
print ("id of counter",id(counter))
print()
fn_use_global()
print()
print("Outside any function, counter =",counter)
print ("id of counter",id(counter))
print()
fn_use_param(counter)
print()
print("Outside any function, counter =",counter)
print ("id of counter",id(counter))
print()
fn_displaycounter()