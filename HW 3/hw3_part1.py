'''
Author: John Rivera

Purpose: Prints the stats from 2 different teams from a module containing lists. Then,from these stats, it decides which team is better.  

'''

import hw3_util

teams = hw3_util.read_fifa()

team1 = int(raw_input('Team 1 id => '))
print team1
team2 = int(raw_input('Team 2 id => '))
print team2
print

print 'Team'.ljust(20) + 'Win'.ljust(6) + 'Draw'.ljust(6) + 'Lose'.ljust(6) + 'GF'.ljust(6) + 'GA'.ljust(6) + 'Pts'.ljust(6) + 'GD'.ljust(6)

Name1 = teams[team1][0].ljust(20)
Win1 = str(teams[team1][2]).ljust(6)
Draw1 = str(teams[team1][3]).ljust(6)
Lose1 = str(teams[team1][4]).ljust(6)
GF1 = str(teams[team1][5]).ljust(6)
GA1 = str(teams[team1][6]).ljust(6)
Pts1 = str(3 * int(Win1) + int(Draw1)).ljust(6)
GD1 = str(int(GF1) - int(GA1)).ljust(6)

print "%s%s%s%s%s%s%s%s" %(Name1,Win1,Draw1,Lose1,GF1,GA1,Pts1,GD1)

Name2 = teams[team2][0].ljust(20)
Win2 = str(teams[team2][2]).ljust(6)
Draw2 = str(teams[team2][3]).ljust(6)
Lose2 = str(teams[team2][4]).ljust(6)
GF2= str(teams[team2][5]).ljust(6)
GA2 = str(teams[team2][6]).ljust(6)
Pts2 = str(3 * int(Win2) + int(Draw2)).ljust(6)
GD2 = str(int(GF2) - int(GA2)).ljust(6)

print "%s%s%s%s%s%s%s%s" %(Name2,Win2,Draw2,Lose2,GF2,GA2,Pts2,GD2)

if int(Pts1)>int(Pts2):
    print teams[team1][0], "is better"
elif int(Pts1)<int(Pts2):
    print teams[team2][0], "is better"
elif int(Pts1)==int(Pts2):
    if int(GD1)>int(GD2):
        print teams[team1][0], "is better"
    elif int(GD1)<int(GD2):
        print teams[team2][0], "is better"
    elif int(GD1)==int(GD2):
        if int(GF1)>int(GF2):
            print teams[team1][0], "is better"
        elif int(GF1)<int(GF2):
            print teams[team2][0], "is better"
        elif int(GF1)==int(GF2):
            print "Both teams are tied"