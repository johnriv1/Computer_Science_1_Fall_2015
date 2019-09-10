def add(m,n):
    if n == 0:
        return m
    else:
        return add(m,n-1) + 1
    
def mult(m,n):
    if m == 0 or n == 0:
        return 0
    elif n == 1:
        return m
    else:
        return add(mult(m, n-1), m)
    
def power(x,n):
    if x == 0:
        return 0
    elif n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return mult(power(x, n-1), x)
    
print
print "the calls from add(5,3):"  
print "   add(5,0) -> returns 5"
print "   add(5,1) -> returns 6"
print "   add(5,2) -> returns 7"
print "   add(5,3) -> returns 8"
print

print add(5,3)
print mult(8,3)
print power(6,4)