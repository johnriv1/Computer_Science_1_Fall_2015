import lab05_util

def print_info(restaurant):
    restaurant[3] = restaurant[3].split('+')
    print restaurant[0], "(%s)" %(restaurant[5])
    print "\t" + restaurant[3][0]
    print "\t" + restaurant[3][1]
    
    if len(restaurant[6])>=3:
        newsum = sum(restaurant[6]) - min(restaurant[6]) - max(restaurant[6])
        average = float(newsum)/(len(restaurant[6])-2)
    else:
        average = float(sum(restaurant[6]))/len(restaurant[6])
    
    if average >= 4:
        print "This restaurant is rated very good, based on %d reviews" %(len(restaurant[6]))
    elif average >= 3:
        print "This restaurant is rated above average, based on %d reviews" %(len(restaurant[6]))
    elif average >= 2:
        print "This restaurant is rated average, based on %d reviews" %(len(restaurant[6]))
    elif average >= 0:
        print "This restaurant is rated bad, based on %d reviews" %(len(restaurant[6]))
    
    
restaurants = lab05_util.read_yelp('yelp.txt')

usernum = int(raw_input('Type in the id of a restaurant between 1 and 155: '))
index = usernum - 1

if usernum >= 1 and usernum <= 155:
    print_info(restaurants[index])
else:
    print "This was not a valid id"
        

