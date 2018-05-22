#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
AC
'''

import sys
import time


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        len_t = len(prices)
        if len_t < 2:
            return 0
        max_t = 0
        prices_t = prices[0]
        for i in range(len_t):
            if prices[i] < prices_t:
                prices_t = prices[i]
            else:
                max_t = max(max_t, prices[i] - prices_t)
        return max_t


if __name__ == "__main__":

    t0 = time.perf_counter()

    test = Solution()

    test_list = [[7, 1, 5, 3, 6, 4], [7, 2, 4, 1], [2, 7, 3, 2, 3, 4, 5, 6],
                 [], [1, 2],
                 list(range(10000))]
    for i in test_list:
        print(test.maxProfit(i))

    print(time.perf_counter() - t0)
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==0:
            return 0
        min_ = sys.maxint
        cur_max = 0
        
        for price in prices:
            if price >min_:
                cur_max = max(cur_max,price-min_)
            else:
                min_=price
        return cur_max
'''
