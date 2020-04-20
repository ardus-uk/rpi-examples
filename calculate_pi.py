#!/usr/bin/python3

# Approximate pi, using an obscure formula from Mark

# However, convergence is very rapid, and as the Python library reference notes,
# "Floating point numbers are implemented using double in C. 
# All bets on their precision are off unless you happen to know the machine you are working with."

import math

desired_precision = 1e-50
pi_estimate = 1

const = (2*math.sqrt(2)/9801)
sum_of_terms = 0
k = 0
last_pi_estimate = 0

while (abs(pi_estimate-last_pi_estimate) > desired_precision):
    term = math.factorial(4*k)*(1103+26390*k)/((math.factorial(k)**4)*(396**(4*k)))
    print("Next term in infinite series sum: " + str(term))
    sum_of_terms = sum_of_terms + term
    last_pi_estimate = pi_estimate
    pi_estimate = 1/(const*sum_of_terms)
    print ("\t\tNew estimate for pi: " + str(pi_estimate))
    k = k+1


