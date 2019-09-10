from check2 import *

def birthdates():
    
    f = open('birthdays.txt')
    
    f = f.read() 
    
    dates = f.split('\n')
    dates.remove('')
    
    for i in range(len(dates)):
        dates[i] = dates[i].split(' ')
    
    datetuples = []
    for j in range(len(dates)):
        datetuples.append((int(dates[j][0]), int(dates[j][1]), int(dates[j][2])))
    
    return datetuples
    
if __name__ == '__main__':
    
    d = Date()
    
    month_names = [ '', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',\
                        'September', 'October', 'November', 'December' ]
    
    
    #print birthdates()
    dates = birthdates()
    
    
    ###finds earliest month
    
    year, month, date = dates[1]
    yearpre, monthpre, datepre = dates[0]
    
    if Date(year, month, date).__lt__(Date(yearpre, monthpre, datepre)):
        earliest = year, month, date
    else:
        earliest = yearpre, monthpre, datepre
    
    yearpre, monthpre, datepre = earliest
        
    for i in range(2, len(dates)):
        year, month, date = dates[i]
    
        if Date(year, month, date).__lt__(Date(yearpre, monthpre, datepre)):
            earliest = year, month, date
            yearpre, monthpre, datepre = year, month, date
        else:
            earliest = yearpre, monthpre, datepre
              
    #print earliest
    
    
    
    ## finds latest birthday
    
    year, month, date = dates[1]
    yearpre, monthpre, datepre = dates[0]
    
    if not Date(year, month, date).__lt__(Date(yearpre, monthpre, datepre)):
        latest = year, month, date
    else:
        latest = yearpre, monthpre, datepre
    
    yearpre, monthpre, datepre = latest
        
    for j in range(2, len(dates)):
        
        year, month, date = dates[j]
    
        if not Date(year, month, date).__lt__(Date(yearpre, monthpre, datepre)):
            latest = year, month, date
            yearpre, monthpre, datepre = year, month, date
        else:
            latest = yearpre, monthpre, datepre
    
    #print latest
    
    
    month_occur = []
    
    for k in range(len(dates)):
        month_occur.append(dates[k][1])
    
    #print month_occur
    
    cntmax = 0
    month_indx = 0
    for k in month_occur:
        cnt = month_occur.count(k)
        if cnt > cntmax:
            cntmax = cnt
            month_indx = k
    
    #print cntmax
    #print month_indx
    
    bestmonth = month_names[month_indx]
    #print bestmonth
    
    print "The earliest birthday is %d/%d/%d" %(earliest[0], earliest[1], earliest[2])
    print "The latest birthday is %d/%d/%d" %(latest[0], latest[1], latest[2])
    print "The month that has the most birthdays %s" %(bestmonth)