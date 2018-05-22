#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
not right
'''

import sys
import time




class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        change=[]
        profit=[]
        for i in range(len(prices)-1):
            change.append(prices[i+1]-prices[i])
        profit_t=0
        for change_i in change:
            if change_i>0:
                profit_t+=change_i
            else:
                profit.append(profit_t)
                profit_t=0
        else:
            profit.append(profit_t)
            profit_t=0
        return max(profit)

        

            


if __name__ == "__main__":

    t0 = time.perf_counter()

    test = Solution()

    test_list=[[7,1,5,3,6,4],[7,6,4,3,1],[1,2,3,4,5,6]]
    for i in test_list:
        print(test.maxProfit(i))

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
