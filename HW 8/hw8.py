import math
from Board import *
from Rick import *

if __name__ == "__main__":
    
    board_filename = raw_input('Board file name => ')
    print board_filename
    rick_filename = raw_input('Rick file name => ')
    print rick_filename
    
    ### Print first Board info ######################################################
        
    board_file = (open(board_filename)).read()
    all_boards = board_file.strip('\n')
    all_boards = all_boards.split('\n')
    
    #print all_boards
    
    for i in range(len(all_boards)):
        all_boards[i] = all_boards[i].split('|')
    
    #print all_boards
    boards_dict = dict()
    
    for i in range(len(all_boards)):
        boards_dict[all_boards[i][0]] = Board(all_boards[i][0:])
    
    #print boards_dict
    
    for key in boards_dict:
        print boards_dict[key]
    
    #print boards_dict
    
    print
        
    #################################################################################
        
    ### Print first Rick info #######################################################
    
    rick_file = (open(rick_filename)).read()
    all_ricks = rick_file.strip('\n')
    all_ricks = all_ricks.split('\n')
    
    for i in range(len(all_ricks)):
        all_ricks[i] = all_ricks[i].split('|')
        
    #print all_ricks
    rick_classlist = []
    for r in range(len(all_ricks)):
        rick_classlist.append(Rick(all_ricks[r]))
    
    print 'All Ricks'
    for k in rick_classlist:
        print k
    print '-'*75 + '\n'
        
    #################################################################################
    
    i = 1
    step_text = ''
    while i < 100:
        
        if i%10 == 9:
            step_text += "-"*75+"\nEnd of time %d: all free Ricks\n" %(i)
        for r in range(len(rick_classlist)):
            
            rick_dx1 = rick_classlist[r].dx
            rick_dy1 = rick_classlist[r].dy
            rick_board1 = rick_classlist[r].curr_boardname  
            
            move_text = rick_classlist[r].move(boards_dict)
            
            rick_dx2 = rick_classlist[r].dx
            rick_dy2 = rick_classlist[r].dy
            rick_board2 = rick_classlist[r].curr_boardname 
            
            if rick_dx1 != rick_dx2 or rick_dy1 != rick_dy2 or rick_board1 != rick_board2:
                print 'Time %d:' %(i), move_text + '\n'            
            
            if i%10 == 9:
                step_text += move_text
                if r == range(len(rick_classlist))[-1]:
                    step_text += '\n' + '-' * 75 + '\n'
                print step_text
                step_text = ''
            

        i += 1