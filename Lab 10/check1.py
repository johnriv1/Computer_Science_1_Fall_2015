def closest1(numlist):
    if len(numlist)<2:
        return (None, None)
    else:
        mindist = abs(numlist[0] - numlist[1])
        mindist_tup = (numlist[0], numlist[1])
        for i in numlist:
            for j in numlist:
                if i != j:
                    if abs(i-j) <= mindist:
                        mindist_tup = (i, j)
                        mindist = abs(i-j)
        return mindist_tup

numlist = [ 15.1, -12.1, 5.4, 11.8, 17.4, 4.3, 6.9 ]
print closest1(numlist)