#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
AC - but O(n^2)
'''

import time


class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        len_t = len(nums)
        max_t = [1]*len_t

        for i in range(len_t):
            for j in range(i, -1, -1):
                if nums[i] > nums[j]:
                    if max_t[i] < max_t[j]+1:
                        max_t[i] = max_t[j]+1
        return max(max_t)


if __name__ == "__main__":

    t0 = time.perf_counter()

    test_list = [[10, 9, 2, 5, 3, 7, 101, 18], [
        1, 2, 5], [2], [], [1, 3, 6, 7, 9, 4, 10, 5, 6]]
    answer_list = [4, 3, 1, 0, 6]

    test = Solution()
    for i in range(len(test_list)):
        out_t = test.lengthOfLIS(test_list[i])

        if out_t == answer_list[i]:
            print("\033[1;32;40m  Pass \033[0m")
        else:
            print(
                "\033[1;31;40m  Fail!!\033[0m\033[0;34;40m out \"%s\" should \"%s\" by \"%.50s\" "
                % (out_t, answer_list[i],str(test_list[i])))

    print("\nRun Time is %f s" % (time.perf_counter() - t0))


'''

'''
