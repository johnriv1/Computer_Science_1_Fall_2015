"""
   Author: John Rivera   riverj5@rpi.edu
   
   Purpose: Takes two candidates and their statististics, and compares each of them in a number of possible different outcomes for the next state that votes for them to decide who would win in each case.
   
"""

def board_winners(candidate1, candidate2):
    
    winners = ''
    
    stats1 = candidate1[:]
    stats2 = candidate2[:]
        
    for newrepvotes2 in range(5):
        
        for newrepvotes1 in range(5):
            
            stateswon1 = int(stats1[1])
            statestied1 = int(stats1[2])
            repvotes1 = int(stats1[3])
            
            stateswon2 = int(stats2[1])
            statestied2 = int(stats2[2])
            repvotes2 = int(stats2[3])   
            
            if newrepvotes1 > newrepvotes2:
                stateswon1 += 1
                repvotes1 += newrepvotes1
                repvotes2 += newrepvotes2                
            elif newrepvotes2 > newrepvotes1:
                stateswon2 += 1
                repvotes2 += newrepvotes2
                repvotes1 += newrepvotes1                
            elif newrepvotes1 == newrepvotes2:
                statestied1 += 1
                statestied2 += 1
                repvotes1 += newrepvotes1
                repvotes2 += newrepvotes2 
                
            stateswonscore1 = stateswon1 * 5
            statestiedscore1 = statestied1 * 2
            repvotesscore1 = repvotes1 / 2
        
            stateswonscore2 = stateswon2 * 5
            statestiedscore2 = statestied2 * 2
            repvotesscore2 = repvotes2 / 2
        
            points1 = stateswonscore1 + statestiedscore1 + repvotesscore1
            points2 = stateswonscore2 + statestiedscore2 + repvotesscore2
            
            if points1 > points2:
                winners += cand1[0][0]
            elif points1 < points2:
                winners += cand2[0][0]
            elif points1 == points2: 
                winners += '-'
        
        winners += ''
    
    winners = (winners).strip()
    return winners

def print_board(board_winners):
    results = 'Votes|  0    1    2    3    4  ' + '\n' + '-'*5 + '|' + '-'*25

    results += '\n' + ' '*2+'0'+' '*2+'|  ' + ((board_winners(cand1, cand2)[0:5]).replace('', '    ')).strip() + ' '*2
    
    results += '\n' + ' '*2+'1'+' '*2+'|  ' + ((board_winners(cand1, cand2)[5:10]).replace('', '    ')).strip()+ ' '*2
    
    results += '\n' + ' '*2+'2'+' '*2+'|  ' + ((board_winners(cand1, cand2)[10:15]).replace('', '    ')).strip()+ ' '*2

    results += '\n' + ' '*2+'3'+' '*2+'|  ' + ((board_winners(cand1, cand2)[15:20]).replace('', '    ')).strip()+ ' '*2
    
    results += '\n' + ' '*2+'4'+' '*2+'|  ' + ((board_winners(cand1, cand2)[20:25]).replace('', '    ')).strip()+ ' '*2
    
    return results

if __name__ == "__main__":

    cand1 = raw_input('Enter candidate 1 stats ==> ')
    print cand1
    cand2 = raw_input('Enter candidate 2 stats ==> ')
    print cand2
    
    cand1 = cand1.split(',')
    cand2 = cand2.split(',')


    
    

print "Columns are %s's votes, rows are %s's votes" %(cand1[0], cand2[0])
print print_board(board_winners)