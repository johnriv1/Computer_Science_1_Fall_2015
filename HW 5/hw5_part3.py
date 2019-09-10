"""
   Author: John Rivera   riverj@rpi.edu
   Purpose: Asks user for a file to read that contains a list baby names and their popularity, and then asks them how many names of each category (male and female) they want. Finally it takes the file, reads it, sorts it, seperates the males from the females by putting them in different lists, and prints the top amount according to how large their number for popularity are.
"""

def most_popular(gender):
    results = ''
    for i in range(len(gender)):
        results += "%s (%d)"%(gender[i][2], gender[i][0])
        if (i+1)%3 != 0 and not i == len(gender)-1:
            results += ' '
        elif (i+1)%3 == 0 and not i == len(gender)-1:
            results += '\n'
        elif i == len(gender)-1:
            results += ''
    return results

if __name__ == "__main__":
    
    file_name = raw_input('File name => ')
    print file_name
    amount = raw_input('How many names to display? => ')
    print amount
    
    babyfile = open(file_name)
    babyinfo = babyfile.read()
    babyinfo = babyinfo.split('\n')
    babyinfo.remove('')
    
    babysorted = []
    for k in range(len(babyinfo)):
        babyinfo[k] = babyinfo[k].split(',')
        babysorted.append(babyinfo[k][::-1])
        babysorted[k][0] = int(babysorted[k][0])
    
    babysorted.sort(reverse = True)
    
    males = []
    females = []
    for i in range(len(babysorted)): 
        if len(males) < int(amount):
            if 'M' == (babysorted[i])[1]:
                males.append(babysorted[i])
        if len(females) < int(amount):
            if 'F' == (babysorted[i])[1]:
                females.append(babysorted[i])
                
    print   
    print "Top female names"
    print most_popular(females)
    print "Top male names"
    print most_popular(males)