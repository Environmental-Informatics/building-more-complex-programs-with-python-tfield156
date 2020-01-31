#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 12:56:48 2020

@author: tfield
"""

import turtle
import math

t42 = turtle.Turtle()

#for flowerNum in range(3): #Draw 3 flowers
    
    
arc(t42, 50, 360)   
    
    
    



turtle.mainloop()

# Draws an arc in turtle (t) with radius (r) and at the specified angle
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)
    
# Draws n connected line segments of length (length) and incrementally changing the angle by (angle)
def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)
        
# Draw
def petal(t, r, angle)
    arc(t, r, angle)
    t.lt(180)
    arc(t, r, angle)
        
def flower(t, n, rad):
    for i in range(n):
        petal(t, r, angle)
        t.lt(180())
    
    
    
    
    
    

