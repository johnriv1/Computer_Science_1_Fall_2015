"""Author: John Rivera
   
   Purpose: Find all the categories that co-occur with the user inputted category and number how many times each occur. Display the ones that occur more than or equal to the cutoff value.
"""

import json

f = open('businesses.json')

user_categ = raw_input('Enter a category ==> ')
print user_categ
cutoff = int(raw_input('Cutoff for displaying categories => '))
print cutoff

found_bool = False
co_occur_dict = dict()
for line in f:
    business = json.loads(line)
    if user_categ in business['categories']:
        found_bool = True
        for category in business['categories']:
            if category != user_categ:
                if category in co_occur_dict.keys():
                    co_occur_dict[category] += 1
                else:
                    co_occur_dict[category] = 1

if found_bool == False:
    print "Searched category is not found"
else:
    print "Categories co-occurring with %s:" %(user_categ)
    co_occur_filt = dict()
    for key in sorted(co_occur_dict):
        if co_occur_dict[key] >= cutoff:
            co_occur_filt[key] = co_occur_dict[key]
            print "%s: %d" %(key.rjust(30), co_occur_filt[key])       
            
    if len(co_occur_filt) == 0:
        print "None above the cutoff"