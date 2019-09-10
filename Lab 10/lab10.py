""" This is the skeleton for your lab 10. We provide a function
    here to show the use of nose.

"""

import random
import time

def addone(x):
    return x+1

def closest1(numlist):
    if len(numlist)<2:
        return (None, None)
    else:
        mindist = abs(numlist[0] + numlist[1])
        mindist_tup = (numlist[0], numlist[1])
        for i in range(len(numlist)):
            for j in range(len(numlist)):
                if i != j:
                    if abs(numlist[i]-numlist[j]) <= mindist:
                        mindist = abs(numlist[i]-numlist[j])
                        if numlist[i] <= numlist[j]:
                            mindist_tup = (numlist[i], numlist[j])
                        else:
                            mindist_tup = (numlist[j], numlist[i])
        return mindist_tup
    
def closest2(numlist):
    new_list = numlist[:]
    new_list.sort()
    mindist = (new_list[1]-new_list[0])
    for i in range(1,len(new_list)):
        if abs(new_list[i]-new_list[i-1]) <= mindist:
            mindist = abs(new_list[i]-new_list[i-1])
            if new_list[i] <= new_list[i-1]: 
                mindist_tup = (new_list[i],new_list[i-1])
            else:
                mindist_tup = (new_list[i-1],new_list[i])
    return mindist_tup
    
    

if __name__ == "__main__":
    
    ## closest1 uses double for loop, copies list ---> O(N^2) + O(N)
    ## closest2 uses one loop, sorting ---> O(N) + O(N log N)
    
    ## because (O(N^2) + O(N)) > (O(N) + O(N log N)), closest 1 will take longer
    
    floatlist = []
    i = 0
    while i < 10000:
        unit = random.uniform(0.0, 1000)
        floatlist.append(unit)
        i+=1
    print floatlist
    
    start = time.time()
    a,b = closest1(floatlist)
    end = time.time()
    print "closest1 took %f seconds" %(end-start)
    
    start2 = time.time()
    c,d = closest2(floatlist)
    end2 = time.time()
    print "closest2 took %f seconds" %(end2-start2)    