'''
Start to the Date class for Lab 9.  This code will not run in Python
until three methods are added:
    __init__,
    __str__
    same_day_in_year
'''

days_in_month = [ 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
month_names = [ '', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',\
                    'September', 'October', 'November', 'December' ]

class Date(object):
    def __init__(self, year=1900, month=1, day=1):
        self.year = year
        self.month = month
        self.day = day
    
    def __str__(self):
        return '%d/%s/%s' %(self.year, str((self.month)).rjust(2,'0'), str((self.day)).rjust(2,'0'))
    
    def same_day_in_year(self, other):
        if self.day == other.day and self.month == other.month:
            return True
        else:
            return False
            

if __name__ == "__main__":
    d0 = Date()
    d1 = Date(1972, 3, 27)
    d2 = Date(1998, 4, 13)
    d3 = Date(1996, 4, 13)
    d4 = Date(1999, 12, 1)
    print "d0: " + str(d0)
    print "d1: " + str(d1)
    print "d2: " + str(d2)
    print "d3: " + str(d3)
    print "d1.same_day_in_year(d2)", d1.same_day_in_year(d2) 
    print "d2.same_day_in_year(d3)", d2.same_day_in_year(d3) 
    print  
