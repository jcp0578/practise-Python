#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
AC pythonic
'''

import time
import copy

class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        out_t=[[]]
        for i in nums:
            out_t=out_t +[ [i]+temp for temp in out_t]
        return out_t


if __name__ == "__main__":

    t0 = time.perf_counter()

    test_list = [[1, 2, 3]]
    answer_list = [[[3], [1], [2], [1, 2, 3], [1, 3], [2, 3], [1, 2], []],    ]

    test = Solution()
    for i in range(len(test_list)):
        out_t = test.subsets(test_list[i])

        if out_t == answer_list[i]:
            print("\033[1;32;40m  Pass \033[0m")
        else:
            print(
                "\033[1;31;40m  Fail!!\033[0m\033[0;34;40m out \"%s\" should \"%s\" by \"%.50s\" "
                % (out_t, answer_list[i], str(test_list[i])))

    print("\nRun Time is %f s" % (time.perf_counter() - t0))
'''
class Solution:
    
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        for index in range(1<<len(nums)):#n^2
            item = []
            for j in range(len(nums)):
                if(index&(1<<j)):item.append(nums[j])
            res.append(item)
        return res
'''
