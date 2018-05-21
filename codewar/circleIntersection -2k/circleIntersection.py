#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
#run on single file
#sys.path.append('../')

#run on Python workspace
sys.path.append('.\practise-Python\codewar')
import cw as test
import time



'''

'''
#from math import *;circleIntersection=lambda a,b,r:int([r*r*(i-sin(i))for i in[2*acos(min(sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)/2/r,1))]][0]) 

#from math import *;circleIntersection=lambda a,b,r:int([2*r*r*acos(i/r)-2*i*sqrt(r*r-i*i)if i<r else 0 for i in[sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)/2]][0]) 


#code length is 130
from math import *;circleIntersection=lambda a,b,r:int([r*r*(i-sin(i))for i in[2*acos(min(hypot(a[0]-b[0],a[1]-b[1])/2/r,1))]][0])


if __name__ == "__main__":

    t0 = time.time()

    test.assert_equals(circleIntersection([0, 0],[7, 0],5),14)

    test.assert_equals(circleIntersection([0, 0],[0, 10],10),122)

    test.assert_equals(circleIntersection([5, 6],[5, 6],3),28)

    test.assert_equals(circleIntersection([-5, 0],[5, 0],3),0)

    test.assert_equals(circleIntersection([10, 20],[-5, -15],20),15)

    test.assert_equals(circleIntersection([-7, 13],[-25, -5],17),132)

    test.assert_equals(circleIntersection([-20, -4],[-40, 29],7),0)

    test.assert_equals(circleIntersection([38, -18],[46, -29],10),64)

    test.assert_equals(circleIntersection([-29, 33],[-8, 13],15),5)

    test.assert_equals(circleIntersection([-12, 20],[43, -49],23),0)


    print(time.time() - t0)




'''
def proper_fractions(n):
    phi = n > 1 and n
    for p in range(2, int(n ** .5) + 1):
        if not n % p:
            phi -= phi // p
            while not n % p:
                n //= p
    if n > 1: phi -= phi // n
    return phi


def euler(n):
    res = 1.0*n
    p = 2
    while p*p <= n:
        if n%p == 0:
            while n%p == 0:
                n = n/p
            res *= (1.0 - (1.0/p) )
        p += 1
    
    if n > 1:
        res *= (1.0 - (1.0/n) )
    
    return int(res)

def proper_fractions(d):
    if d == 1:
        return 0
    return euler(d)
    
'''
