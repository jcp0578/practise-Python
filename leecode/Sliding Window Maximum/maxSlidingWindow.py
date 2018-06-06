#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
AC
'''
import sys
import time


class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if nums==[]:
            return []
        out_t = []
        max_t = max(nums[:k])
        out_t.append(max_t)
        for i in range(1, len(nums)-k+1):
            if nums[i+k-1] >= max_t:
                max_t = nums[i+k-1]
            elif nums[i-1] == max_t:
                max_t = max(nums[i:i+k])
            out_t.append(max_t)
        return out_t


if __name__ == "__main__":

    if sys.version_info.major == 3:
        t0 = time.perf_counter()
    else:
        t0 = time.time()

    test_list = [[1, 3, -1, -3, 5, 3, 6, 7],[1, 3, -1, -3, 5, 3, 6, 7] ]
    test_list_2 = [3,1]
    answer_list = [[3, 3, 5, 5, 6, 7],[1, 3, -1, -3, 5, 3, 6, 7]]

    test = Solution()
    for i in range(len(test_list)):
        out_t = test.maxSlidingWindow(test_list[i], test_list_2[i])

        if out_t == answer_list[i]:
            print("\033[1;32;40m  Pass \033[0m")
        else:
            print(
                "\033[1;31;40m  Fail!!\033[0m\033[0;34;40m out \"%s\" should \"%s\" by \"%.50s\" "
                % (out_t, answer_list[i],
                   str(test_list[i]) + " " + str(test_list_2[i])))

    if sys.version_info.major == 3:
        print("\nRun Time is %f s" % (time.perf_counter() - t0))
    else:
        print("\nRun Time is %f s" % (time.time() - t0))

'''
what? my solution is the fast?unbelievably

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dp = deque()
        max_numbers = []
        
        for i in range(len(nums)):
            while dp and nums[i]>=nums[dp[-1]]:
                dp.pop()
            dp.append(i)
            if i>=k and dp and dp[0]==i-k:
                dp.popleft()
            if i>=k-1:
                max_numbers.append(nums[dp[0]])
              
        return max_numbers
'''
