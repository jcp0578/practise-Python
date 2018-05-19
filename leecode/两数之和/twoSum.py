#!/usr/bin/python3
# -*- coding: utf-8 -*-


'''
'''

import sys
import time

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        len_t=len(nums)
        for i in range(len_t):
            target_t = target -nums[i]
            for j in range(i+1,len_t):
                if nums[j]==target_t:
                    return [i,j]
                else:
                    pass


    


if __name__ == "__main__":

    t0 = time.perf_counter()
    test=Solution()
    
    nums = [3, 2, 4, 15]
    target = 6
    print(test.twoSum(nums,target))
    print(time.perf_counter() - t0)




'''
class Solution:
    def twoSum(self, nums, target):
        if len(nums)<1:
            print('faux')
        else:
            d={}
            for i in range(len(nums)):
                if nums[i] in d:
                    return [d[nums[i]],i]
                else:
                    d[target-nums[i]]=i
    
'''
