"""
 
Process results from different countries using function that is called 4 times with print

"""

def results(country, num_wins, num_losses, num_draw, goals_for, goals_against):
    points = int(num_wins) * 3+int(num_draw)
    goal_adv = int(goals_for) - int(goals_against)    
    results = "%s\nWin: %d Lose: %d Draw: %d\nTotal number of points: %d Goal advantage: %d" %(country, num_wins, num_losses, num_draw, points, goal_adv)
    return results


## Process results for Germany

country = 'Germany'
num_wins = 2
num_losses = 1 
num_draw = 0
goals_for = 7
goals_against = 2

print results(country, num_wins, num_losses, num_draw, goals_for, goals_against)

## Process results for USA


country = 'USA'
num_wins = 1
num_draw = 1
num_losses = 1 
goals_for = 4
goals_against = 4

print results(country, num_wins, num_losses, num_draw, goals_for, goals_against)


## Process results for Argentina

country = 'Argentina'
num_wins = 3
num_draw = 0
num_losses = 0 
goals_for = 6
goals_against = 3

print results(country, num_wins, num_losses, num_draw, goals_for, goals_against)


## Process results for England

country = 'England'
num_wins = 0
num_draw = 1
num_losses = 2 
goals_for = 2
goals_against = 4

print results(country, num_wins, num_losses, num_draw, goals_for, goals_against)