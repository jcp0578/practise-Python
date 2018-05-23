#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
AC -but not a good solution
'''

import time


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type prices: List[int]
        :rtype: int
        """
        len_t = len(nums)
        if len_t ==0:
            return 0
        # elif len_t==1:
        #     return nums[0]
        # for i in range(1,len_t):
        #     nums[i]+=nums[i-1]          
        temp=[0]
        for i in range(len_t):
            temp.append(nums[i]+temp[i])
        print(nums)
        print(temp)
        max_t = 0
        nums_t = temp[0]
        for i in range(len_t+1):
            if temp[i] < nums_t:
                nums_t = temp[i]
            else:
                max_t = max(max_t, temp[i] - nums_t)
        return max_t if max_t>0 else max(nums)


if __name__ == "__main__":

    t0 = time.perf_counter()

    test = Solution()

    test_list = [[-2,1,-3,4,-1,2,1,-5,4], [7,-1, 2, 4, 2], [2, 7, 3, 2, 3, 4, 5, 6],
                 [], [-1,-2],[-1],[2]]
#                 list(range(10000))]
    for i in test_list:
        print(test.maxSubArray(i))

    print(time.perf_counter() - t0)


'''
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

       # nums=[1,-2,1]
        yt=nums[0]
        ym=nums[0]
        for i in range(1,len(nums)):
            if yt<=0:
                yt=0
               # print(yt,ym)
            yt=yt+nums[i]
            if yt>=ym:
                ym=yt
                #print(yt,ym)
            #print(ym)
        return ym
'''
