#!/usr/bin/python3

import cmath

def cno_entered(prompt_string):
    message = prompt_string
    while (message !=""):
        cno = input(message)
        parts = cno.split('+')

        if (False): message = "Please try again.\n" + prompt_string
        elif (False): message = "Only alphabetic characters, please.\n" + prompt_string
        else: message = ""
    x = float(parts[0].strip())
    y = float(parts[1].strip()[:-1])
    return complex(x,y)

z = cno_entered("Complex number in form a+bi: ")

# printing real and imaginary part of complex number 
print ("The real part of complex number is : ",end="") 
print (z.real) 
  
print ("The imaginary part of complex number is : ",end="") 
print (z.imag) 

# printing phase of a complex number using phase() 
# print ("The phase of complex number is : ",end="") 
# print (cmath.phase(z)) 

# converting complex number into polar using polar() 
w = cmath.polar(z) 
  
# printing modulus and argument of polar complex number 
print ("The modulus is : ",end="") 
print (w[0]) 
print ("The argument is : ",end="") 
print (w[1]) 
  
# converting complex number into rectangular using rect() 
#w = cmath.rect(1.4142135623730951, 0.7853981633974483) 
  
# printing rectangular form of complex number 
#print ("The rectangular form of complex number is : ",end="") 
#print (w) 