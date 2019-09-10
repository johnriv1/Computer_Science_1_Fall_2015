import hw3_util
teams = hw3_util.read_fifa()

def stats(index):
    Name = teams[index][0].ljust(20)
    Win = str(teams[index][2]).ljust(6)
    Draw = str(teams[index][3]).ljust(6)
    Lose = str(teams[index][4]).ljust(6)
    GF = str(teams[index][5]).ljust(6)
    GA = str(teams[index][6]).ljust(6)
    Pts = str(3 * int(Win) + int(Draw)).ljust(6)
    GD = str(int(GF) - int(GA)).ljust(6)

    return "%s%s%s%s%s%s%s%s" %(Name,Win,Draw,Lose,GF,GA,Pts,GD)
    

team1 = int(raw_input('Team 1 id => '))
print team1
team2 = int(raw_input('Team 2 id => '))
print team2

print 'Team'.ljust(20) + 'Win'.ljust(6) + 'Draw'.ljust(6) + 'Lose'.ljust(6) + 'GF'.ljust(6) + 'GA'.ljust(6) + 'Pts'.ljust(6) + 'GD'.ljust(6)

print stats(team1)
print stats(team2)

