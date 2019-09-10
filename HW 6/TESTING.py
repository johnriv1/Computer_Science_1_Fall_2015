f = open('DrWhoVillains.tsv')
file = f.readline()
file = f.read()
file = file.strip('\n')
file = file.split('\n')

for i in range(len(file)):
    file[i] = file[i].split('\t')
    for k in range(len(file[i])):
        file[i][k] = file[i][k].strip(' ')

villain_stories = set()

for j in range(len(file)):
    villain_story_tuple = int(file[j][6]), file[j][0], file[j][8]
    villain_stories.add(villain_story_tuple)

villain_stories = sorted(villain_stories)

villain_stories = All

Top_10 = villain_stories[0:10]


Top_10_print = ''
i = 0
for i in range(len(Top_10)):
    Top_10_print += '%d. %s\n' %(i+1, villain_stories[i][1])
    i+=1

Top_10_print = Top_10_print.strip('\n')
print Top_10_print

while True:
    command = raw_input('Please enter a number between 1 and 10, or -1 to end\nEnter a villain ==> ')
    print command
    if command.isdigit():
        if int(command)>= 1 and int(command) <= 10:
            print 'hi'
    else:
        if command == '-1':
            print 'Exiting'
            break
    
    print '\n' + Top_10_print




villain_stories.sort(reverse = True)
common_stories = ''
chosenvil_story_names = Top_10[int(command)-1][2].split(',')
for m in range(len(chosenvil_story_names)):
    chosenvil_story_names[m] = chosenvil_story_names[m].strip(' ')
for n in range(len(Top_10)):
    All = All[n][2].split(',')
    for p in range(All[n][2]):
        All[n][2][p] = All[n][2][p].strip(' ')        