#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
AC 
'''

import time
from math import *


class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        return pow(3, round(log(n, 3))) == n


if __name__ == "__main__":

    t0 = time.perf_counter()
    testlist = [243, 1162261466]
    test = Solution()
    for i in testlist:
        print(test.isPowerOfThree(i))

    print(time.perf_counter() - t0)
'''
class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """         
        if n < 1:
            return False       
        while (n % 3) == 0:
            n //= 3         
        return n == 1
'''
