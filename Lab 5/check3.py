import lab05_util
import webbrowser

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
    print "\nWhat would you like to do next?"
    print "1. Visit the homepage"
    print "2. Show on Google Maps"
    print "3. Show directions to this restaurant"
    choice = int(raw_input("Your choice (1-3)? ==> "))
    if choice == 1:
        webbrowser.open(restaurants[index][4])
    elif choice ==2:
        webbrowser.open('http://www.google.com/maps/place/%s' %(restaurants[index][3]))
    elif choice ==3:
        webbrowser.open('http://www.google.com/maps/dir/110 8th Street Troy NY/%s' %(restaurants[index][3]))          
        
else:
    print "This was not a valid id"
        