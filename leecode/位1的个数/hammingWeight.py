#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
AC 
'''

#import time
from math import *

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')

if __name__ == "__main__":

    #t0 = time.perf_counter()
    testlist=[0,1,3,128]
    test=Solution()
    for i in testlist:
        print(test.hammingWeight(i))

    #print(time.perf_counter() - t0)


'''

'''
