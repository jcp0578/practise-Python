#!/usr/bin/python3
# -*- coding: utf-8 -*-


'''

'''

import sys
import time

class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        nums[:]=nums[-k:]+nums[:-k]


    



if __name__ == "__main__":

    t0 = time.perf_counter()
    test=Solution()
    
    num=[1,2,3,4,5,6,7]
    k=10
    print(num,k)
    print(test.rotate(num,k))
    print(num)
    print(time.perf_counter() - t0)




'''
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        i = k % length
        nums[:] = nums[-i:]+nums[:-i]

'''
