"""
Author: John Rivera

Purpose: Moves a "turtle" in coordinate space using user inputs.
"""



def move(x,y,direction,amount):
    if direction == 'right':
        if amount == 'move':
            x += 20
        elif amount == 'jump':
            x += 50
        else:
            x += 0
    elif direction == 'up':
        if amount == 'move':
            y -= 20
        elif amount == 'jump':
            y -= 50
        else:
            y -= 0
    elif direction == 'left':
        if amount == 'move':
            x -= 20
        elif amount == 'jump':
            x -= 50
        else:
            x -= 0
    elif direction == 'down':
        if amount == 'move':
            y += 20
        elif amount == 'jump':
            y += 50
        else:
            y += 0
    else:
        y+=0
        x+=0
        
    return x,y
    
    
def turn(direction):
    if direction == 'right':
        direction = 'up'
    elif direction == 'up':
        direction = 'left'
    elif direction == 'left':
        direction = 'down'
    elif direction == 'down':
        direction = 'right'
    return direction
    
Direction = 'right'
Amount = 'None'
x = 200
y = 200
(x,y) = move(x,y,Direction,Amount)
i=0

commandlist = []
while i < 5:
    print 'Turtle: (%s,%s) facing: %s' %(x,y,Direction)
    command = raw_input('Command (move,jump,turn) => ')
    print command
    commandlist.append(command)
    command = command.lower()
    if command == "turn":
        Direction = turn(Direction)
    elif command == 'move':
        (x,y) = move(x,y,Direction,command)
    elif command == 'jump':
        (x,y) = move(x,y,Direction,command)
    i+=1

print 'Turtle: (%s,%s) facing: %s' %(x,y,Direction)
print
print 'All commands entered', commandlist

commandlist.sort()

print 'Sorted commands', commandlist