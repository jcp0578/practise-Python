#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
https://www.codewars.com/kata/integers-recreation-one

list_squared(1, 250) --> [[1, 1], [42, 2500], [246, 84100]]
list_squared(42, 250) --> [[42, 2500], [246, 84100]]

'''
import sys
sys.path.append('../')
import cw as Test
import time

from math import sqrt

debug = 1


def debug_print(flag, out):
    if debug:
        print("temp" + str(flag) + ":" + str(out))

def issquare(x):
    return sqrt(x)==int(sqrt(x))

def list_squared(m, n):
    out_list = []
    for x in range(m,n+1):
        sum_t=sum( (i**2 + (x//i)**2*(x/i!=i) ) for i in range(1,int(sqrt(x))+1) if x % i==0)
        if issquare(sum_t):
            out_list.append([x,sum_t])
    return out_list

if __name__ == "__main__":

    t0 = time.perf_counter()

    list_squared(394,16049)
    Test.assert_equals(list_squared(1, 250), [[1, 1], [42, 2500], [246, 84100]])
    Test.assert_equals(list_squared(42, 250), [[42, 2500], [246, 84100]])
    Test.assert_equals(list_squared(250, 500), [[287, 84100]])

    print (time.perf_counter() - t0)


'''
o(nlogn)
I think I'm best，hhhh!
'''
