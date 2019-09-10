"""Author: John Rivera  riverj5@rpi.edu
   
   Purpose: Read a list of dictionaries and get certain values from it.
"""

import json

def results_max(month, data, attribute):
    needed_info = []
    for dicti in data:
        if dicti['month'] == month:
            if dicti[attribute] != -9999 and dicti[attribute] != 0:
                needed_info.append((dicti[attribute], dicti['year']))
    needed_info.sort(reverse = True)
    if len(needed_info) >= 3:
        info_str = "%d: %.1f, %d: %.1f, %d: %.1f" %(needed_info[0][1], needed_info[0][0], needed_info[1][1], needed_info[1][0], needed_info[2][1], needed_info[2][0] )
    else:
        info_str = 'Not enough data'
    return info_str

def results_min(month, data, attribute):
    needed_info = []
    for dicti in data:
        if dicti['month'] == month:
            if dicti[attribute] != -9999 and dicti[attribute] != 0:
                needed_info.append((dicti[attribute], dicti['year']))
    needed_info.sort()
    if len(needed_info) >= 3:
        info_str = "%d: %.1f, %d: %.1f, %d: %.1f" %(needed_info[0][1], needed_info[0][0], needed_info[1][1], needed_info[1][0], needed_info[2][1], needed_info[2][0] )
    else:
        info_str = 'Not enough data'
    return info_str

def histogram(month, data, all_averagetemps):
    histo = ''
    for i in range(len(all_averagetemps)/10+1):
        increment = all_averagetemps[(0+10*i): (10*(i+1))]
        increment_av = sum(increment)/len(increment)
        if i != (len(all_averagetemps)/10):
            histo += '%d-%d:' %(years_averagetemps[0][0]+10*i, years_averagetemps[0][0]+10*(i+1)-1) + ' ' + '*'*int(increment_av) + '\n'
        if i == (len(all_averagetemps)/10):
            histo += '%d-%d:' %(years_averagetemps[0][0]+10*i, years_averagetemps[len(years_averagetemps)-1][0]) + ' ' + '*'*int(increment_av) + '\n'
    histo = histo.strip('\n')
    return histo
    
if __name__ == '__main__':
    data = json.loads(open("tempdata.json").read())
    
    user_idx = int(raw_input('Enter a month (1-12) => '))
    print user_idx
    
    print 'Temperatures'
    print '-' * 50
    print 'Highest max  value =>', results_max(user_idx, data, 'EMXT')
    print 'Lowest min value =>', results_min(user_idx, data, 'EMNT')
    print 'Highest days with max >= 90 =>', results_max(user_idx, data, 'DT90')
    print 'Highest days with max <= 32 =>', results_max(user_idx, data, 'DX32')
    print
    print 'Precipitation'
    print '-' * 50
    print 'Highest total =>', results_max(user_idx, data, 'TPCP')
    print 'Lowest total =>', results_min(user_idx, data, 'TPCP')
    print 'Highest snow depth =>', results_max(user_idx, data, 'TSNW')
    print 'Lowest snow depth =>', results_min(user_idx, data, 'TSNW')
    print
    print 'Average temperatures'
    print '-' * 50
    
    years_averagetemps = []
    for dicti in data:
        if dicti['MNTM'] != -9999 and dicti['MNTM'] != 0 and dicti['month'] == user_idx:
            years_averagetemps.append((dicti['year'], dicti['MNTM']))
    #print years_averagetemps
    
    all_averagetemps = []
    for i in range(len(years_averagetemps)):
        all_averagetemps.append(years_averagetemps[i][1])
    #print all_averagetemps
        
    first10 = []
    i = 0
    while i < 10:
        first10.append(all_averagetemps[i])
        i += 1
    #print first10
    
    last10 = []
    i = -1
    while i > -11:
        last10.append(all_averagetemps[i])
        i -= 1
    #print last10
    
    average_all = sum(all_averagetemps)/float(len(all_averagetemps))
    
    #print '%.1f' %(average_all)
    
    average_first10 = sum(first10)/float(len(first10))
    
    #print '%.1f' %(average_first10)
    
    average_last10 = sum(last10)/float(len(last10))
    
    print 'Overall: %.1f' %(average_all)    
    
    print 'First 10 years: %.1f' %(average_first10)
    
    print 'Last 10 years: %.1f' %(average_last10)
    
    print
    
    print histogram(user_idx, data, all_averagetemps)
    
    #i = 0
    #all_averagetemps = []
    #temps_per_year = []
    #while i < len(years_averagetemps)-1:
        #if i == 0:
            #temps_per_year.append(years_averagetemps[i][1])
            #i+=1
        #elif years_averagetemps[i][0] == years_averagetemps[i-1][0]:
            #temps_per_year.append(years_averagetemps[i][1])
            #i+=1
        #else:
            #new_av = sum(temps_per_year)/ float(len(temps_per_year))
            #all_averagetemps.append(new_av)
            #temps_per_year = []
            #temps_per_year.append(years_averagetemps[i][1])
            #i+=1
    
    #print all_averagetemps
    
    #something = sum(all_averagetemps)/len(all_averagetemps)
    #print something