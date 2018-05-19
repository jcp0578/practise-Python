#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''

'''

import sys
import time




class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        x,y=1,2
        while(n-1):
            x,y,n = y, x+y, n - 1
        return x
        

            


if __name__ == "__main__":

    t0 = time.perf_counter()

    test = Solution()

    test_num=[1,2,3,1000]
    for i in test_num:
        print(test.climbStairs(i))

    print(time.perf_counter() - t0)


'''
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        df =[]
        for i in range(n):
            if i+1==1:
                df.append(1)
            if i+1==2:
                df.append(2)
            if i+1>2:
                df.append(df[i-1]+df[i-2])
        return df[n-1]
'''
