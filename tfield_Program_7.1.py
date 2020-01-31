#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 14:14:04 2020

@author: tfield
"""
import math

# Calculate the square root of a using Newton's Method
def mysqrt(a):
    x = a/2;
    epsilon  = 0.000000001
    y = (x + a/x) / 2
    
    while abs(y-x) >= epsilon:
        x = y
        y = (x + a/x) / 2
    return x

# Compare the result of Newton's Method with the built in square root function for a given value
def test_square_root(a):
    sqrtOUT = mysqrt(a)
    diff = abs(sqrtOUT - math.sqrt(a)) # difference between methods
    print("{0:.1f} {1:13.11f} {2:13.11f} {3:.11e}".format(a, sqrtOUT, math.sqrt(a), diff))
          #"{0:.11e}".format(diff))

# Prints column headers
def printHeader():
    print("a   mysqrt(a)     math.sqrt(a)   diff")
    print("-   ---------     ------------   ----")


# Test values 1 to 9
printHeader();
for i in range(9):
    test_square_root(i+1)
    
    
    