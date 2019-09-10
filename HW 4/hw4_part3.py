'''
   Author: John Rivera riverj@rpi.edu

   Purpose: Takes user inputs for the flu statistics of two countries and then checks to see if the countries are included in the module. If so, it will print '-' and '+' for each of the 52 weeks of the year (also labeled by months 1-12) depending on if the value is larger or smaller than the cutoff. If the countries are invalid, program will not do anything except tell you which of the countries are not valid.  

'''
import hw4_util

def results(cdata, cutoff):
    x = 0
    results = ''
    while x < 52:
        if cdata[x]<cutoff:
            results += '-'
        else:
            results += '+'
        x+=1
    return results

first = raw_input('First country => ')
print first
second = raw_input('Second country => ')
print second

cdata1 = hw4_util.read_flu(first)
cdata2 = hw4_util.read_flu(second)

if cdata1 == [] and cdata2 == []:
    print "I could not find country", first
    print "I could not find country", second
elif cdata1 == []:
    print "I could not find country", first
elif cdata2 == []:
    print "I could not find country", second
else: 
    average1 = sum(cdata1)/len(cdata1)
    average2 = sum(cdata2)/len(cdata2)
    cutoff1 = (average1 + max(cdata1))/2
    cutoff2 = (average2 + max(cdata2))/2
    
    monthstr = ''
    i = 1
    while i<=12:
        monthstr += str(i).ljust(4)
        i+=1
    
    print ' '*12 + monthstr
    print first.ljust(12) + results(cdata1, cutoff1)
    print second.ljust(12) + results(cdata2, cutoff2)