"""
Author: John Rivera

Purpose: Make a diamond using user inputted background character, foreground character, and height
"""

background = raw_input('Background char => ')
print background
character = raw_input('Foreground char => ')
print character
height = raw_input('Height => ')
print height
print

if str.isdigit(height) == False or len(background) != 1 or len(character) != 1:
    if str.isdigit(height) == False:
        print "Please enter a number for height"
    if len(background) != 1: 
        print "Please enter one character for background"
    if len(character) != 1:
        print "Please enter one character for foreground"
else:
    i = 0
    while i<(int(height)/2):
        
        
        if i==2:
            print str((int(i)+1)).rjust(len(height)) + background*(int(height)-i) + character + background*(2*(i)) + 'o' + background*(int(height)-i)
        else:
            print str((int(i)+1)).rjust(len(height)) + background*(int(height)-i) + character + background*(2*(i)) + character + background*(int(height)-i)
        
        i += 1
    
    t = i
    
    if int(height)%2 == 0:
        while i<=(int(height)/2) and i > 0:
            i -= 1
            print str((int(t)+1)).rjust(len(height)) + background*(int(height)-i) + character + background*(2*(i)) + character + background*(int(height)-i)
            t += 1
    
    elif int(height)%2 == 1:
        while i<=(int(height)/2) and i >= 0:
            print str((int(t)+1)).rjust(len(height)) + background*(int(height)-i) + character + background*(2*(i)) + character + background*(int(height)-i)
            i -= 1
            t += 1    