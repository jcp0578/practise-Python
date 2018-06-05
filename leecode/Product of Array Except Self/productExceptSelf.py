#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
AC but not a good solution
'''
import sys
import time


class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        front_nums = [1]
        len_t = len(nums)
        for i in range(1, len_t):
            front_nums.append(front_nums[-1] * nums[i - 1])
        reverse_nums = nums[::-1]
        back_nums = [1]
        for i in range(1, len_t):
            back_nums.append(back_nums[-1] * reverse_nums[i - 1])
        back_nums = back_nums[::-1]
        return [front_nums[i] * back_nums[i] for i in range(len_t)]


if __name__ == "__main__":

    if sys.version_info.major == 3:
        t0 = time.perf_counter()
    else:
        t0 = time.time()

    test_list = [[1, 2, 3, 4], []]
    answer_list = [[24, 12, 8, 6], []]

    test = Solution()
    for i in range(len(test_list)):
        out_t = test.productExceptSelf(test_list[i])

        if out_t == answer_list[i]:
            print("\033[1;32;40m  Pass \033[0m")
        else:
            print(
                "\033[1;31;40m  Fail!!\033[0m\033[0;34;40m out \"%s\" should \"%s\" by \"%.50s\" "
                % (out_t, answer_list[i], str(test_list[i])))

    if sys.version_info.major == 3:
        print("\nRun Time is %f s" % (time.perf_counter() - t0))
    else:
        print("\nRun Time is %f s" % (time.time() - t0))
'''

'''
