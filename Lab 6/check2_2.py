

def ok_to_add(row, column, addnum):
    for j in bd[row]:
        if j != bd[row][column]:
            if j == addnum:
                return False
            elif j!= addnum:
                continue
        else:
            continue
    k = 0
    while k < 8:
        if bd[k][column] != bd[row][column]:
            if bd[k][column] == addnum:
                return False
            elif bd[k][column] != addnum:
                k += 1
        else:
            k += 1
    l = 0
    while l < 3:
        if row < 3:
            if column < 3:
                if l != column and l != row:
                    if addnum in bd[:3][l][:3]:
                        return False
                    else:
                        l += 1
                else:
                    l += 1
            elif column < 6:
                if l != (column - 3) and l != row:
                    if addnum in bd[:3][l][3:6]:
                        return False
                    else:
                        l += 1
                else:
                    l += 1
            elif column < 9:
                if l != (column - 6) and l != row:
                    if addnum in bd[:3][l][6:9]:
                        return False
                    else:
                        l += 1
                else:
                    l+=1
        elif row < 6:
            if column < 3:
                if l != column and l != (row-3): 
                    if addnum in bd[3:6][l][:3]:
                        return False
                    else:
                        l += 1
                else:
                    l += 1
            elif column < 6:
                if l != (column-3) and l != (row-3):
                    if addnum in bd[3:6][l][3:6]:
                        return False
                    else:
                        l += 1
                else:
                    l += 1
            elif column < 9:
                if l != (column-6) and l != (row-3):
                    if addnum in bd[3:6][l][6:9]:
                        return False
                    else:
                        l += 1
                else:
                    l += 1
        elif row < 9:
            if column < 3:
                if l != column and l != (row - 6):
                    if addnum in bd[6:9][l][:3]:
                        return False
                    else:
                        l += 1
                else:
                    l += 1
            elif column < 6:
                if l != (column-3) and l != (row - 6):
                    if addnum in bd[6:9][l][3:6]:
                        return False
                    else:
                        l += 1
                else:
                    l += 1
            elif column < 9:
                if l != (column-6) and l != (row - 6):
                    if addnum in bd[6:9][l][6:9]:
                        return False
                    else:
                        l += 1
                else:
                    l += 1
    return True

def sudokuboard(bd):
    num = ''
    for i in range(len(bd)):
        if i%3 ==0:
            num += '-'*25+'\n'    
        for j in range(len(bd)):
            if j%3 == 0:
                num += '| '
            num += bd[i][j] + ' '
            if j == 8:
                num += '|'
        num += '\n'
    return num

bd = [ [ '1', '.', '.', '.', '2', '.', '.', '3', '7'],
       [ '.', '6', '.', '.', '.', '5', '1', '4', '.'],
       [ '.', '5', '.', '.', '.', '.', '.', '2', '9'],
       [ '.', '.', '.', '9', '.', '.', '4', '.', '.'],
       [ '.', '.', '4', '1', '.', '3', '7', '.', '.'],
       [ '.', '.', '1', '.', '.', '4', '.', '.', '.'],
       [ '4', '3', '.', '.', '.', '.', '.', '1', '.'],
       [ '.', '1', '7', '5', '.', '.', '.', '8', '.'],
       [ '2', '8', '.', '.', '4', '.', '.', '.', '6'] ]

print sudokuboard(bd)

row = int(raw_input('Enter a row => '))
column = int(raw_input('Enter a column => '))
addnum = raw_input('Enter a number to add => ')
print

if ok_to_add(row, column, addnum) == False:
    print "This number cannot be added"
else:
    bd[row][column] = addnum
    print sudokuboard(bd)
    