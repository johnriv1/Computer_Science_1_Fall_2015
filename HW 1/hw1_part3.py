name = raw_input('Please enter a name ==> ')
print name
count1970 = raw_input('Count in 1970 => ')
print count1970
count1980 = raw_input('Count in 1980 => ')
print count1980
count1990 = raw_input('Count in 1990 => ')
print count1990
count2000 = raw_input('Count in 2000 => ')
print count2000

change1970_1980 = float(count1980)-float(count1970)
percentchange1970_1980 = 100*(change1970_1980)/float(count1970)

change1980_1990 = float(count1990)-float(count1980)
percentchange1980_1990 = 100*(change1980_1990)/float(count1980)

change1990_2000 = float(count2000)-float(count1990)
percentchange1990_2000 = 100*(change1990_2000)/float(count1990)

Average_change = (percentchange1970_1980 + percentchange1980_1990 + percentchange1990_2000)/3

print '\nBabies named', name + '\n' + '*' * (13+len(name))

print '\nYear / Total / % change from previous decade'
print '1970 /', count1970
print '1980 /', count1980, '/ %', '%.2f' %percentchange1970_1980
print '1990 /', count1990, '/ %', '%.2f' %percentchange1980_1990
print '2000 /', count2000, '/ %', '%.2f' %percentchange1990_2000
print 'Average change: %', '%.2f' %Average_change