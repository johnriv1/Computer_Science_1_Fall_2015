'''
This is code to test your functions in this lab.  It is driven by a
Python module called nose, which has been imported here.  

We assume your program is called lab10.py, and we import all the
function in your program here. Make sure any other code in lab10.py
is under the 

     if __name__ == "__main__":

line.

Nose testing module is actually relative simple.

To understand it, start by looking at the main code at the bottom of
the file.  The function call nose.runmodule() causes nose to scan back
up through the preceeding code and find all functions that start with
test_.  Nose runs these functions in turn.  Each function must end
with an 'assert' statement followed by a boolean condition.  If the
boolean condition evaluate to True, nose does not say anything.  If a
condition evaluates to False, the "assert" is said to "fail".  Nose
detects these failures and tells you about them.  To see the behavior
of Nose, change some of the assert statements (for example, try == 3 for 
any test) and see what happens.

'''

import nose
from lab10 import *

def test_addone_1():
    x = 1
    assert addone(x) == 2

def test_addone_2():
    x = 0
    assert addone(x) == 1


def test_closest1_1():
    assert closest1([ 15.1, -12.1, 5.4, 11.8, 17.4, 4.3, 6.9 ]) == (4.3, 5.4)
    
def test_closest1_2():
    assert closest1([1,2]) == (1, 2)

def test_closest1_3():
    assert closest1([0,2,1,1,9]) == (1,1)
    
def test_closest1_4():
    assert closest1([1]) == (None, None)

def test_closest1_5():
    assert closest1([1, 88, 70, 2]) == (1, 2)
    
    
def test_closest2_1():
    assert closest2([ 15.1, -12.1, 5.4, 11.8, 17.4, 4.3, 6.9 ]) == (4.3, 5.4)

def test_closest2_2():
    assert closest2([1,2]) == (1, 2)
    
def test_closest2_3():
    assert closest2([0,1,2,1,9]) == (1,1)

def test_closest2_4():
    assert closest2([1, 88, 70, 2]) == (1, 2)
         
                    
if __name__ == "__main__":
    nose.runmodule()
