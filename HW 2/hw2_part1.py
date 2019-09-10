"""
Author: John Rivera

Purpose: This program calculates the volume of a rectangular prism shaped lock using user input for the length, width, and height. Then this program calculates the height/depth that a cylinder shaped lake will lose using the volume from the first function and using user input for the radius.

"""

import math

def volume_prism(length, width, height):
    volume_prism = ((float(length) * float(width) * float(height)))*70*3*30
    return volume_prism

def find_length(radius, volume):
    height = volume/(math.pi*radius**2)
    return height

length = raw_input('Length of rectangular prism (m) ==> ')
print length
length = float(length)
width = raw_input('Width of rectangular prism (m) ==> ')
print width
width = float(width)
height = raw_input('Height of rectangular prism (m) ==> ')
print height
height = float(height)

print "Water needed for (%.1fm,%.1fm,%.1fm) locks is %.1fm^3." %(length, width, height,volume_prism(length, width, height))

radius = raw_input('Radius of cylinder (m) ==> ')
print radius
radius = float(radius)

print "Lake with radius %.1fm will lose %.1fm depth in three months." %(radius, find_length(radius, volume_prism(length, width, height)))

