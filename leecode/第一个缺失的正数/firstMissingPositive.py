#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
error
'''
import sys
import time


class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        nums=list(set(nums))
        sum_t = 0
        min_t = nums[0]
        max_t = nums[0]
        for num in nums:
            if num > 0:
                min_t = min(min_t, num)
                max_t = max(max_t, num)
                sum_t += num
        if min_t > 1 or max_t < 1:
            return 1
        else:
            out_t = ((min_t+max_t)*(max_t-min_t+1) >> 1)-sum_t
            return out_t if out_t else max_t+1


if __name__ == "__main__":

    if sys.version_info.major == 3:
        t0 = time.perf_counter()
    else:
        t0 = time.time()

    test_list = [[1, 2, 0], [3, 4, -1, 1], [7, 8, 9, 11, 12], [1, 1],[1,1000]]
    answer_list = [3, 2, 1, 2,2]

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

'''
