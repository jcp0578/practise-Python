#!/usr/bin/python3
# -*- coding: utf-8 -*-


'''

'''

import sys
sys.path.append('../')
import cw as Test
import time

  
u=[1]

def dbl_linear(n):
    temp = [1]
    i=0
    tt =(2**n)
    while len(temp) < (tt):
        temp.append(temp[i]*2+1)
        temp.append(temp[i]*3+1)
        i+=1
    temp.sort()
    for j in range(i):
        if temp[j] ==temp[j+1]:
            temp.pop(j)
        else :
            pass
    return temp[n]


	# your code



if __name__ == "__main__":

    t0 = time.perf_counter()

    def testing(actual, expected):
        Test.assert_equals(actual, expected)

    Test.describe("dbl_linear")
    Test.it("Basic tests")	
    testing(dbl_linear(10), 22)
    testing(dbl_linear(20), 57)
    testing(dbl_linear(30), 91)
    testing(dbl_linear(50), 175)



    print(time.perf_counter() - t0)




'''
def last_digit(lst):
    if not lst:
        return 1
    else:
        out = 1
        for n in lst[len(lst):0:-1]:
            out = n**out
            if out > 2:
                out -= 2
                out %= 4
                out += 2
    return lst[0]**out% 10


from functools import reduce
        
def last_digit(lst):
    return reduce(lambda p, n: 1 if p == 0 or n == 1 else n if p == 1 or n == 0 else pow(n, p, 40) + 40, lst[::-1], 1) % 10


'''
