"""
   Author: John Rivera riverj5@rpi.edu

   Purpose: This program shows the user a list of legos. The user then asks for a type of lego, and the program shows a combination that could be used to make that lego. If it's not possible with the given lists of legos, the program will let the user know

"""

import hw4_util

def remove(type_requested, legos):
    i=0
    if type_requested == '2x2':
        if legos.count('2x2') >= int(quantity_wanted):
            while i < int(quantity_wanted):
                i+=1
                legos.remove('2x2')
        elif legos.count('2x1') >= (2*int(quantity_wanted)):
            while i < (2*int(quantity_wanted)):
                i+=1
                legos.remove('2x1')
        elif legos.count('1x1') >= (4*int(quantity_wanted)):        
            while i < (4*int(quantity_wanted)):
                i+=1
                legos.remove('1x1') 
    elif type_requested == '2x1':
        if legos.count('2x1') >= int(quantity_wanted):
            while i < int(quantity_wanted):
                i+=1
                legos.remove('2x1')    
        elif legos.count('1x1') >= (2*int(quantity_wanted)):
            while i < (2*int(quantity_wanted)):
                i+=1
                legos.remove('1x1')
    elif type_requested == '1x1':
        if legos.count('1x1') >= int(quantity_wanted):
            while i < int(quantity_wanted):
                i+=1
                legos.remove('1x1')
    print 'Remaining legos', legos


legos = hw4_util.read_legos()

print 'Current legos', legos

type_requested = raw_input('Type of lego wanted => ')
print type_requested
quantity_wanted = raw_input('Quantity wanted => ')
print quantity_wanted


if type_requested == '2x2':
    if legos.count('2x2') >= int(quantity_wanted):
        print 'I can use', quantity_wanted, '2x2 legos for this'
        remove(type_requested, legos)
    elif legos.count('2x1') >= (2*int(quantity_wanted)):
        print 'I can use', (2*int(quantity_wanted)), '2x1 legos for this'
        remove(type_requested, legos)
    elif legos.count('1x1') >= (4*int(quantity_wanted)):
        print 'I can use', (4*int(quantity_wanted)), '1x1 legos for this'
        remove(type_requested, legos)
    else:
        print "I don't have", quantity_wanted, '2x2 legos'
elif type_requested == '2x1':
    if legos.count('2x1') >= int(quantity_wanted):
        print 'I can use', quantity_wanted, '2x1 legos for this'
        remove(type_requested, legos)
    elif legos.count('1x1') >= (2*int(quantity_wanted)):
        print 'I can use', (2*int(quantity_wanted))
        remove(type_requested, legos)
    else:
        print "I don't have", quantity_wanted, '2x1 legos'    
elif type_requested == '1x1':
    if legos.count('1x1') >= int(quantity_wanted):
        print 'I can use', quantity_wanted, '1x1 legos for this'
        remove(type_requested, legos)
    else:
        print "I don't have", quantity_wanted, '1x1 legos'    
        
        
    