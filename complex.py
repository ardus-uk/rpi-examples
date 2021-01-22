#!/usr/bin/python3

import cmath

x = 5
y = 3

z = complex(x,y)

# printing real and imaginary part of complex number 
print ("The real part of complex number is : ",end="") 
print (z.real) 
  
print ("The imaginary part of complex number is : ",end="") 
print (z.imag) 

# printing phase of a complex number using phase() 
print ("The phase of complex number is : ",end="") 
print (cmath.phase(z)) 

# converting complex number into polar using polar() 
w = cmath.polar(z) 
  
# printing modulus and argument of polar complex number 
print ("The modulus and argument of polar complex number is : ",end="") 
print (w) 
  
# converting complex number into rectangular using rect() 
w = cmath.rect(1.4142135623730951, 0.7853981633974483) 
  
# printing rectangular form of complex number 
print ("The rectangular form of complex number is : ",end="") 
print (w) 