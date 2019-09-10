"""
This program experiments with the use of functions
and also learning error checking.


"""
import math

## import math so it can be used in function

## Function returns the length of a line 
## starting at (x1,y1) and ending at (x2,y2)
def line_length(x1,y1,x2,y2):
    x1 = int(x1)
    y1 = int(y1)                      
    x2 = int(x2)
    y2 = int(y2)
    length = (x1-x2)**2 + (y1-y2)**2
    length = math.sqrt(length)
    return length

## converted variables into integers so they could be used mathematically

initial_x = 10
initial_y = 10
next_x = raw_input("The next x value ==> ")
next_y = raw_input("The next y value ==> ")

print "The line has moved from (%d,%d)" %(initial_x, initial_y),\
    "to", "(" + next_x + "," + next_y +")"

## removed a comma after first string so %d can be substituted
## removed str() from str(next_x) because next_x is already a string
## added the two "("

print "Total length traveled is: %.2f" %line_length(initial_x, initial_y, next_x, next_y)

## included line_length(initial_x, initial_y, next_x, next_y) in string and rounded it through %.2f

