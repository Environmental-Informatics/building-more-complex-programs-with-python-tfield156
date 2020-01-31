#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 13:37:21 2020

@author: tfield
"""


# Takes input from the user for four values and converts them to integers
def getNumbers():
    a = int(input('a = '))
    b = int(input('b = '))
    c = int(input('c = '))
    n = int(input('n = '))
    numbers = [a, b, c, n]
    return numbers

# Checks if Fermat's Last Theorem (a^n + b^n = c^n) holds for the the given inputs
def check_fermat(a, b, c, n):
    if ((a <= 0) or (b <= 0) or (c <= 0)):
        print('First three inputs must be positive')
        return
    elif (n <= 2):
        print('Fourth input must be greater than 2')
        return
    leftSide = (a ** n) + (b ** n)
    rightSide = c ** n
    if leftSide == rightSide:
        print('Holy smokes, Fermat was wrong!')
    else:
        print('No, that doesn\'t work.')

# Get the numbers from the user and check if Fermat's Last Theorem holds
userNumbers = getNumbers();
check_fermat(userNumbers[0], userNumbers[1], userNumbers[2], userNumbers[3])

