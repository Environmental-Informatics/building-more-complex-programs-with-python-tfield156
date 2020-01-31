#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 13:55:56 2020

@author: tfield
"""

# Takes two inputs from the user and converts them to integers
def getNumbers():
    a = int(input('First number: '))
    b = int(input('Second number: '))
    numbers = [a, b]
    return numbers

# computes the greatest common divisor of two numbers
def gcd(a, b):
    if b == 0: # gcd(a, 0) = a is given in the problem statement
        return a
    else: #gcd(a, b) = gcd(b, a % b)
        r = a % b;
        num = gcd(b, r)
        return num

# Collect two numbers from the user, and then determine the greatest common divisor between them    
userNumbers = getNumbers()
greatestDivisor = gcd(userNumbers[0], userNumbers[1])
print(' GCD is', greatestDivisor)