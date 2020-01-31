#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 12:56:48 2020

@author: tfield
"""

import turtle
import math

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
       
# Draws a single petal in turtle (t) using radius (r) and angle (angle) for the arcs
def petal(t, r, angle):
    arc(t, r, angle)
    t.lt(180-angle)
    arc(t, r, angle)
    t.lt(180-angle)
        
# Draws a flower by drawing multiple petals around the starting point
def flower(t, r, n, angle):
    for i in range(n):
        petal(t, r, angle)
        t.lt(360//n)
        
# Moves the pen horizontally, without drawing
def shift(t, d):
    t.pu();
    t.fd(d);
    t.pd();

t42 = turtle.Turtle()

shift(t42, -150)
 #Draw 3 flowers
flower(t42, 50, 7, 60) #Left flower
shift(t42, 150)
flower(t42, 50, 10, 90) #Center flower
shift(t42, 150)
flower(t42, 100, 20, 30) #Right flower


turtle.update()
turtle.mainloop()