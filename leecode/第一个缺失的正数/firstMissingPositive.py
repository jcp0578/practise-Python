#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
AC 
'''
import sys
import time


class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        out_t = 0
        for i in range(len(nums)):
            nums = list(map(lambda x: x-1, nums))
            out_t += 1
            if not nums.count(0):
                return out_t
        return out_t+1


if __name__ == "__main__":

    if sys.version_info.major == 3:
        t0 = time.perf_counter()
    else:
        t0 = time.time()

    test_list = [[1, 2, 3], [3, 4, -1, 1],
                 [7, 8, 9, 11, 12], [1, 1], [1, 1000], []]
    answer_list = [4, 2, 1, 2, 2, 1]

    test = Solution()
    for i in range(len(test_list)):
        out_t = test.firstMissingPositive(test_list[i])

        if out_t == answer_list[i]:
            print("\033[1;32;40m  Pass \033[0m")
        else:
            print(
                "\033[1;31;40m  Fail!!\033[0m\033[0;34;40m out \"%s\" should \"%s\" by \"%.50s\" "
                % (out_t, answer_list[i],
                   str(test_list[i])))

    if sys.version_info.major == 3:
        print("\nRun Time is %f s" % (time.perf_counter() - t0))
    else:
        print("\nRun Time is %f s" % (time.time() - t0))

'''
class Solution:
	def firstMissingPositive(self, nums):
		s=set()
		for x in nums:
			if x>0:
				s.add(x)
		if len(nums)==0:
			return 1
		for x in range(1,len(nums)+2):
			if x not in s:
				return x
                
class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 1
        
        k = 0
        for i in range(len(nums)):
            if nums[i] > 0 and nums[i] <= len(nums):
                nums[k] = nums[i]
                k += 1
        
        for i in range(k):
            val = abs(nums[i])
            nums[val-1] = -abs(nums[val-1])

        for i in range(k):
            if nums[i] > 0:
                return i+1
            
        return k+1
'''