#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
二分法
'''

import sys
import time

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def __init__(self,error=10):
        self._error_version=error

    def isBadVersion(self,n):
        return True if n>=self._error_version else False


    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if self.isBadVersion(1):
            return 1
        start,end=1,n
        while end !=(start+1):
            mid=(start +end)//2
            if self.isBadVersion(mid):
                end= mid
            else:
                start=mid
        return end

            


if __name__ == "__main__":

    t0 = time.perf_counter()
    n=2
    test = Solution(2)

    print(test.firstBadVersion(n))

    print(time.perf_counter() - t0)


'''
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left,right = 1,n  
        while(left<=right):  
            mid = (left+right)/2  
            if isBadVersion(mid):  
                right = mid-1  
            else:  
                left = mid+1  
        return left  
'''
