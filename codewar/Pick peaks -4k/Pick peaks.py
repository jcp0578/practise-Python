#!/usr/bin/python3
# -*- coding: utf-8 -*-


'''

'''

import sys
import time

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(len(nums)//2):
            if nums[2*i]!=nums[2*i+1]:
                return nums[2*i]
        else:
            return nums[-1]


    



if __name__ == "__main__":

    t0 = time.perf_counter()
    test=Solution()
    
    num=[4,1,2,1,2]
    print(num)
    print(test.singleNumber(num))
    print(time.perf_counter() - t0)




'''
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for x in nums:
            result ^= x
        return result
    
'''
