import lab05_util

def print_info(restaurant):
    restaurant[3] = restaurant[3].split('+')
    print restaurant[0], "(%s)" %(restaurant[5])
    print "\t" + restaurant[3][0]
    print "\t" + restaurant[3][1]
    average = float(sum(restaurant[6]))/len(restaurant[6])
    print "Average Score: %.2f" %(average)
    
    
restaurants = lab05_util.read_yelp('yelp.txt')

print_info(restaurants[0])
print 
print_info(restaurants[1])
