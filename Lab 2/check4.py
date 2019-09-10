fname = raw_input( "Please enter your first name:")
lname = raw_input( "Please enter your last name:")+'!' 

max1 = max(len(fname),len(lname))

max2 = max(max1,len('Hello,'))

print'*'*max2+'*'*6, '\n', '**', 'Hello,'+' '*((max2+6)-6-len('Hello,')) ,'**', '\n', '**', fname +' '*((max2+6)-6-len(fname)),'**','\n', '**', lname +' '*((max2+6)-6-len(lname)), '**', '\n', '*'*max2+'*'*6