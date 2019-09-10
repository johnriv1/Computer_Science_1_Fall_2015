"""
Author: John Rivera

Purpose: Asks user for a sudoku file, then asks to solve it until it is solved. 

"""
import lab06_util

def ok_to_add(row, column, addnum, bd):
    
    if int(row) <= 8 and int(row) >= 0 and int(column) <= 8 and int(column) >= 0 and int(addnum) > 0 and int(addnum) <= 9: 
        
        original = bd[row][column]
        
        bd[row][column] = '.'
        
        for j in bd[row]:
            if j == addnum:
                bd[row][column] = original
                return False
            elif j!= addnum:
                continue
        k = 0
        while k < 8:
            if bd[k][column] == addnum:
                bd[row][column] = original
                return False
            elif bd[k][column] != addnum:
                k += 1
        l = 0
        while l < 3:
            if row < 3:
                if column < 3:
                    if addnum in bd[:3][l][:3]:
                        bd[row][column] = original
                        return False
                    else:
                        l += 1
                elif column < 6:
                    if addnum in bd[:3][l][3:6]:
                        bd[row][column] = original
                        return False
                    else:
                        l += 1
                elif column < 9:
                    if addnum in bd[:3][l][6:9]:
                        bd[row][column] = original
                        return False
                    else:
                        l += 1
            elif row < 6:
                if column < 3:
                    if addnum in bd[3:6][l][:3]:
                        bd[row][column] = original
                        return False
                    else:
                        l += 1
                elif column < 6:
                    if addnum in bd[3:6][l][3:6]:
                        bd[row][column] = original
                        return False
                    else:
                        l += 1
                elif column < 9:
                    if addnum in bd[3:6][l][6:9]:
                        bd[row][column] = original
                        return False
                    else:
                        l += 1
            elif row < 9:
                if column < 3:
                    if addnum in bd[6:9][l][:3]:
                        bd[row][column] = original
                        return False
                    else:
                        l += 1
                elif column < 6:
                    if addnum in bd[6:9][l][3:6]:
                        bd[row][column] = original
                        return False
                    else:
                        l += 1
                elif column < 9:
                    if addnum in bd[6:9][l][6:9]:
                        bd[row][column] = original
                        return False
                    else:
                        l += 1
        
        bd[row][column] = original
        return True
    else:
        return 'These are not valid inputs'

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

def verify_board(bd):
    for m in bd:
        if '.' in m:
            return False
        else:
            continue 
        
    c = 0    
    for r in range(len(bd)):
        if ok_to_add(r, c, bd[r][c], bd):
            for c in range(len(bd)):
                if ok_to_add(r, c, bd[r][c], bd):
                    continue
        else:
            return False        
    return True

boardname = raw_input('Enter a file name => ')

bd = lab06_util.read_sudoku(boardname)

print sudokuboard(bd)

while verify_board(bd) == False:
    row = int(raw_input('Enter a row => '))
    column = int(raw_input('Enter a column => '))
    addnum = raw_input('Enter a number to add => ')
    print
    
    if ok_to_add(row, column, addnum, bd) == False:
        print "This number cannot be added"
        print
    elif ok_to_add(row, column, addnum, bd) == True:
        bd[row][column] = addnum
    else:
        print ok_to_add(row, column, addnum, bd)
        print
    
    print sudokuboard(bd)

if verify_board(bd):
    print "It is solved"