
i = 0
num = ''
while i <= 8:
    num += str(i) + ' '
    i += 1
print num

print

num2 = ''
for i in range(0,9):
    num2 += str(i) + ' '
print num2

print

num2 = []
for i in range(0,9):   
    if i%3 ==0 and i != 0:
            num2 += '\n'        
    for j in range(0,9):
        if j%3 == 0 and j != 0:
            num2 += ' '            
        num2 += str(i) + ',' + str(j) + ' '
    num2 += '\n'    
print num2

row = raw_input('Row number => ')
column = raw_input('Column number')

