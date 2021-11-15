#!/usr/bin/env python3

counter = 0

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