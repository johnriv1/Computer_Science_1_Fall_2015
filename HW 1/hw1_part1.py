Width = raw_input('Width of box ==> ')
print Width

Height = raw_input('Height of box ==> ')
print Height

Character = raw_input('Enter frame character ==> ')
print Character

print '\nBox:'

print Character * int(Width) + '\n', Character, Width + 'x' + Height + ' ' * (int(Width)-(len(Width)+len(Height)+5)), Character+ ('\n' + Character + ' ' * (int(Width)-2) + Character)*(int(Height)-3)+ '\n' + Character * int(Width)