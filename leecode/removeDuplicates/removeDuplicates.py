#!/usr/bin/python3
# -*- coding: utf-8 -*-


'''
'''

import sys
import time

class Solution:
    def removeDuplicates(self, nums):
        if nums ==[]:
            return 0
        i=0
        while i <(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums.pop(i+1)
            else :
                i+=1
        return i+1


    

'''
time out
class Solution:
    def removeDuplicates(self, nums):
        if nums ==[]:
            return 0
        i=0
        next_pos=0
        while 1:
            next_pos+=nums.count(nums[i])-((next_pos)!=i)
            if (next_pos > len(nums)-1):
                break
            i+=1
            nums[i]=nums[next_pos]
        for j in range(len(nums)-1,i,-1):
            nums.pop()
        return i+1
'''

if __name__ == "__main__":

    t0 = time.perf_counter()
    test=Solution()
    num=[1]
    print(test.removeDuplicates(num))
    print(num)
    print(time.perf_counter() - t0)




'''
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        index = 0
        for i in range(1,len(nums)):
            if nums[index] != nums[i]:
                index+=1
                nums[index]=nums[i]
                
        return index+1

'''
