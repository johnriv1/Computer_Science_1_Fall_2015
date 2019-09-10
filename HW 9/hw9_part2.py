"""Author: John Rivera

   Purpose: Find id's from one file that match up to user inputted restaurant, then get the reviews corresponding to the id's from another file.

"""

import json
import textwrap

r = open('reviews.json')
f = open('businesses.json')

business_name = raw_input("Enter a business name => ")
print business_name

id_set = set()
business_found = True

for line in f:
    business = json.loads(line)
    if business['name'] == business_name:
        id_set.add(business['business_id'])
        
if len(id_set) == 0:
    business_found = False

if business_found == False:
    print "This business is not found"
else:
    review_list = []
    for line in r:
        review = json.loads(line)
        if review['business_id'] in id_set:
            review_list.append(review['text'])
            
    if review_list == []:
        print "No reviews for this business is found"
    else:
        
        review_output = ''
        for i in range(len(review_list)):
            review_output += "\nReview %s:" %(i + 1)
            
            text = "%s" %(review_list[i])
            text = text.split('\n\n')
            for line in text:
                textw = textwrap.wrap(line, 70)
                for line in textw:
                    review_output += '\n' + '    ' + line
                review_output += '\n\n'
            
        
        print review_output.strip('\n')
        print
        print