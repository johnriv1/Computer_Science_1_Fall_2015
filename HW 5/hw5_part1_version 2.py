"""
   Author: John Rivera   riverj5@rpi.edu
   
   Purpose: Takes two user inputs and uses them as arguments for a function that calculates the bunny and fox populations. Then it tells you whether or not the populations converged and during what cycle.

"""


def next_pop(bpop, fpop):
    bpop_next = int(max(0,round((10*bpop)/(1+0.1*bpop) - 0.05*bpop*fpop)))
    fpop_next = int(max(0,round(0.4 * fpop + 0.02 * fpop * bpop)))
    return (bpop_next, fpop_next)

def check_convergence(bpop, fpop):
    i = 0
    
    while i < 100:
        if bpop == 0 or fpop == 0:
            converged = True
            return (bpop, fpop, i, converged)
        
        ##previous = next_pop(bpop, fpop)             
        
        (bpop2, fpop2)= next_pop(bpop, fpop)
        i += 1        
        if (bpop2, fpop2) == (bpop,fpop):
            converged = True
            return (bpop2, fpop2, i, converged)
        elif bpop2 == 0 or fpop2 == 0:
            converged = True
            return (bpop2, fpop2, i, converged)
        elif i == 100:
            converged = False
            return (bpop2, fpop2, i, converged)
        (bpop,fpop)=(bpop2,fpop2)
        
        
        
if __name__ == "__main__":
    
    bpop = int(raw_input("Please enter the starting bunny population ==> "))
    print bpop
    fpop = int(raw_input("Please enter the starting fox population ==> "))
    print fpop
    
    result = check_convergence(bpop, fpop)
    
    print "(Bunny, Fox): Start (%d, %d) End: (%d, %d), Converged:" %(bpop, fpop, result[0], result[1]), result[3], "in %d generations" %(result[2])