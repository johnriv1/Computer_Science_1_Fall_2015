import textwrap

def find_common_villains(command, Top_10, All):
    chosenvil_story_names = Top_10[int(command)-1][2].split(',')
    for m in range(len(chosenvil_story_names)):
        chosenvil_story_names[m] = chosenvil_story_names[m].strip(' ')
    
    chosenvil_story_names_set = set()
    for story in chosenvil_story_names:
        chosenvil_story_names_set.add(story) 
    
    common_villains = []   
    for n in range(len(All)):          
        vil_storynames = All[int(n)][2].split(',')
        for p in range(len(vil_storynames)):
            vil_storynames[p] = vil_storynames[p].strip(' ')
        vil_storynames = set(vil_storynames)
        
        if chosenvil_story_names_set & vil_storynames != set([]):
            common_villains.append(All[n][1])
    
    common_villains.sort()
    return common_villains


def find_unique_story(command, Top_10, All):
    
    chosenvil_story_names = Top_10[int(command)-1][2].split(',')
    for m in range(len(chosenvil_story_names)):
        chosenvil_story_names[m] = chosenvil_story_names[m].strip(' ')
    
    chosenvil_story_names_set = set()
    for story in chosenvil_story_names:
        chosenvil_story_names_set.add(story) 
    
    for n in range(len(All)):          
        vil_storynames = All[int(n)][2].split(',')
        for p in range(len(vil_storynames)):
            vil_storynames[p] = vil_storynames[p].strip(' ')
        vil_storynames = set(vil_storynames)
        
        if All[int(n)][1] != Top_10[int(command)-1][1]:
            chosenvil_story_names_set = chosenvil_story_names_set - vil_storynames
    
    chosenvil_story_names_set = sorted(chosenvil_story_names_set)
    return chosenvil_story_names_set


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

villain_stories.sort(reverse = True)

Top_10 = villain_stories[0:10]

Top_10_print = ''
i = 0
for i in range(len(Top_10)):
    Top_10_print += '%d. %s\n' %(i+1, villain_stories[i][1])
    i+=1

Top_10_print = Top_10_print.strip('\n')
print
print Top_10_print

while True:
    command = raw_input('Please enter a number between 1 and 10, or -1 to end\nEnter a villain ==> ')
    print command
    if command.isdigit():
        if int(command)>= 1 and int(command) <= 10:
            vil_string = ''
            
            for name in find_common_villains(command, Top_10, villain_stories):
                if name != Top_10[int(command) - 1][1]:
                    vil_string += name +', '
            
            print Top_10[int(command) - 1][1] + ' in %d stories, with the following other villains:' %(len(Top_10[int(command)-1][2].split(',')))
            print '='*50  
            vil_string = vil_string.strip(' ')
            vil_string = vil_string.strip(',')
            vil_string = textwrap.wrap(vil_string,70)
            for story in vil_string:
                print story
            
            #print find_unique_story(command, Top_10, villain_stories)
            print
            story_string =''
            if len (find_unique_story(command, Top_10, villain_stories)) == 0:
                print 'There are no stories with only this villain'
                print '='*50
            else:
                print 'The stories that only features %s are:' %(Top_10[int(command) - 1][1])
                print '='*50
                for name in find_unique_story(command, Top_10, villain_stories):
                    story_string += name + ', '
                story_string = story_string.strip(' ')
                story_string = story_string.strip(',')
                story_string = textwrap.wrap(story_string, 70)
                for story in story_string:
                    print story

    else:
        if command == '-1':
            print 'Exiting'
            break
    
    print '\n' + Top_10_print


        
    #return chosenvil_story_names_set

#print find_common_villains('7', Top_10, villain_stories)


        