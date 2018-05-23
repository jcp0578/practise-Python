#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
AC 
'''

import time
from math import sqrt

class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        isPrimes=[1]*n
        for i in range (2,int(sqrt(n)+1)):
            if isPrimes[i]==0:
                continue
            isPrimes[i*i:n:i] = [0]*len(isPrimes[i*i:n:i]) 
        return sum(isPrimes)-2
        
        

if __name__ == "__main__":

    t0 = time.perf_counter()
    testlist=[0,1,2,3,12,499979]
    test=Solution()
    for i in testlist:
        print(test.countPrimes(i))

    print(time.perf_counter() - t0)


'''

'''
