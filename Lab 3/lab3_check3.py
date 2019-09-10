"""
Program used to determine populations of foxes and bunnies

"""

## define functions for both populations

def bpop_next(bpop, fpop):
    bpop_next = (10*bpop)/(1+0.1*bpop) - 0.05*bpop*fpop
    bpop_next = int(bpop_next)
    return bpop_next

def fpop_next(bpop, fpop):
    fpop_next = 0.4 * fpop + 0.02 * fpop * bpop
    fpop_next = int(fpop_next)
    return fpop_next

bpop = int(raw_input('Number of bunnies ==> '))
bpop = max(bpop,0)
fpop = int(raw_input('Number of foxes == > '))
fpop = max(fpop,0)

##determine population numbers for the next year, using the numbers of the functions from the previous year as arguments for the next function

print "Year 1:", bpop, fpop
print "Year 2:", bpop_next(bpop, fpop), fpop_next(bpop, fpop)
print "Year 3:", bpop_next(bpop_next(bpop, fpop), fpop_next(bpop, fpop)), fpop_next(bpop_next(bpop, fpop), fpop_next(bpop, fpop))
print "Year 4:", bpop_next(bpop_next(bpop_next(bpop, fpop), fpop_next(bpop, fpop)), fpop_next(bpop_next(bpop, fpop), fpop_next(bpop, fpop))), fpop_next(bpop_next(bpop_next(bpop, fpop), fpop_next(bpop, fpop)), fpop_next(bpop_next(bpop, fpop), fpop_next(bpop, fpop)))
print "Year 5:", bpop_next(bpop_next(bpop_next(bpop_next(bpop, fpop), fpop_next(bpop, fpop)), fpop_next(bpop_next(bpop, fpop), fpop_next(bpop, fpop))), fpop_next(bpop_next(bpop_next(bpop, fpop), fpop_next(bpop, fpop)), fpop_next(bpop_next(bpop, fpop), fpop_next(bpop, fpop)))), fpop_next(bpop_next(bpop_next(bpop_next(bpop, fpop), fpop_next(bpop, fpop)), fpop_next(bpop_next(bpop, fpop), fpop_next(bpop, fpop))), fpop_next(bpop_next(bpop_next(bpop, fpop), fpop_next(bpop, fpop)), fpop_next(bpop_next(bpop, fpop), fpop_next(bpop, fpop))))