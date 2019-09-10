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
        datetuples.append(Date(int(dates[j][0]), int(dates[j][1]), int(dates[j][2])))
    
    return datetuples

print birthdates()
    
if __name__ == '__main__':
    
    d = Date()
    
    month_names = [ '', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',\
                        'September', 'October', 'November', 'December' ]
    
    
    #print birthdates()
    dates = birthdates()
    
    
    ###finds earliest month
    
    date = dates[1]
    datepre = dates[0]
    
    if date < datepre:
        earliest = date
    else:
        earliest = datepre
    
    datepre = earliest
        
    for i in range(2, len(dates)):
        date = dates[i]
    
        if date < datepre:
            earliest = date
            datepre = date
        else:
            earliest = datepre
              
    #print earliest
    
    
    ## finds latest birthday
    
    date = dates[1]
    datepre = dates[0]
    
    if not date < datepre:
        latest = date
    else:
        latest = datepre
    
    datepre = latest
        
    for j in range(2, len(dates)):
        
        date = dates[j]
    
        if not date < datepre:
            latest = date
            datepre = date
        else:
            latest = datepre
    
    #print latest
    
    
      
    month_occur = []
    
    for k in range(len(dates)):
        splitdates = str(dates[k])
        splitdates = splitdates.split('/')
        month_occur.append(int(splitdates[1]))
    
    ##print month_occur
    
    cntmax = 0
    month_indx = 0
    for k in month_occur:
        cnt = month_occur.count(int(k))
        if cnt > cntmax:
            cntmax = cnt
            month_indx = int(k)
    
    #print cntmax
    #print month_indx
    
    bestmonth = month_names[month_indx]
    #print bestmonth
    
    print "The earliest birthday is %s" %(earliest)
    print "The latest birthday is %s" %(latest)
    print "The month that has the most birthdays %s" %(bestmonth)